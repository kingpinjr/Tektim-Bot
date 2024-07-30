from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(600, 200, 200, 200)
    window.setWindowTitle("Image Tagging Tool")

    layout = QVBoxLayout()

    label = QLabel("XD")
    textbox = QTextEdit()
    button = QPushButton("press")
    button.clicked.connect(lambda: on_clicked(textbox.toPlainText()))

    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()


    app.exec_()

def on_clicked(msg):
    #print('hi')
    mbox = QMessageBox()
    mbox.setText(msg)
    mbox.exec_()

if __name__ == '__main__':
    main()