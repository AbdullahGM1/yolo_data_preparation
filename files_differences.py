import os

# Paths to the two folders
folder1_path = '/home/ab/depth_map_dataset/dataset/images'
folder2_path = '/home/ab/depth_map_dataset/dataset/labels'

# Get lists of file names (without extensions) in each folder
folder1_files = {os.path.splitext(f)[0] for f in os.listdir(folder1_path)}
folder2_files = {os.path.splitext(f)[0] for f in os.listdir(folder2_path)}

# Find differences
only_in_folder1 = folder1_files - folder2_files
only_in_folder2 = folder2_files - folder1_files

# Print results
if only_in_folder1:
    print("Files only in folder 1:")
    for filename in sorted(only_in_folder1):
        print(filename)

if only_in_folder2:
    print("\nFiles only in folder 2:")
    for filename in sorted(only_in_folder2):
        print(filename)

if not only_in_folder1 and not only_in_folder2:
    print("No differences found. Both folders contain the same files.")

