"""
---ABOUT---

Tool for encoding/decoding files to/from noise harmonics WAV file.

Script Name: data2noise.py
Author: Filip Pawłowski 2024
Contact: filippawlowski2012@gmail.com
"""

__version__ = "00.01.02.01"

import os
import time
import wave
import threading
from datetime import datetime as dt


class LoadingAnimation:
    def __init__(self):
        self.animation_signs = ['|', '/', '-', '\\']
        self.sign_index = 0
        self.finished = False

    def start(self):
        self.finished = False
        threading.Thread(target=self._animate).start()

    def stop(self):
        self.finished = True

    def _animate(self):
        while not self.finished:
            print('- ' + self.animation_signs[self.sign_index % len(self.animation_signs)] + ' -', end='\r')
            time.sleep(0.1)
            self.sign_index += 1


# Instantiate LoadingAnimation class
loading_animation = LoadingAnimation()

LOG_F_NAME = ".log"


def cls_():
    os.system('cls' if os.name == 'nt' else 'clear')


def log_event(entry):
    current_time = dt.now()
    print(f"{current_time} || {entry}")
    with open(f"{LOG_F_NAME}", 'a') as f:
        f.write(f"\n[{current_time}]|{entry}")


# Function for encoding binary file
def encode_data(file_data):
    log_event("encoding data...")
    loading_animation.start()

    encoded_data = bytearray()
    for byte in file_data:
        encoded_data.extend([byte >> 4, byte & 0xF])

    loading_animation.stop()
    input("DONE >>>")

    return encoded_data


# Function for decoding sound data
def decode_data(data):
    log_event("decoding data...")
    loading_animation.start()

    decoded_data = bytearray()
    for i in range(0, len(data), 2):
        byte = (data[i] << 4) | data[i + 1]
        decoded_data.append(byte)

    loading_animation.stop()
    input("DONE >>>")

    return decoded_data


# Function for saving sound data to a WAV file
def save_as_wav(filename, data, sample_rate=44100):
    log_event("saving WAV file...")
    loading_animation.start()

    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit (2 bytes)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(data)

    loading_animation.stop()
    input("DONE >>>")


# Function for reading sound data from a WAV file
def read_wav_data(filename):
    log_event("reading WAV file...")
    loading_animation.start()

    with wave.open(filename, 'rb') as wav_file:
        sample_width = wav_file.getsampwidth()
        data = wav_file.readframes(wav_file.getnframes())

    loading_animation.stop()
    input("DONE >>>")

    return data, sample_width


# Function for encoding a file and saving it as a WAV sound file
def encode_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encoded_data = encode_data(file_data)
    wav_filename = f"{file_path}.wav"
    save_as_wav(wav_filename, encoded_data)
    log_event(f"The encoded file saved --> {wav_filename}")


# Function for decoding sound data from a WAV file and saving it as a binary file
def decode_file(file_path):
    wav_data, sample_width = read_wav_data(file_path)
    if sample_width == 2:  # 1 is 8-bit, 2 is 16-bit
        decoded_data = decode_data(wav_data)
        original_filename = file_path.rsplit(".", 1)[0]
        with open(original_filename, 'wb') as file:
            file.write(decoded_data)
        log_event(f"Decoded file saved --> {original_filename}")
    else:
        log_event("Unsupported WAV file format. Supported format is 16-bit PCM.")


if __name__ == '__main__':
    log_event(f"START v{__version__}")

    while True:
        cls_()

        choice = input(f"Data2Noise v{__version__}\
        \n1) Encode\
        \n2) Decode\
        \n3) Exit\
        \n>>> ")

        if choice == '1':
            file_path = input("Enter the path to the file to encode: ")
            encode_file(file_path)
        elif choice == '2':
            file_path = input("Enter the path to the WAV file to decode: ")
            decode_file(file_path)
        elif choice == '3':
            break
        else:
            log_event("Invalid choice. Please try again.")
            time.sleep(.5)
