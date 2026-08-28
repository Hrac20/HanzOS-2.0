import sys
import time
import os
import tkinter as tk
from PIL import Image, ImageTk
from pycaw.pycaw import AudioUtilities

print ("Loading in process...")

for i in range(0, 101, 10):
        blocks = i // 10
        print(f"\r[{'█' * blocks}{' ' * (10 - blocks)}] {i}%", end="")
        time.sleep(0.5)

print()
print("Loading complete.")
time.sleep(2)
print("Checking for integrity...")
time.sleep(0.5)

print("GPU Check...")
time.sleep(0.3)
for i in range(0, 101, 10):
        blocks = i // 10
        print(f"\r[{'█' * blocks}{' ' * (10 - blocks)}] {i}%", end="")
        time.sleep(0.5)
print()
print("GPU: OK")
time.sleep(0.5)
print("CPU Check...")
time.sleep(0.3)
for i in range(0, 101, 10):
        blocks = i // 10
        print(f"\r[{'█' * blocks}{' ' * (10 - blocks)}] {i}%", end="")
        time.sleep(0.5)
print()
print("CPU: OK")
time.sleep(0.5)
print("RAM Check...")
time.sleep(0.3)
for i in range(0, 101, 10):
        blocks = i // 10
        print(f"\r[{'█' * blocks}{' ' * (10 - blocks)}] {i}%", end="")
        time.sleep(0.5)
print()
print("RAM: OK")
time.sleep(0.5)
print("WiFi Check...")
time.sleep(0.3)
for i in range(0, 101, 10):
        blocks = i // 10
        print(f"\r[{'█' * blocks}{' ' * (10 - blocks)}] {i}%", end="")
        time.sleep(0.5)
print()
print("ERROR 404: WiFi not found")
time.sleep(0.5)
print("Retry wifi check? (y/n)")
wifi_retry = input()
if wifi_retry == "y" or wifi_retry == "Y":
    print("Retrying...")
    time.sleep(0.5)
    for i in range(0, 101, 10):
        blocks = i // 10
        print(f"\r[{'█' * blocks}{' ' * (10 - blocks)}] {i}%", end="")
        time.sleep(0.5)
    print()
    print("ERROR 404: WiFi not found")
    time.sleep(0.5)
else:
    print("Skipping WiFi check...")
    time.sleep(0.5)
print("Integrity check complete. You may now proceed to the main program.")
time.sleep(1)



attempts = 0

while attempts < 4:
    username = input("Username: ")
    password = input("Password: ")

    if username == "Hanz" and password == "1234":
        print()
        print("ACCESS GRANTED")
        break

    else:
        attempts += 1
        print(f"ACCESS DENIED - Attempts left: {4 - attempts}")

if attempts == 4:
    print("Too many failed attempts.")
    sys.exit()


def YT():
    print("https://www.youtube.com/@HanzFG.Official")

    while True:
        command = input("> ")

        if command.lower() == "desktop" or command.lower() == "dt":
            break

def heslo():
    print("""To bys chtěl vědět ty špínáku, že jo? Ale ne, to ti neřeknu!

<--dt""")

    while True:
        command = input("> ")

        if command.lower() == "desktop" or command.lower() == "dt":
            break

def neco():
    print("""=====-NĚCO-=====
<--dt""")

    while True:
        command = input("> ")
def BIOS():
    print("""=====-BIOS-=====
BIOS is not functional yet...
<--dt""")


    while True:
        command = input("> ")

        if command.lower() == "desktop" or command.lower() == "dt":
            break

while True:
    print()
    print("|=========================== HanzOS 2.0 ===========================|")
    print("|[1] YT                                                            |")
    print("|[2] Heslo                                                         |")
    print("|[3] Něco                                                          |")
    print("|[4] BIOS                                                          |")
    print("|[5] Vypnout                                                       |")
    print("|Pokud se budeš chtít vrátit na plochu, napiš 'desktop' nebo 'dt'. |")
    print("|==================================================================|")

    choice = input("> ")

    if choice == "1":
        YT()

    elif choice == "2":
        heslo()

    elif choice == "3":
        neco()
    elif choice == "4":
        BIOS()

    elif choice == "5":
        break