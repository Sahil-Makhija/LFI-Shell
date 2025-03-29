def get_file_content(filepath:str):
    try:
        with open(filepath, "r") as f:
            content = f.read() # Update content with file data
            return content
    except FileNotFoundError:
            print(f"Error: File not found: {filepath}")
            return None
    except Exception as e:
            print(f"Error reading file: {e}")
            return None
    
def replace_range(original: str, replacement: str, start: int, end: int) -> str:
    """
    Replace characters in a string from start index to end index with replacement string.
    
    Args:
        original (str): Original string
        replacement (str): String to replace with
        start (int): Starting index (inclusive)
        end (int): Ending index (exclusive)
    
    Returns:
        str: New string with replaced characters
    """
    # Method 1: Using string slicing
    return original[:start-2] + replacement + original[end+2:]