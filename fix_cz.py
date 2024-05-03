import struct
import os

def check_header(file):
    file.seek(1)
    data = file.read(2)
    header = struct.unpack('<BB', data)
    print(header)
    if header == (90,49) or header == (90,51) or header == (90,52): #cz1, cz3 or cz4
        return True
    return False

def write_byte(file):
    file.seek(14)
    file.write(struct.pack('<B', 3))
    file.flush()

def main():
    for root, dirs, files in os.walk("EXTRACTED\\CZ"):
        for cz_file in files:

            cz_file = os.path.join(root, cz_file)

            with open(cz_file, 'r+b') as file:
                check = check_header(file)
                if check:
                    write_byte(file)
                    print("Modified ", cz_file)

if __name__ == '__main__':
    main()