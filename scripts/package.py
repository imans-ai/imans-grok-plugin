"""Build a deterministic, validated plugin ZIP without repository history."""

from __future__ import annotations

import hashlib
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from validate import ROOT, load_json, validate


def build(root: Path = ROOT) -> Path:
    """Archive the validated public package and write a SHA-256 sidecar."""
    paths = validate(root)
    version = load_json(root / "plugin.json")["version"]
    output = root / "dist" / f"imans-grok-plugin-{version}.zip"
    output.parent.mkdir(exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path in paths:
            name = "imans/" + path.relative_to(root).as_posix()
            entry = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            data = path.read_bytes()
            if path.suffix in (".md", ".json", ".svg") or path.name in (
                "LICENSE",
                "NOTICE",
            ):
                data = data.replace(b"\r\n", b"\n")
            archive.writestr(entry, data)
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix(output.suffix + ".sha256").write_text(
        f"{digest}  {output.name}\n", encoding="utf-8"
    )
    return output


if __name__ == "__main__":
    print(build())
