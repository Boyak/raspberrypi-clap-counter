from gpiozero import Button
button = Button(2)

counter = 0

while True:
    button.wait_for_press(bounce_time=0.2)
    button.wait_for_release()
    counter = counter+1
    print('You pushed me')
    print(counter)