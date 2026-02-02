import pyautogui as pa
from time import sleep

# Music that will be played
music = input('Music: ')
sleep(1)
# Use .press to use keyboard keys
pa.press('win')

# Use .write to type
pa.write("chrome")
sleep(2)
pa.press("ENTER")
sleep(3)

# Use .click to click somewhere in the screen
pa.click(x=582, y=375)

pa.write("youtube.com")
sleep(1)
pa.press('ENTER')
sleep(5)
pa.click(x=548, y=120)
pa.write(music)
sleep(2)
pa.press("ENTER")
sleep(2)
pa.click(x=525, y=372)