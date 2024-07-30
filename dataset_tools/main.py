from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os

def main():
    app = QApplication([])
    window = QWidget()

    #initial size
    window.setGeometry(0, 0, 800, 800)
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
    cringe_btn.clicked.connect(lambda: on_clicked(cringe_btn.text(), label))

    funny_btn = QPushButton("funny")
    funny_btn.setStyleSheet("background-color: #76db91")
    #funny_btn.resize(150, 50)
    funny_btn.clicked.connect(lambda: on_clicked(funny_btn.text(), label))

    neutral_btn = QPushButton("neutral")
    neutral_btn.setStyleSheet("background-color: #adadad")
    #neutral_btn.resize(150, 50)
    neutral_btn.clicked.connect(lambda: on_clicked(neutral_btn.text(), label))

    hlayout.addWidget(cringe_btn)
    hlayout.addWidget(neutral_btn)
    hlayout.addWidget(funny_btn)

    main_layout.addLayout(hlayout)

    window.setLayout(main_layout)
    window.show()


    app.exec_()

# function to control button clicks
def on_clicked(msg, label):
    print('hi')
    set_image(label)

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
    global file_counter
    directory = "C:\\Users\\timka\\Documents\\code\\python\\Tektim-Bot\\data\\images\\break-room_media"
    files = os.listdir(directory)
    #print(len(files))

    file = directory + "\\" + files[file_counter]
    file_counter = file_counter + 1
    #print(file)

    return file

def set_image(label):
    pixmap = QPixmap(retrieve_image())
    label.setPixmap(pixmap)
    label.resize(pixmap.width(), pixmap.height())

file_counter = 0

if __name__ == '__main__':
    main()