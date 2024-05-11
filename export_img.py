import os
import time
import struct
# Define the command to execute
command_luck = '.\\TOOLS\\Lucksystem\\LuckSystem.exe image export -i {} -o {}.png'
command_luca = '.\\TOOLS\\LucaSystem\\lucasystemtools.exe -t cz4 -m export -f {} -o '
extracted_root = 'EXTRACTED\\IMG'

def check_lucksystem(file_path):
    with open(file_path, 'r+b') as file:
        file.seek(1)
        data = file.read(2)
        header = struct.unpack('<BB', data)
        if header == (90,48):          #cz0
            return 0
        if header == (90,49):          #cz1
            return 1
        elif header == (90,50):        #cz2
            return 2
        elif header == (90,51):        #cz3
            return 3
        return -1                      #cz4

# Function to traverse directories recursively
def process_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "" or 1:    
                # Form the input and output file paths
                input_file = os.path.join(root, file)
                # Get the parent folder of the current file
                parent_folder = os.path.basename(os.path.dirname(input_file))
            
                # Form the output file path
                output_folder = os.path.join(extracted_root, parent_folder)
                output_file = output_folder + '\\' + str(file)
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                    print(f"Folder '{output_folder}' created.")
                # Execute the command
                cz = check_lucksystem(input_file)
                if cz >= 0:
                    command = command_luck.format(input_file, output_file)
                    print("==== {} =====".format(input_file))
                    os.system(command)
                else:
                    command = command_luca.format(input_file)
                    print("==== {} =====".format(input_file))
                    os.system(command)
                    os.replace(input_file,output_file)
                time.sleep(0.05)
                

# Main function to start processing from the current directory
def main():
    for root, dirs, files in os.walk("EXTRACTED\\CZ"):
        for dir in dirs: 
                try:
                    process_files(os.path.join(root, dir))
                except Exception as e:
                    print(e)
if __name__ == "__main__":
    main()
