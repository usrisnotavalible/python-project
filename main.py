#                       Healthy Programmer
import pygame
from time import time

()
from datetime import datetime
from pygame import mixer


# Giving water sound start and stop
def gym_songs(file, pause):
    mixer.init()
    mixer.music.load(file)
    mixer.play()

    while True:
        z = input()
        if z == pause:
            mixer.music.stop()
            break


def log_now(msg):
    with open("log.txt", "a"):
        f.write(f"{msg} and {datetime.now()}")


if __name__ == '__main__':
    # gymsongs("water.mp3", "pause")
    init_water = time()
    init_eyes = time()
    init_exe = time()
    water_sec = 10
    eye_sec = 13
    exe_sec = 30
    while True:
        if time() - init_water > water_sec:  # wil give us exact time
            print("Drkink water and type 'Done'")
            gym_songs("water.mp3", "Done")
            init_water = time()  # will start calculating time again


