import pyautogui as pg
from time import sleep
import os

os.chdir(os.path.abspath(os.path.dirname(__file__)))


if pg.confirm(text='Want to send snap streaks?', buttons=["STREAKS", "STOPPPP!"]) == "STREAKS":

    sleep(5)

    os.system(r'start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"  --profile-directory=Default --app-id=abdndmcckigaeepaljhpcngbfdkbiggb')

    sleep(5) 

    OnButton = pg.locateOnScreen("OnButton.png", confidence=.5)
    OnButtonx, OnButtony = pg.center(OnButton)
    pg.click(OnButtonx, OnButtony)

    sleep(1)

    PictureButton = pg.locateOnScreen("TakePicture.png", confidence=.5)
    PictureButtonx, PictureButtony = pg.center(PictureButton)
    pg.click(PictureButtonx, PictureButtony)

    sleep(1)

    TextButton = pg.locateOnScreen("Text.png", confidence=.5)
    TextButtonx, TextButtony = pg.center(TextButton)
    pg.click(TextButtonx, TextButtony)
    sleep(0.2)
    pg.write("Automated python streaks by Mitchell Gibbons. This is sent by a bot basically.")

    sleep(1)

    SendToButton = pg.locateOnScreen("SendTo.png", confidence=.5)
    SendToButtonx, SendToButtony = pg.center(SendToButton)
    pg.click(SendToButtonx, SendToButtony)

    sleep(1)

    for person in ["person", "person1", "person2", "person3", "person4"]:
        pg.write(person)
        sleep(0.2)
        SelectButton = pg.locateOnScreen("PersonSelect.png", confidence=.5)
        SelectButtonx, SelectButtony = pg.center(SelectButton)
        pg.click(SelectButtonx, SelectButtony)
        sleep(0.2)
        
        ExitButton = pg.locateOnScreen("Exit.png", confidence=.9)
        ExitButtonx, ExitButtony = pg.center(ExitButton)
        pg.click(ExitButtonx, ExitButtony)
        sleep(0.2)
        pg.click(ExitButtonx, ExitButtony)


    sleep(1)

    SendButton = pg.locateOnScreen("Send.png", confidence=.5)
    SendButtonx, SendButtony = pg.center(SendButton)
    pg.click(SendButtonx, SendButtony)

else:
    os.sys.exit()