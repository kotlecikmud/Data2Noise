import wave, os


# Function for encoding binary file
def encode_data(file_data):
    encoded_data = bytearray()
    for byte in file_data:
        encoded_data.extend([byte >> 4, byte & 0xF])
    return encoded_data


# Function for decoding sound data
def decode_data(data):
    decoded_data = bytearray()
    for i in range(0, len(data), 2):
        byte = (data[i] << 4) | data[i + 1]
        decoded_data.append(byte)
    return decoded_data


# Function for saving sound data to a WAV file
def save_as_wav(filename, data, sample_rate=44100):
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit (2 bytes)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(data)


# Function for reading sound data from a WAV file
def read_wav_data(filename):
    with wave.open(filename, 'rb') as wav_file:
        sample_width = wav_file.getsampwidth()
        data = wav_file.readframes(wav_file.getnframes())
    return data, sample_width


# Function for encoding a file and saving it as a WAV sound file
def encode_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encoded_data = encode_data(file_data)
    wav_filename = f"{file_path}.wav"
    save_as_wav(wav_filename, encoded_data)
    print(f"The encoded sound has been saved to the file: {wav_filename}")


# Function for decoding sound data from a WAV file and saving it as a binary file
def decode_file(file_path):
    wav_data, sample_width = read_wav_data(file_path)
    if sample_width == 2:  # 16-bit
        decoded_data = decode_data(wav_data)
        original_filename = file_path.rsplit(".", 1)[0]
        with open(original_filename, 'wb') as file:
            file.write(decoded_data)
        print(f"The decoded file has been saved as: {original_filename}")
    else:
        print("Unsupported WAV file format. Supported format is 16-bit PCM.")


# Main loop
while True:
    choice = input("data2noise\
        \n1) Encode to noise\
        \n2) Encode from noise\
        \n3) Exit\
        \n>>> ")

    os.system('cls' if os.name == 'nt' else 'clear')

    if choice == '1':
        file_path = input("Enter the path to the file to encode: ")
        encode_file(file_path)
    elif choice == '2':
        file_path = input("Enter the path to the WAV file to decode: ")
        decode_file(file_path)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
