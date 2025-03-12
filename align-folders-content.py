import os

raw_extention = ".raf"
jpg_extention = ".jpg"

# Define paths (Update these before running)
jpg_folder = "jpg_folder"
raf_folder = "raf_folder"

# Get the set of JPG file names (without extensions)
jpg_files = {os.path.splitext(f)[0] for f in os.listdir(jpg_folder) if f.lower().endswith(jpg_extention)}
raw_files = os.listdir(raf_folder)

print("Before alignment:")
print(f"Total files in jpg_folder: {len(jpg_files)}")
print(f"Total files in raf_folder: {len(raw_files)}")

# Process RAF files in the second folder
for raf_file in raw_files:
    if raf_file.lower().endswith(raw_extention):
        raf_name = os.path.splitext(raf_file)[0]  # Get filename without extension
        if raf_name not in jpg_files:
            raf_path = os.path.join(raf_folder, raf_file)
            os.remove(raf_path)  # Delete RAF file
            print(f"Deleted: {raf_path}")

print("After alignment:")
print(f"Total files in jpg_folder: {len(jpg_files)}")
print(f"Total file in raf_folder: {len(os.listdir(raf_folder))}")

print("Cleanup complete!")