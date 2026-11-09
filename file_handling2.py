# load Unicode UTF-8 text file and return its content or None if fails.
# include comprehensive error handling for file operations and Unicode decoding errors.
def load_text_file(file_path):
    """
    Load the content of a text file and return it as a string.
    
    :param file_path: Path to the text file.
    :return: Content of the text file as a string, or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except UnicodeDecodeError:
        print(f"Error: Could not decode the file '{file_path}' using UTF-8 encoding.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading the file '{file_path}': {e}")
        return None

# save UTF-8 text file with comprehensive error handling for file operations and Unicode encoding errors.
# return True if successful, False otherwise.
def save_text_file(file_path, content):
    """
    Save a string to a text file.
    
    :param file_path: Path to the text file.
    :param content: String content to be saved to the file.
    :return: True if the file was saved successfully, False otherwise.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except UnicodeEncodeError:
        print(f"Error: Could not encode the content to UTF-8 for the file '{file_path}'.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while saving the file '{file_path}': {e}")
        return False

def main():
    # Example usage of the file handling functions
    text_file_path = 'example.txt'
    
    # Save content to a text file
    content_to_save = "Hello, this is a sample text file.\n同学们好\nصباح الخير"
    if save_text_file(text_file_path, content_to_save):
        print(f"Content successfully saved to '{text_file_path}'.")
    
    # Load content from the text file
    loaded_content = load_text_file("does_not_exist.txt")  # This will raise an error if the file does not exist
    #loaded_content = load_text_file(text_file_path)
    if loaded_content is not None:
        print("Loaded Content:", loaded_content)

if __name__ == "__main__":
    main()