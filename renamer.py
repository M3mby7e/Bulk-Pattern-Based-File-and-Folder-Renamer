import os

def collect_renames(root_dir, pattern):
    """
    Walk through root_dir and collect all files/folders whose names
    contain 'pattern'. Returns a list of (old_path, new_path) pairs.
    """
    renames = []

    for current_path, folders, files in os.walk(root_dir):
        # Folders
        for folder in folders:
            if pattern in folder:
                old_path = os.path.join(current_path, folder)
                new_name = folder.replace(pattern, "")
                new_path = os.path.join(current_path, new_name)
                if old_path != new_path:
                    renames.append((old_path, new_path))

        # Files
        for filename in files:
            if pattern in filename:
                old_path = os.path.join(current_path, filename)
                new_name = filename.replace(pattern, "")
                new_path = os.path.join(current_path, new_name)
                if old_path != new_path:
                    renames.append((old_path, new_path))

    return renames


def apply_renames(renames):
    """
    Apply rename operations from deepest path to shallowest to avoid
    'path not found' errors when parent dirs are renamed.
    """
    # Sort by depth (number of path separators), deepest first
    renames.sort(key=lambda p: p[0].count(os.sep), reverse=True)

    for old_path, new_path in renames:
        print(f"Renaming:\n  {old_path}\n  → {new_path}")
        try:
            # Skip if the source no longer exists (already moved/renamed by something else)
            if not os.path.exists(old_path):
                print(f"  [SKIP] Source does not exist anymore: {old_path}")
                continue

            # Optional: warn if target already exists
            if os.path.exists(new_path):
                print(f"  [SKIP] Target already exists: {new_path}")
                continue

            os.rename(old_path, new_path)
        except FileNotFoundError as e:
            print(f"  [ERROR] FileNotFoundError: {e}")
        except PermissionError as e:
            print(f"  [ERROR] PermissionError: {e}")
        except OSError as e:
            print(f"  [ERROR] OSError: {e}")


if __name__ == "__main__":
    # Accept user input, strip whitespace and optional quotes
    directory = input("Enter directory path: ").strip().strip('"').strip("'")
    pattern = input("Enter pattern to remove: ").strip().strip('"').strip("'")

    print(f"\nUsing directory: {directory}")
    print(f"Pattern to remove: {pattern!r}\n")

    if not os.path.isdir(directory):
        print("❌ Invalid directory path!")
    else:
        print("Scanning and planning renames...\n")
        renames = collect_renames(directory, pattern)

        if not renames:
            print("No files or folders found containing that pattern.")
        else:
            print(f"Found {len(renames)} items to rename.\n")
            apply_renames(renames)
            print("\n✔ Done.")
