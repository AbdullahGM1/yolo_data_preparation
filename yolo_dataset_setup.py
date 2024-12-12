import os
import shutil
import random

# Base folder for YOLO dataset
base_folder = '/home/ab/depth_map_dataset/yolo_dataset_training'

# Define paths for source folders
images_folder = '/home/ab/depth_map_dataset/dataset_labels/images'
labels_folder = '/home/ab/depth_map_dataset/dataset_labels/labels'

# Define paths for output folders
train_images_folder = os.path.join(base_folder, 'train/images')
train_labels_folder = os.path.join(base_folder, 'train/labels')
test_images_folder = os.path.join(base_folder, 'test/images')
test_labels_folder = os.path.join(base_folder, 'test/labels')
valid_images_folder = os.path.join(base_folder, 'valid/images')
valid_labels_folder = os.path.join(base_folder, 'valid/labels')

# Ensure output directories exist
os.makedirs(train_images_folder, exist_ok=True)
os.makedirs(train_labels_folder, exist_ok=True)
os.makedirs(test_images_folder, exist_ok=True)
os.makedirs(test_labels_folder, exist_ok=True)
os.makedirs(valid_images_folder, exist_ok=True)
os.makedirs(valid_labels_folder, exist_ok=True)

# Get all image files
image_files = sorted(os.listdir(images_folder))
total_files = len(image_files)

# Shuffle and split indices
random.shuffle(image_files)
train_count = int(total_files * 0.7)
test_count = int(total_files * 0.2)
valid_count = total_files - train_count - test_count

# Split files
train_files = image_files[:train_count]
test_files = image_files[train_count:train_count + test_count]
valid_files = image_files[train_count + test_count:]

# Function to copy images and corresponding labels
def copy_files(image_list, dest_images_folder, dest_labels_folder):
    for image_file in image_list:
        # Determine paths for image and corresponding label
        image_src = os.path.join(images_folder, image_file)
        label_src = os.path.join(labels_folder, os.path.splitext(image_file)[0] + '.txt')

        # Copy image and label if the label exists
        if os.path.exists(label_src):
            shutil.copy(image_src, dest_images_folder)
            shutil.copy(label_src, dest_labels_folder)
        else:
            print(f"Warning: Label file for {image_file} not found.")

# Copy files for train, test, and validation sets
copy_files(train_files, train_images_folder, train_labels_folder)
copy_files(test_files, test_images_folder, test_labels_folder)
copy_files(valid_files, valid_images_folder, valid_labels_folder)

print("Dataset split and copied successfully.")

