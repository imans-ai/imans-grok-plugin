"""Exercise release boundaries: credentials, references and archive contents."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

import jsonschema

from package import build
from validate import ROOT, ROOT_FILES, package_paths, validate


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ROOT_FILES:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        for folder in ("assets", "skills", "docs"):
            shutil.copytree(ROOT / folder, self.root / folder)

    def test_archive_is_reproducible_and_excludes_private_repository_files(self):
        (self.root / ".env").write_text(
            "PRIVATE_FIXTURE=do-not-distribute", encoding="utf-8"
        )
        (self.root / ".git").mkdir()
        (self.root / ".git" / "config").write_text(
            "private remote fixture", encoding="utf-8"
        )
        archive = build(self.root)
        first = archive.read_bytes()
        self.assertEqual(first, build(self.root).read_bytes())
        with ZipFile(archive) as result:
            expected = {
                "imans/" + p.relative_to(self.root).as_posix()
                for p in package_paths(self.root)
            }
            self.assertEqual(set(result.namelist()), expected)
            self.assertTrue(
                all(
                    ".env" not in name and "/.git/" not in name
                    for name in result.namelist()
                )
            )
            self.assertIn("imans/.cursor-plugin/plugin.json", result.namelist())

    def test_embedded_credentials_and_tool_filters_are_rejected(self):
        path = self.root / "mcp.json"
        clean = json.loads(path.read_text(encoding="utf-8"))
        for field, value in (
            ("headers", {"Authorization": "Bearer fixture"}),
            ("allowed_tools", ["search"]),
        ):
            with self.subTest(field=field):
                data = json.loads(json.dumps(clean))
                data["mcpServers"]["imans"][field] = value
                path.write_text(json.dumps(data), encoding="utf-8")
                with self.assertRaises((ValueError, jsonschema.ValidationError)):
                    validate(self.root)

    def test_broken_skill_reference_blocks_a_release(self):
        (self.root / "skills/imans/references/actions.md").unlink()
        with self.assertRaisesRegex(ValueError, "Undistributed local reference"):
            validate(self.root)

    def test_nested_environment_file_blocks_a_release(self):
        (self.root / "assets/.env").write_text(
            "PRIVATE_FIXTURE=do-not-distribute", encoding="utf-8"
        )
        with self.assertRaisesRegex(ValueError, "Unexpected distribution file"):
            validate(self.root)

    def test_local_reference_outside_package_blocks_a_release(self):
        path = self.root / "README.md"
        path.write_text(
            path.read_text(encoding="utf-8") + "\n[Private source](../private.txt)\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValueError, "Undistributed local reference"):
            validate(self.root)

    def test_manifest_version_drift_blocks_a_release(self):
        path = self.root / ".cursor-plugin/plugin.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["version"] = "9.0.0"
        path.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Cursor manifest differs"):
            validate(self.root)


if __name__ == "__main__":
    unittest.main()
