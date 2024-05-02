import os

# Define the command to execute
command_template = 'luck image export -i {} -o {}.png'

# Function to traverse directories recursively
def process_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
                # Form the input and output file paths
                input_file = os.path.join(root, file)
                output_file = os.path.join(root, os.path.splitext(file)[0])
                # Execute the command
                command = command_template.format(input_file, output_file)
                print(command)
                os.system(command)
                

# Main function to start processing from the current directory
def main():
    current_directory = 'HAR/syscg/cz'
    try:
        process_files(current_directory)
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()
