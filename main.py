from gpiozero import Button
button = Button(pin=2, bounce_time=0.2)

counter = 0
        # Get the dimensions of the screen
screen_resolution = QApplication.instance().desktop().screenGeometry()
screen_width, screen_height = screen_resolution.width(), screen_resolution.height()

        # Define the label
label = QLabel()
label.setText("Huge Label")
label.setAlignment(Qt.AlignCenter)

        # Define the font and size
font = QFont("Arial", 50, QFont.Bold)
label.setFont(font)

        # Define the geometry of the label
label_width = screen_width
label_height = screen_height

label.setGeometry(QRect(0, 0, label_width, label_height))

        # Set the geometry of the main window
setGeometry(0, 0, screen_width, screen_height)
setWindowState(Qt.WindowFullScreen)
while True:
    button.wait_for_press()
    button.wait_for_release()
    counter = counter+1
    print('You pushed me')
    print(counter)
    label.setText(counter)