import os

# Define the command to execute
command_template = '.\\TOOLS\\Lucksystem\\LuckSystem.exe pak extract -i {} -o {} --all {}'
extracted_root = 'EXTRACTED\\'

# Function to traverse directories recursively
def process_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Form the input and output file paths
            input_file = os.path.join(root, file)
            # Execute the command
            extracted_des = os.path.join(extracted_root, os.path.splitext(file)[0])
            command = command_template.format(input_file, '_', extracted_des)
            print(command)
            os.system(command)

# Main function to start processing from the current directory
def main():
    current_directory = 'PAK'
    try:
        process_files(current_directory)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
