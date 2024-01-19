def write_file(file_name, file_content):
    file_name = str(file_name) + ".txt"

    try:
        with open(file_name, "w") as file:
            file.write(file_content)
        print(f"File '{file_name}' has been successfully written.")
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")


def append_file(file_name, append_content):
    # Add the .txt file extension to the file_name
    file_name = str(file_name) + ".txt"

    try:
        # Open the file in append mode
        with open(file_name, "a") as file:
            # Append the content to the file
            file.write(append_content)
        print(f"Content has been successfully appended to file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def read_file(file_name):
    # Add the .txt file extension to the file_name
    file_name = str(file_name) + ".txt"

    try:
        # Open the file in read mode
        with open(file_name, "r") as file:
            # Read the content of the file
            file_content = file.read()
        return file_content
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None