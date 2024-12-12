import os

# List of folder paths
folder_paths = [
    '/home/ab/depth_map_dataset/dataset_images/dataset_images/images7',  
  
]
starting_number = 3489  # Replace with the initial starting number

# Process each folder separately
for folder_path in folder_paths:
    # Get a sorted list of files in the folder, sorting numerically based on filename
    files = sorted(os.listdir(folder_path), key=lambda x: int(os.path.splitext(x)[0]))

    # Rename files in sequence
    for index, filename in enumerate(files):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]
        
        # Create the new name with the correct sequence
        new_name = f"{starting_number + index}{file_extension}"
        
        # Full paths
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        
        # Rename file
        os.rename(old_file, new_file)
        print(f"Renamed '{filename}' to '{new_name}' in folder '{folder_path}'")
    
    # Update starting number for the next folder
    starting_number += len(files)

