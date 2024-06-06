import os
import random
import shutil

# Set the paths for your dataset
dataset_dir = 'dataset'
train_dir = 'train'
valid_dir = 'valid'
test_dir = 'test'

# Create directories if they don't exist
os.makedirs(os.path.join(train_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(train_dir, 'labels'), exist_ok=True)
os.makedirs(os.path.join(valid_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(valid_dir, 'labels'), exist_ok=True)
os.makedirs(os.path.join(test_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(test_dir, 'labels'), exist_ok=True)

# Get a list of all jpg files
jpg_files = [f for f in os.listdir(dataset_dir) if f.endswith('.jpg')]

# Shuffle the list
random.shuffle(jpg_files)

# Calculate the split indices
total_files = len(jpg_files)
test_count = int(total_files * 0.1)
valid_count = int(total_files * 0.2)
train_count = total_files - test_count - valid_count

# Split the files
test_files = jpg_files[:test_count]
valid_files = jpg_files[test_count:test_count + valid_count]
train_files = jpg_files[test_count + valid_count:]

def move_files(files, images_destination, labels_destination):
    for file in files:
        base_name = os.path.splitext(file)[0]
        jpg_path = os.path.join(dataset_dir, base_name + '.jpg')
        txt_path = os.path.join(dataset_dir, base_name + '.txt')
        shutil.move(jpg_path, os.path.join(images_destination, base_name + '.jpg'))
        if os.path.exists(txt_path):
            shutil.move(txt_path, os.path.join(labels_destination, base_name + '.txt'))

# Move the files to their respective directories
move_files(test_files, os.path.join(test_dir, 'images'), os.path.join(test_dir, 'labels'))
move_files(valid_files, os.path.join(valid_dir, 'images'), os.path.join(valid_dir, 'labels'))
move_files(train_files, os.path.join(train_dir, 'images'), os.path.join(train_dir, 'labels'))

print(f"Moved {len(train_files)} files to {os.path.join(train_dir, 'images')} and {os.path.join(train_dir, 'labels')}")
print(f"Moved {len(valid_files)} files to {os.path.join(valid_dir, 'images')} and {os.path.join(valid_dir, 'labels')}")
print(f"Moved {len(test_files)} files to {os.path.join(test_dir, 'images')} and {os.path.join(test_dir, 'labels')}")
