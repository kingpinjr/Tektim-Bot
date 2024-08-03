import os
from collections import Counter
from skimage.io import imread
from skimage.transform import resize
import shutil

def list_file_counts(files):
    # Extract file extensions and count them
    extensions = [os.path.splitext(file)[1] for file in files]
    extension_counts = Counter(extensions)

    # Print the counts
    for ext, count in extension_counts.items():
        print(f'{ext}: {count}')

#img_size = 256
#col_num = img_size ** 2

prep_dir = 'data\\images\\preprocessed'
print('Images in Preprocessed Before:')
files = os.listdir(prep_dir)
list_file_counts(files)

# Define the directory you want to scan
parent_directory = 'data\\images'

ext_whitelist = ['.jpeg','.png','.jpg']

dir_blacklist = ('data\\images\\preprocessed',
                 'data\\images\\live_input',
                 'data\\images\\cringe',
                 'data\\images\\neutral',
                 'data\\images\\funny')

# List all files in the directory
#files = os.listdir(directory)
for root, dirs, files in os.walk(parent_directory, topdown=False):
    for file in files:
        if not root.endswith(dir_blacklist): # all files that aren't in blacklisted directories
            extension = os.path.splitext(file)[1]
            # filter based off of file type
            file_path = root + "\\" + file
            if extension not in ext_whitelist:
                #print(file_path)
                try:
                    os.remove(file_path)
                    print("Removed: " + file_path)
                except Exception as e:
                    print(f'An error has occured: {e}')
            
            else:
                shutil.move(file_path, prep_dir)


                

print('\nImages in Preprocessed After:')
files = os.listdir(prep_dir)
list_file_counts(files)

# delete emptied image folders now
subdirectories = next(os.walk(parent_directory))[1]
print(subdirectories)
for dir in subdirectories:
    dir_name = parent_directory + "\\" + dir
    if dir_name not in dir_blacklist:
        print("Removing " + dir_name)
        os.rmdir(dir_name)
