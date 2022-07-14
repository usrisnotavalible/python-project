#                       Healthy Programmer
import pygame
from playsound import playsound
from time import time

()
from datetime import datetime
from pygame import mixer


def gym_songs(file, pause):
    # file = "drink.wav"   It will only use water sound ot others
    pygame.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while True:
        z = input()
        if z == pause:
            mixer.music.stop()
            break


def log_now(msg):
        f= open("logs.txt", "a")
        f.write(f"{msg} and {datetime.now()}\n")


if __name__ == '__main__':
    # gymsongs("drink.wav", "pause")
    init_water = time()
    init_eyes = time()
    init_exe = time()
    water_sec = 10
    eye_sec = 13
    exe_sec = 30
    while True:
        #For Water
        # if time() - init_water > water_sec:  # wil give us exact time
        #     print("Please drink water and type 'Done' after drinking")
        #     gym_songs("drink.wav", "Done")
        #     init_water = time()  # will start calculating time again
        #     log_now("You had drink water at:")


        #For Eyes
        if time() - init_eyes > eye_sec:  # wil give us exact time
            print("Please relax your eye look here and there")
            gym_songs("Birds.wav", "Done")
            init_eyes = time()  # will start calculating time again
            log_now("You had done eye exercise at:")



        #For Physical exercise
        if time() - init_exe > exe_sec:  # wil give us exact time
            print("Go to the gym")
            gym_songs("Nonstop.wav", "Done")
            init_exe = time()  # will start calculating time again
            log_now("You had done  exercise at:")

