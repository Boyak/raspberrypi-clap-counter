from gpiozero import Button
button = Button(2)

counter = 0

while True:
    button.wait_for_press()
    button.wait_for_release()
    counter = counter+1
    print('You pushed me')
    print(counter)