import sys
import time
import os
import pygame
import random
def anim():
    for i in range(10):
        for symbol in ["\\", "|", "/", "-"]:
            print(f"\rPlease wait {symbol}", end="")
            time.sleep(0.15)
def clear_screen():
    os.system("cls")

print("""Do you want to skip loading?
[1] Yes
[2] No""")
boot_up = input()
if boot_up == "2":
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
            time.sleep(0.5)
            print("ERROR 404: WiFi not found")
    else:
        print("Skipping WiFi check...")
        time.sleep(1)

print("Integrity check complete. You may now proceed to the main program.")
time.sleep(3)


pygame.mixer.init()
pygame.mixer.music.load("windows-7-startup.mp3")
pygame.mixer.music.play()

for i in range(7):
        for symbol in ["\\", "|", "/", "-"]:
            print(f"\rPlease wait {symbol}", end="")
            time.sleep(0.15)

print()

attempts = 0

while attempts < 4:
    username = input("Username: ")
    password = input("Password: ")

    if username == "Hanz" and password == "1234":
        print()
        print("ACCESS GRANTED ENTERING AS ADMIN")
        time.sleep(3)
        break
    elif username == "guest" and password == "guest":
        print()
        print("ACCESS GRANTED ENTERING AS GUEST")
        time.sleep(3)
        break

    else:
        attempts += 1
        print(f"ACCESS DENIED - Attempts left: {4 - attempts}")

if attempts == 4:
    print("Too many failed attempts.")
    sys.exit()

#------------------------------------------------------------------------------------------------
def YT():
    clear_screen()
    print("https://www.youtube.com/@HanzFG.Official")

    while True:
        command = input("> ")

        if command.lower() == "desktop" or command.lower() == "dt":
            break
        else:
            print("Invalid command. Please type 'desktop' or 'dt' to return to the desktop.")
#------------------------------------------------------------------------------------------------
def heslo():
    clear_screen()
    print("""To bys chtěl vědět ty špínáku, že jo? Ale ne, to ti neřeknu!

<--dt""")

    while True:
        command = input("> ")

        if command.lower() == "desktop" or command.lower() == "dt":
            break
        else:
            print("Invalid command. Please type 'desktop' or 'dt' to return to the desktop.")
#------------------------------------------------------------------------------------------------
def neco():
    clear_screen()
    print("""=====-NĚCO-=====
<--dt""")

    while True:
        command = input("> ")
        
        if command.lower() == "desktop" or command.lower() == "dt":
            break
        else:
            print("Invalid command. Please type 'desktop' or 'dt' to return to the desktop.")
#------------------------------------------------------------------------------------------------
def progress_bar():
    clear_screen()
    for i in range(0, 101, 10):
        blocks = i // 10
        print(f"\r[{'█' * blocks}{' ' * (10 - blocks)}] {i}%", end="")
        time.sleep(0.5)

    while True:
        command = input(" > ")

        if command.lower() == "desktop" or command.lower() == "dt":
            break
        else:
            print("Invalid command. Please type 'desktop' or 'dt' to return to the desktop.")
#------------------------------------------------------------------------------------------------
def rotation():
    clear_screen()
    for i in range(10):
        for symbol in ["\\", "|", "/", "-"]:
            print(f"\rBooting {symbol}", end="")
            time.sleep(0.15)

    while True:
        command = input(" > ")

        if command.lower() == "desktop" or command.lower() == "dt":
            break
        else:
            print("Invalid command. Please type 'desktop' or 'dt' to return to the desktop.")
#------------------------------------------------------------------------------------------------
def shut_down():
     clear_screen()
     for i in range(10):
             for symbol in ["\\", "|", "/", "-"]:
                print(f"\rShutting Down {symbol}", end="")
                time.sleep(0.15)
     print()
     print("Thank you for using our service..")
     time.sleep(4); sys.exit()
#------------------------------------------------------------------------------------------------
def pc_specs():
    clear_screen()
    print("CPU: Intel Core i7-9700K")
    print("GPU: NVIDIA GeForce RTX 2080 Ti")
    print("RAM: 32GB DDR4")
    print("Storage: 1TB NVMe SSD")
    print("Motherboard: ASUS ROG Maximus XI Hero")
    print("Power Supply: Corsair RM850x 850W")
    print("Cooling: NZXT Kraken X62 AIO Liquid Cooler")
    print("Operating System: Windows 10 Pro")

    while True:
        command = input("> ")

        if command.lower() == "desktop" or command.lower() == "dt":
            break
        else:
            print("Invalid command. Please type 'desktop' or 'dt' to return to the desktop.")
