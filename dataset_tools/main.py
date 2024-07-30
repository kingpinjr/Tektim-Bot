from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os
import shutil

def main():
    app = QApplication([])
    window = QWidget()

    #initial size
    window.setGeometry(0, 0, 1200, 800)
    set_center(window)
    window.setWindowTitle("Image Tagging Tool")

    main_layout = QVBoxLayout()

    # get the first image to pop up
    pixmap = QPixmap(retrieve_image())
    label = QLabel()
    label.setPixmap(pixmap)
    label.setAlignment(Qt.AlignCenter)

    label.resize(pixmap.width(), pixmap.height())   

    main_layout.addWidget(label)

    # layout for buttons
    hlayout = QHBoxLayout()
    cringe_btn = QPushButton("cringe")
    cringe_btn.setStyleSheet("background-color: #c74646")
    #cringe_btn.resize(150, 50)
    cringe_btn.clicked.connect(lambda: on_clicked(label))

    funny_btn = QPushButton("funny")
    funny_btn.setStyleSheet("background-color: #76db91")
    #funny_btn.resize(150, 50)
    funny_btn.clicked.connect(lambda: on_clicked(label))

    neutral_btn = QPushButton("neutral")
    neutral_btn.setStyleSheet("background-color: #adadad")
    #neutral_btn.resize(150, 50)
    neutral_btn.clicked.connect(lambda: on_clicked(label))

    hlayout.addWidget(cringe_btn)
    hlayout.addWidget(neutral_btn)
    hlayout.addWidget(funny_btn)

    main_layout.addLayout(hlayout)

    window.setLayout(main_layout)
    window.show()


    app.exec_()

# function to control button clicks
def on_clicked(label):
    global lock
    if not lock:

        # move image into new folder
        process_dir = "C:\\Users\\timka\\Documents\\code\\python\\Tektim-Bot\\data\\images\\processed"
        # Ensure the destination directory exists
        if not os.path.exists(process_dir):
            os.makedirs(process_dir)

        global current_image_path
        # move the file
        shutil.move(current_image_path, process_dir)

        # grab a new image
        set_image(label)
        print('grabbing new image')
    else:
        print('locked, ran out of images!')

# function to center window on monitor screen
def set_center(window):
    # Get the screen's rectangle
    screen_rect = QDesktopWidget().availableGeometry()

    # Get the rectangle of the window
    window_rect = window.frameGeometry()

    # Calculate the center point of the screen
    center_point = screen_rect.center()

    # Move the rectangle of the window to the center
    window_rect.moveCenter(center_point)

    # Move the top-left point of the window to the top-left point of the moved rectangle
    window.move(window_rect.topLeft())

def retrieve_image():
    global lock
    global current_image_path
    directory = "C:\\Users\\timka\\Documents\\code\\python\\Tektim-Bot\\data\\images\\break-room_media"
    files = os.listdir(directory)
    #print(len(files))
    if len(files) == 0:
        file =  "C:\\Users\\timka\\Documents\\code\\python\\Tektim-Bot\\dataset_tools\\out_of_images.png"
        lock = True

    else:
        file = directory + "\\" + files[0]
        current_image_path = file

    return file

def set_image(label):
    pixmap = QPixmap(retrieve_image())

    # need to check for scaling
    max_width = 600
    max_height = 600

    if pixmap.width() > max_width:
        pixmap = pixmap.scaled(max_width, pixmap.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    
    if pixmap.height() > max_height:
        pixmap = pixmap.scaled(pixmap.width(), max_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    label.setPixmap(pixmap)
    label.resize(pixmap.width(), pixmap.height())

lock = False
current_image_path = ""

if __name__ == '__main__':
    main()