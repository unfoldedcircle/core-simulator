#!/usr/bin/env python3
"""
Git tag release script to simplify creating git tags with changelog since last release.
Copyright (c) 2026 Unfolded Circle.
"""

import os
import subprocess
import sys
import tempfile
import re
import json
import argparse


def run_command(command, check=True):
    """Run a shell command and return the output."""
    try:
        result = subprocess.run(command, shell=True, check=check, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        if check:
            sys.exit(1)
        return None


def get_latest_tag():
    """Get the latest git tag."""
    return run_command("git describe --tags --abbrev=0", check=False)


def get_changelog_from_file(version):
    """Get changelog from the CHANGELOG.md file in the root directory."""
    changelog_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "CHANGELOG.md")
    if not os.path.exists(changelog_path):
        print(f"Error: CHANGELOG.md not found at {changelog_path}")
        sys.exit(1)

    with open(changelog_path, "r") as f:
        lines = f.readlines()

    start_idx = -1
    for i, line in enumerate(lines):
        if line.startswith("## "):
            header_line = line.strip()
            if re.match(r'^## v' + re.escape(version) + r'(?:\s+-\s+.*|\s*)$', header_line):
                start_idx = i
                break

    if start_idx == -1:
        print(f"Error: Version '{version}' not found in CHANGELOG.md")
        sys.exit(1)

    extracted_lines = []
    for i in range(start_idx + 1, len(lines)):
        if lines[i].startswith("## "):
            break
        extracted_lines.append(lines[i])

    changelog = "".join(extracted_lines).strip()

    # Transform extracted changelog
    # Replace ### headers: simply remove the hash characters. Example: ### Fixed --> Fixed
    changelog = re.sub(r'^###\s*', '', changelog, flags=re.MULTILINE)
    # Replace all markdown links: keep only text, remove https link.
    # Example: ([#123](https://github.com/foobar/repo/issues/123)). --> (#123)
    changelog = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', changelog)
    changelog = re.sub(r'\)\.', ')', changelog)

    return changelog


def is_valid_semver(tag):
    """
    Check if the version is a valid semver format.

    https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string
    """
    return re.match(r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$", tag) is not None



def main():
    parser = argparse.ArgumentParser(description="Git tag script to simplify creating git tags.")
    parser.add_argument("version", help="The new version in semver format (e.g., 0.21.0)")
    parser.add_argument("--dry-run", action="store_true", help="Do not create or push the tag")
    args = parser.parse_args()

    version = args.version
    dry_run = args.dry_run
    if not is_valid_semver(version):
        print(f"Error: Version '{version}' is not in valid semver format (X.Y.Z)")
        sys.exit(1)

    new_tag = f"v{version}"

    # Check if tag already exists
    existing_tags = run_command("git tag").split("\n")
    if new_tag in existing_tags:
        print(f"Error: Tag '{new_tag}' already exists.")
        sys.exit(1)

    latest_tag = get_latest_tag()
    print(f"Latest tag: {latest_tag}")

    changelog = get_changelog_from_file(version)
    if not changelog:
        print(f"No changelog found for version {version}")
        sys.exit(0)

    initial_message = f"Release {new_tag}\n\n{changelog}"

    # Create temporary file for editing
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tmp:
        tmp.write(initial_message.encode("utf-8"))
        tmp_path = tmp.name

    editor = os.environ.get("EDITOR", "nano")
    subprocess.call([editor, tmp_path])

    with open(tmp_path, "r") as f:
        tag_message = f.read().strip()

    os.unlink(tmp_path)

    if not tag_message:
        print("Tag message is empty. Aborting.")
        sys.exit(1)

    print("\n--- Tag Message ---")
    print(tag_message)
    print("-------------------\n")

    confirm = input(f"Create and push tag {new_tag}? (y/n): ")
    if confirm.lower() == "y":
        if dry_run:
            print(f"[DRY-RUN] Would create annotated tag: {new_tag}")
            print(f"[DRY-RUN] Would push tag {new_tag} to origin.")
        else:
            # Create annotated tag
            run_command(f'git tag -a {new_tag} -m "{tag_message}"')
            print(f"Tag {new_tag} created locally.")

            # Push tag
            run_command(f"git push origin {new_tag}")
            print(f"Tag {new_tag} pushed to origin.")
    else:
        print("Aborted.")


if __name__ == "__main__":
    main()
