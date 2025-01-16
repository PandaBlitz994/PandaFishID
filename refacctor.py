import os

# Class mapping (old class index -> new class index)
class_mapping = {
    0: 3, 1: 4, 2: 2, 3: 5, 4: 6, 5: 7, 6: 8
}

# Directory containing your YOLO annotation files
annotations_dir = r'E:\dowlonds\fish breeds.v9-v7.0-sweetlips-moorish.yolov8 (1)\train\labels'

# Iterate through each annotation file
for filename in os.listdir(annotations_dir):
    if filename.endswith('.txt'):  # Only process .txt files
        file_path = os.path.join(annotations_dir, filename)
        
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Refactor the labels
        refactored_lines = []
        for line in lines:
            parts = line.strip().split()
            old_class = int(parts[0])
            new_class = class_mapping.get(old_class, old_class)  # Use the new class from the mapping
            parts[0] = str(new_class)
            refactored_lines.append(' '.join(parts))
        
        # Save the refactored annotations
        with open(file_path, 'w') as file:
            file.write('\n'.join(refactored_lines) + '\n')

print("Annotations refactored successfully!")