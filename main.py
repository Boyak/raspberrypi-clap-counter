from gpiozero import Button
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QRect


class MyMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Get the dimensions of the screen
        screen_resolution = QApplication.instance().desktop().screenGeometry()
        screen_width, screen_height = screen_resolution.width(), screen_resolution.height()

        # Define the label
        self.label = QLabel(self)
        self.label.setText("Huge Label")
        self.label.setAlignment(Qt.AlignCenter)

        # Define the font and size
        font = QFont("Arial", 50, QFont.Bold)
        self.label.setFont(font)

        # Define the geometry of the label
        label_width = screen_width
        label_height = screen_height

        self.label.setGeometry(QRect(0, 0, label_width, label_height))

        # Set the geometry of the main window
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowState(Qt.WindowFullScreen)

    def keyPressEvent(self, event):
        # Allow closing the app by pressing the Escape key
        if event.key() == Qt.Key_Escape:
            self.close()


def main():
    app = QApplication(sys.argv)
    main_win = MyMainWindow()
    main_win.show()

    button = Button(pin=2, bounce_time=0.2)
    counter = 0
    while True:
        button.wait_for_press()
        button.wait_for_release()
        counter = counter+1
        print('You pushed me')
        print(counter)
        self.label.setText(counter)


    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

