# Data2Noise

Data2Noise is a simple program written in Python that allows you to encode binary files into sound data and decode them back to binary files. The encoded data is saved as a WAV sound file, which can be played or shared like any other audio file.

## Requirements

- Python 3.x
- wave (Python standard library)

## Usage

1. Run the program by executing the Python script.
```
python data2noise.py
```
2. Choose an option by entering the corresponding number:

- `1) Encode to noise`: Allows you to encode a binary file into sound data.
- `2) Encode from noise`: Allows you to decode sound data from a WAV file and save it as a binary file.
- `3) Exit`: Exits the program.

3. If you choose option `1) Encode to noise`:

- Enter the path to the file you want to encode when prompted.
- The program will encode the file and save the encoded sound as a WAV file with the same name as the original file but with the `.wav` extension.
- The path to the encoded sound file will be displayed.

4. If you choose option `2) Encode from noise`:

- Enter the path to the WAV file you want to decode when prompted.
- The program will decode the sound data from the WAV file and save it as a binary file with the same name as the original file (before encoding).
- The path to the decoded file will be displayed.

5. Repeat steps 3-5 as needed.

## Limitations

- The program supports 16-bit PCM WAV files. Other formats are not supported.
- The program assumes mono sound data (single channel) with a sample rate of 44100 Hz and 16-bit sample width.
- Ensure that the binary files you encode and the WAV files you decode have compatible formats to avoid issues.

Feel free to use, modify, and distribute this program.
"# Data2Noise" 
