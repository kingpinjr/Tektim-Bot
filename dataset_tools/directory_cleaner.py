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

img_size = 256
col_num = img_size ** 2

prep_dir = 'data\\images\\preprocessed'
print('Before:')
files = os.listdir(prep_dir)
list_file_counts(files)

# Define the directory you want to scan
directory = 'C:\\Users\\timka\\Documents\\code\\python\\Tektim-Bot\\data\\images'

ext_whitelist = ['.jpeg','.png','.jpg']

dir_blacklist = ('data\\images\\processed',
                 'data\\images\\preprocessed',
                 'data\\images\\live_input')

# List all files in the directory
#files = os.listdir(directory)
for root, dirs, files in os.walk(directory, topdown=False):
    for file in files:
        if not root.endswith(dir_blacklist): # all files that aren't in blacklisted directories
            extension = os.path.splitext(file)[1]
            # filter based off of file type
            file_path = directory + "\\" + file
            if extension not in ext_whitelist:
                #print(file_path)
                try:
                    os.remove(file_path)
                    print("Removed: " + file_path)
                except Exception as e:
                    print(f'An error has occured: {e}')
            
            else:
                img = imread(file_path)
                img = resize(img, (img_size, img_size))
                img = img.flatten()
                # filter bsaed off size of file; only accept files that flatten to be 900
                if(len(img) != col_num):
                    try:
                        os.remove(file_path)
                        print("Removed: " + file_path)
                    except Exception as e:
                        print(f'An error has occured: {e}')
                
                else:
                    shutil.move(file_path, prep_dir)
                

print('\nAfter:')
files = os.listdir(prep_dir)
list_file_counts(files)
