from cryptography_functions import functions as crypto
from colorama import Fore
from ui import menu_msg as msg
from time import sleep

import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()


def menu():
    """Funcion menu"""
    clearConsole()
    registro_keys = []
    registro_cipher = []
    validador = False
    option = 0
    msg.msg()
    sleep(2)
    clearConsole()
    while (option!=4):
        msg.crypto_menu()
        try:
            option = int(input("Digite una opcion: "))
        except:
            print("Digita una opcion valida!")

        if (option==1):
            mensaje = input("Digite el mensaje que quiere encriptar: ")
            key_program = crypto.key(mensaje)
            registro_keys.append(key_program) #se registra la llave.
            cipher_text = crypto.encrypt(key_program,mensaje)
            registro_cipher.append(cipher_text)
            print("")
            print(f"{Fore.GREEN}Your encrypt message is: {cipher_text}")
            print("")
            validador = True
        elif(option==2):
            if (validador==False):
                print("")
                print("Necesitas primero cifrar un mensaje.")
                print("")
            else:
                mensaje_decrypt = crypto.decrypt(key_program, cipher_text)
                print("")
                print(f"{Fore.GREEN}Your decrypt message is: {mensaje_decrypt}")
                print("")
        elif(option==3):
            print()
            print(f"{Fore.GREEN}Resgiter keys: \n {registro_keys}")
            print()
            print(f"{Fore.GREEN}Encrypted messages:: \n {registro_cipher}")
            print()