#------------------------------------------------------------------------------------------------
def guess_the_number():
    clear_screen()

    while True:
        number = random.randint(1, 100)
        attempts = 0

        while True:
            guess = int(input("Guess the number (1-100): "))
            attempts += 1

            if guess < number:
                print("Too low!")

            elif guess > number:
                print("Too high!")

            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        print("Do you want to play again? (y/n)")
        play_again_number = input(">")
        while play_again_number.lower() not in ["y", "n"]:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            play_again_number = input(">")
        if play_again_number.lower() == "n":
            print("Returning to the desktop...")
            time.sleep(2)
            anim()
            break
        elif play_again_number.lower() == "y":
            for i in range(0, 31, 10):
                blocks = i // 10
                print(f"\rRestarting game {'.' * blocks}{' ' * (10 - blocks)}", end="")
                time.sleep(0.5)

        
#------------------------------------------------------------------------------------------------
def coin_flip():
    clear_screen()
    print("Flipping a coin...")
    time.sleep(2)
    result = random.choice(["Heads", "Tails"])
    print(f"The result is: {result}")
    time.sleep(2)
    print("Automatically returning to the desktop...")
    time.sleep(2)
    anim()
#------------------------------------------------------------------------------------------------
def calculator():
    print()
    clear_screen()
    print("Welcome to the calculator")
    while True:
        print("""Choose an operation:
[+] Addition
[-] Subtraction
[*] Multiplication
[/] Division""")
        operation = input("> ")
        if operation == "+":
            print("You chose addition.")
        elif operation == "-":
            print("You chose subtraction.")
        elif operation == "*":
            print("You chose multiplication.")
        elif operation == "/":
            print("You chose division.")
        else:
            print("Invalid input. Please enter +, -, *, or /.")
            continue
        první_číslo = int(input("Enter the first number: "))
        druhé_číslo = int(input("Enter the second number: "))
        if operation == "+":
            výsledek = první_číslo + druhé_číslo
        elif operation == "-":
            výsledek = první_číslo - druhé_číslo
        elif operation == "*":
            výsledek = první_číslo * druhé_číslo
        elif operation == "/":
            výsledek = první_číslo / druhé_číslo
        print(f"The result of {první_číslo} {operation} {druhé_číslo} is {výsledek}")
        print("Do you want to perform another calculation? (y/n)")
        odpověď = input("> ")
        if odpověď.lower() == "y":
            print("Restarting the calculator...")
            time.sleep(1)
            clear_screen()
            continue
        else:
            print("Exiting the calculator...")
        time.sleep(1)
        break
#------------------------------------------------------------------------------------------------
while True:
    print()
    clear_screen()
    print("|=========================== HanzOS 2.1 ===========================|")
    print("|[1] YT                                                            |")
    print("|[2] Password                                                      |")
    print("|[3] Something                                                     |")
    print("|[4] Computer Specifications                                       |")
    print("|[5] Calculator                                                    |")
    print("|------------------------ Loading Preview -------------------------|")
    print("|[6] Progress Bar                                                  |")
    print("|[7] Rotation                                                      |")
    print("|----------------------------- Games ------------------------------|")
    print("|[8] Guess The Number                                              |")
    print("|[9] Coin Flip                                                     |")
    print("|[10] Shut Down                                                    |")
    print("|If you want to return to the desktop, type 'desktop' or 'dt'.     |")
    print("|==================================================================|")

    choice = input("-> ")

    if choice == "1":
        YT()
    elif choice == "2":
        heslo()
    elif choice == "3":
        neco()
    elif choice == "4":
        pc_specs()
    elif choice == "5":
        calculator()
    elif choice == "6":
        progress_bar()
    elif choice == "7":
        rotation()
    elif choice == "8":
        guess_the_number()
    elif choice == "9":
        coin_flip()
    elif choice == "10":
        shut_down()
    elif choice.lower() == "":
        if username == "Hanz" and password == "1234":
            print("welcome back, Hanz. You are logged in as admin. What do you need?")
            time.sleep(8)
        else:
            print("Invalid command. Please type the folowing numbers on the desktop.")
            time.sleep(4)
            continue
    else:
        print("Invalid command. Please type the folowing numbers on the desktop.")
        time.sleep(4)
        continue
