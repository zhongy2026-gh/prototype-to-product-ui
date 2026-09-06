#!/usr/bin/env python3
"""Dependency-free structural and portability checks for this Skill package."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "VALIDATION.md",
    "LICENSE",
    "agents/openai.yaml",
    "references/prototype-implementation.md",
    "references/visual-qa.md",
    "references/local-launch-and-handoff.md",
    "templates/page-state-matrix.md",
    "templates/ui-acceptance-report.md",
    "examples/stitch-to-existing-app.md",
)

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ""}
FORBIDDEN_PATTERNS = {
    "macOS personal path": re.compile(r"/Users/[^/\s]+/"),
    "Windows personal path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\"),
    "unfinished placeholder": re.compile(r"\[?TODO[:\]]|YOUR[_ -]?(?:API[_ -]?KEY|SECRET)", re.I),
    "assigned secret": re.compile(r"(?:api[_-]?key|password|secret|access[_-]?token)\s*[:=]\s*[\"'][^\"']+[\"']", re.I),
}


def fail(messages: list[str]) -> None:
    for message in messages:
        print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        skill = skill_path.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---", skill, re.S)
        if not match:
            errors.append("SKILL.md has invalid frontmatter boundaries")
        else:
            frontmatter = match.group(1)
            name = re.search(r"^name:\s*([^\n]+)$", frontmatter, re.M)
            description = re.search(r"^description:\s*([^\n]+)$", frontmatter, re.M)
            if not name or name.group(1).strip() != root.name:
                errors.append("frontmatter name must match the package directory")
            if not description or not description.group(1).strip():
                errors.append("frontmatter description is missing")
            elif len(description.group(1).strip()) > 1024:
                errors.append("frontmatter description exceeds 1024 characters")

        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", skill):
            if not re.match(r"^(?:https?://|#)", target) and not (root / target).exists():
                errors.append(f"SKILL.md links to a missing file: {target}")

    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root)
        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{relative} contains {label}")

    metadata = root / "agents/openai.yaml"
    if metadata.is_file():
        content = metadata.read_text(encoding="utf-8")
        if "$prototype-to-product-ui" not in content:
            errors.append("agents/openai.yaml default prompt must name the Skill")

    license_path = root / "LICENSE"
    if license_path.is_file() and "MIT License" not in license_path.read_text(encoding="utf-8"):
        errors.append("LICENSE is not the expected MIT license")

    if errors:
        fail(sorted(set(errors)))

    print(f"Package validation passed: {root}")


if __name__ == "__main__":
    main()
