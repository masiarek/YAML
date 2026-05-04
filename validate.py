import os
import glob
from strictyaml import load, YAMLError

# Your target directory
directory = '/Volumes/T7/_trash/2026-05-03/YAML/YAML_library/1_positive'

# Find all .yaml and .yml files
files = glob.glob(os.path.join(directory, '*.yaml')) + glob.glob(os.path.join(directory, '*.yml'))

# Sort the files alphabetically by their base file name
files.sort(key=lambda filepath: os.path.basename(filepath).lower())

if not files:
    print("No YAML files found in the specified directory.")

# Lists to track our outputs
failed_files = []
summary_lines = []

for file_path in files:
    filename = os.path.basename(file_path)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        load(content)
        # Store the success message instead of printing it
        summary_lines.append(f"✅ Valid: {filename}")

    except YAMLError as exc:
        # Store the failure message and the detailed error
        summary_lines.append(f"❌ Invalid: {filename}")
        failed_files.append((filename, f"Invalid YAML syntax/features:\n{exc}"))
    except Exception as e:
        summary_lines.append(f"❌ Error: {filename}")
        failed_files.append((filename, f"Could not read file:\n{e}"))

# 1. Print the detailed errors first (if any)
if failed_files:
    print("\n" + "=" * 50)
    print(f"🚨 ERROR DETAILS ({len(failed_files)} files failed)")
    print("=" * 50)
    for filename, error_msg in failed_files:
        print(f"\n📄 {filename}:")
        print(f"   {error_msg}")

    print("\n" + "=" * 50)
    print("📊 FINAL SUMMARY")
    print("=" * 50)
else:
    print("\n" + "=" * 50)
    print("🎉 ALL CLEAR: All YAML files are valid!")
    print("=" * 50)

# 2. Print the clean list at the very bottom
for line in summary_lines:
    print(line)