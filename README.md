## Bulk Pattern-Based File and Folder Renamer

This tool scans a directory recursively and renames all files and
folders whose names contain a specific pattern. The tool removes the
pattern from each name and applies the renaming operations in the
correct order to avoid directory structure issues.

### Features

-   Recursively scans all subdirectories.
-   Detects both files and folders that contain the given pattern.
-   Generates a rename plan before performing changes.
-   Applies renames from deepest path to shallowest to avoid path not
    found errors.
-   Skips rename operations where the target already exists.
-   Handles errors such as missing paths and permission issues.
-   Uses only the built-in Python `os` module.

### How It Works

#### 1. Collect Renames

    collect_renames(root_dir, pattern)

This function walks through the directory and builds a list of rename
operations.

Each rename is stored as:

    (old_path, new_path)

#### 2. Apply Renames

    apply_renames(renames)

Renames are sorted by depth (deepest paths first) to avoid directory
conflicts.

### Usage

Run the script:

    python rename_tool.py

You will be asked for a directory path and a pattern to remove.

### Example Use Cases

-   Removing suffixes from batches of files.
-   Cleaning temporary or backup markers.
-   Standardizing naming conventions.

### Notes

-   Renaming is permanent; use carefully.
-   Works on Windows, macOS, and Linux.
