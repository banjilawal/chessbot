import os

def find_missing_init_files(base_dirs):
    missing = []
    for base_dir in base_dirs:
        for root, dirs, files in os.walk(base_dir):
            # Skip hidden directories like .venv or __pycache__
            if any(part.startswith('.') or part == '__pycache__' for part in root.split(os.sep)):
                continue
            if '__init__.py' not in files:
                missing.append(root)
    return missing

if __name__ == "__main__":
    # Adjust these paths based on your repo layout
    base_dirs = ["src", "tests"]
    missing_dirs = find_missing_init_files(base_dirs)

    if missing_dirs:
        print("🚨 Missing __init__.py in the following directories:")
        for d in missing_dirs:
            print(f" - {d}")
    else:
        print("✅ All package directories have __init__.py files.")