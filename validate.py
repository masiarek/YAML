import os
import glob
import re
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

# Regex pattern to detect quotes on active (non-comment) portions of a line.
quote_pattern = re.compile(r'^[^#]*[\'"]')

for file_path in files:
    filename = os.path.basename(file_path)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse with StrictYAML
        load(content)

        # Check for quotes line by line
        affected_lines = []
        for line_num, line in enumerate(content.splitlines(), start=1):
            if quote_pattern.search(line):
                # Strip leading/trailing whitespace so it aligns cleanly in the output
                affected_lines.append(f"      Line {line_num}: {line.strip()}")

        if affected_lines:
            summary_lines.append(f"⚠️ Valid (Quotes Detected): {filename}")
            # Add all the affected lines directly below the filename
            summary_lines.extend(affected_lines)
        else:
            summary_lines.append(f"✅ Valid & Clean: {filename}")

    except YAMLError as exc:
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