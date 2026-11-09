def load_text_file(file_path):
    """
    Load the content of a text file and return it as a string.
    
    :param file_path: Path to the text file.
    :return: Content of the text file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_text_file(file_path, content):
    """
    Save a string to a text file.
    
    :param file_path: Path to the text file.
    :param content: String content to be saved to the file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content) 

def main():
    # Example usage of the file handling functions
    text_file_path = 'example.txt'
    
    # Save content to a text file
    content_to_save = "Hello, this is a sample text file.\n同学们好\nصباح الخير"
    save_text_file(text_file_path, content_to_save)
    
    # Load content from the text file
    loaded_content = load_text_file("mira.avif")  # This will raise an error if the file does not exist
    print("Loaded Content:", loaded_content)    

if __name__ == "__main__":
    main()