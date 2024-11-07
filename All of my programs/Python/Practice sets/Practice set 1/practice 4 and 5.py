import os

def list_directory_contents(directory_path):
     try:
        # List all items in the directory
        contents = os.listdir(directory_path)
        print(f"Contents of '{directory_path}':")
        for item in contents:
            print(item)
     except FileNotFoundError:
        print(f"The directory '{directory_path}' was not found.")
     except NotADirectoryError:
        print(f"The path '{directory_path}' is not a directory.")
     except PermissionError:
        print(f"Permission denied to access '{directory_path}'.")
while True:
    directory_path = input("\nEnter the directory path (or type 'exit' to quit): ")
    if directory_path.lower() == 'exit':
         print("Exiting program.")
         break
    list_directory_contents(directory_path)