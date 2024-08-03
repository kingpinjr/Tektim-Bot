import os
from collections import Counter

def list_file_counts(files):
    # Extract file extensions and count them
    extensions = [os.path.splitext(file)[1] for file in files]
    extension_counts = Counter(extensions)

    # Print the counts
    for ext, count in extension_counts.items():
        print(f'{ext}: {count}')

# Define the directory you want to scan
directory = 'C:\\Users\\timka\\Documents\\code\\python\\Tektim-Bot\\data\images\\general_a186558b-e053-4982-90e0-a61444b6298d\\general_media'

# List all files in the directory
files = os.listdir(directory)

print('Before:')
list_file_counts(files)