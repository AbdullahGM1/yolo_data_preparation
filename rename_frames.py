import os
import re

# Define the directory containing your images
directory = "/home/ab/depth_map_dataset/images2_copy"

# Get a list of files in the directory that match the pattern "_<number>.extension"
files = [f for f in os.listdir(directory) if re.match(r"^_\d+\.\w+$", f)]

# Sort files by the numbers in their names
files.sort(key=lambda x: int(re.search(r"\d+", x).group()))

# Rename files sequentially starting from 1
for i, filename in enumerate(files, start=1):
    # Extract the file extension
    ext = os.path.splitext(filename)[1]
    # Create the new filename
    new_name = f"{i}{ext}"
    # Get the full paths
    old_path = os.path.join(directory, filename)
    new_path = os.path.join(directory, new_name)
    # Rename the file
    os.rename(old_path, new_path)
    print(f"Renamed '{filename}' to '{new_name}'")

print("Renaming completed.")
