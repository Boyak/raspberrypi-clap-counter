import sys
import time
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QRect, pyqtSignal, QThread
from gpiozero import Button

class MyThread(QThread):
    # Define a new signal called 'trigger' that has no arguments.
    trigger = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)
        self.button = Button(2, bounce_time=0.2)
        self.counter = 0
        self.button.when_pressed = self.button_pressed

    def button_pressed(self):
        self.counter += 1

    def run(self):
        while True:
            self.trigger.emit(self.counter)
            time.sleep(0.1)  # Frequency of checking button state

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

        self.thread = MyThread()
        self.thread.trigger.connect(self.update_label)
        self.thread.start()

    def keyPressEvent(self, event):
        # Allow closing the app by pressing the Escape key
        if event.key() == Qt.Key_Escape:
            self.close()

    def update_label(self, counter):
        # Replace with your logic to fetch new text
        new_text = "Updated Text. Button presses: " + str(counter)
        self.label.setText(new_text)

def main():
    app = QApplication(sys.argv)
    main_win = MyMainWindow()
    main_win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
