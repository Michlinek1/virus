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
    import os
    from pathlib import Path
    if os.path.exists("wallpaper.jpg"):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, str(Path(__file__).parent.resolve()) + "\wallpaper.jpg" , 3)
    else:
        print("wallpaper.jpg doesn't exist!")

def playSound(music: str):
    from time import sleep
    from playsound import playsound as play
    while True:
        play(music)
        sleep(1)

#kill(['brave.exe', 'spotify.exe'])
#changeWallPaper()
#playSound('sound.mp3')
