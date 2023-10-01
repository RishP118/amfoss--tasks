import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea, QPushButton, QHBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class Display(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pokemon")
        self.cap_images = self.fetch_captured_images()
        self.index = 0
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.init_ui()
       
    def init_ui(self):
        mlayout = QVBoxLayout()
        blayout = QHBoxLayout()
        self.image_label = QLabel()
        mlayout.addWidget(self.image_label)
        self.pname_label = QLabel()
        mlayout.addWidget(self.pname_label)
        self.pname_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        previous = QPushButton("Previous")
        previous.setFixedSize(160, 60)  # Set the size of the button
        previous.setStyleSheet(" QPushButton { margin: 10px; border: 2px solid red; border-radius: 10px; font-weight: bold; color:white; background-color:black;} QPushButton:hover {background-color: red; color:black;}")
       
        next = QPushButton("Next")
        next.setFixedSize(160, 60)  # Set the size of the button
        next.setStyleSheet("QPushButton { margin: 10px; border: 2px solid red; border-radius: 10px; font-weight: bold; color:white; background-color:black;} QPushButton:hover {background-color: red; color:black;}")
        
        previous.clicked.connect(self.show_pimage)
        next.clicked.connect(self.show_nimage)
        
        blayout.addWidget(previous)
        blayout.addWidget(next)
        

        self.central_widget.setLayout(mlayout)
        # Add the button layout to the main layout
        mlayout.addLayout(blayout)

        self.central_widget.setLayout(mlayout)

        # Display the initial image
        self.displayimage(self.index)

    def displayimage(self, index):
        if 0 <= index < len(self.cap_images):
            imagepath = self.cap_images[index]
            pixmap = QPixmap(imagepath)
            self.image_label.setPixmap(pixmap)
            pname = os.path.splitext(os.path.basename(imagepath))[0]
            self.pname_label.setText(f"Name: {pname}")

    def show_nimage(self):
        self.index += 1
        if self.index >= len(self.cap_images):
            self.index = 0
        self.displayimage(self.index)

    def show_pimage(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.cap_images) - 1
        self.displayimage(self.index)

    def fetch_captured_images(self):
        capdir = 'cap'
        if os.path.exists(capdir) and os.path.isdir(capdir):
            imagefiles = [os.path.join(capdir, filename) for filename in os.listdir(capdir) if filename.endswith('.png')]
            return imagefiles
        else:
            return []
    
if __name__ == "__main__":
    app = QApplication([])
    window = Display()
    window.show()
    app.exec()
