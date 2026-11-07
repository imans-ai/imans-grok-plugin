"""Validate the distributable Imans plugin without contacting the MCP service."""

from __future__ import annotations

import json
import re
from pathlib import Path
from xml.etree import ElementTree

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = "https://mcp.imans.ai/mcp"
ROOT_FILES = (
    "plugin.json",
    ".cursor-plugin/plugin.json",
    "mcp.json",
    "README.md",
    "README.pt-BR.md",
    "LICENSE",
    "NOTICE",
    "SECURITY.md",
    "CHANGELOG.md",
)


def package_paths(root: Path) -> list[Path]:
    """Return only public runtime assets and documentation inside the root."""
    paths = [root / name for name in ROOT_FILES]
    folders = {"assets": {".svg", ".png"}, "skills": {".md"}, "docs": {".md"}}
    for folder, suffixes in folders.items():
        for path in (root / folder).rglob("*"):
            if not path.is_file():
                continue
            relative = path.relative_to(root / folder)
            if path.suffix not in suffixes or any(
                part.startswith(".") for part in relative.parts
            ):
                raise ValueError(f"Unexpected distribution file: {path}")
            paths.append(path)
    for path in paths:
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError(f"Package path escapes root: {path}")
        if not path.is_file():
            raise ValueError(f"Required package file missing: {path}")
    return sorted(paths, key=lambda p: p.relative_to(root).as_posix())


def load_json(path: Path) -> dict:
    """Read one UTF-8 JSON object."""
    return json.loads(path.read_text(encoding="utf-8"))


def validate(root: Path = ROOT) -> list[Path]:
    """Check schemas, host manifests, credentials, skills and local references."""
    paths = package_paths(root)
    manifest = load_json(root / "plugin.json")
    mcp = load_json(root / "mcp.json")
    for name, value in (("plugin", manifest), ("mcp", mcp)):
        schema = load_json(ROOT / "scripts" / "schemas" / f"{name}.schema.json")
        jsonschema.Draft202012Validator(schema).validate(value)

    cursor = load_json(root / ".cursor-plugin" / "plugin.json")
    expected_cursor = {k: v for k, v in manifest.items() if k != "$schema"}
    expected_cursor["logo"] = "assets/logo.svg"
    if cursor != expected_cursor:
        raise ValueError("Cursor manifest differs from the portable manifest")
    if mcp["mcpServers"] != {"imans": {"type": "streamable-http", "url": ENDPOINT}}:
        raise ValueError("Use the complete remote MCP with host-managed OAuth only")
    if not re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")):
        raise ValueError("Release version must use major.minor.patch")

    skills = list((root / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("No discoverable skills")
    for path in skills:
        content = path.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        if len(parts) != 3 or parts[0].strip():
            raise ValueError(f"Missing skill frontmatter: {path}")
        metadata = yaml.safe_load(parts[1])
        if not isinstance(metadata, dict):
            raise ValueError(f"Skill frontmatter must be a mapping: {path}")
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if not isinstance(name, str) or name != path.parent.name:
            raise ValueError(f"Skill name must match its directory: {path}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            raise ValueError(f"Invalid skill name: {path}")
        if not isinstance(description, str) or not description.strip():
            raise ValueError(f"Missing skill description: {path}")

    distributed = {p.resolve() for p in paths}
    for path in paths:
        if path.suffix != ".md":
            continue
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            destination = (path.parent / target.split("#", 1)[0]).resolve()
            if destination not in distributed:
                raise ValueError(f"Undistributed local reference in {path}: {target}")

    svg = ElementTree.parse(root / cursor["logo"]).getroot()
    if (
        svg.tag != "{http://www.w3.org/2000/svg}svg"
        or svg.get("viewBox") != "0 0 512 512"
    ):
        raise ValueError("Marketplace logo must be a square SVG")
    if svg.find("{http://www.w3.org/2000/svg}rect") is None:
        raise ValueError("Marketplace logo needs a background plate")
    return paths


if __name__ == "__main__":
    files = validate()
    print(
        f"Valid Imans plugin: {len(files)} distribution files; full remote MCP; no credentials"
    )
