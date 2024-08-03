import os
from collections import Counter
from skimage.io import imread
from skimage.transform import resize

def list_file_counts(files):
    # Extract file extensions and count them
    extensions = [os.path.splitext(file)[1] for file in files]
    extension_counts = Counter(extensions)

    # Print the counts
    for ext, count in extension_counts.items():
        print(f'{ext}: {count}')

# Define the directory you want to scan
directory = 'C:\\Users\\timka\\Documents\\code\\python\\Tektim-Bot\\data\\images\\break-room_media'

whitelist = ['.jpeg','.png','.jpg']

# List all files in the directory
files = os.listdir(directory)

print('Before:')
list_file_counts(files)
'''

for file in files:
    extension = os.path.splitext(file)[1]

    # filter based off of file type
    file_path = directory + "\\" + file
    if extension not in whitelist:
        #print(file_path)
        try:
            os.remove(file_path)
            print("Removed: " + file_path)
        except Exception as e:
            print(f'An error has occured: {e}')
    
    else:
        img = imread(file_path)
        img = resize(img, (15,15))
        img = img.flatten()
        # filter bsaed off size of file; only accept files that flatten to be 900
        if(len(img) != 900):
            try:
                os.remove(file_path)
                print("Removed: " + file_path)
            except Exception as e:
                print(f'An error has occured: {e}')

files = os.listdir(directory)
print('\nAfter:')
list_file_counts(files)
'''