import pyautogui as pa
from time import sleep

user = "YourUSername"
password = "YourPassword"

pa.press('win')
pa.write("chrome")
sleep(1)
pa.press('ENTER')
sleep(3)

pa.click(x=582, y=375)
sleep(1)
pa.write("suap ifsp")  # Destination
sleep(2)
pa.press("ENTER")
sleep(1)
pa.click(x=345, y=310)

# Login, sometimes you should get the inputs' position, it migth be different depending on each website
# You don't necessary need to use the mouse pointer in some login's forms, use ENTER instead
sleep(3)
pa.write(user)
pa.press("ENTER")
pa.write(password)
sleep(1)
pa.press("ENTER")

