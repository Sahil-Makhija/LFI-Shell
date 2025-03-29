def find_between_markers(text: str) -> tuple[int, int] | None:
    """
    Finds the start and end indices of the substring between two ^^ markers.
    If mode is FILE, opens the file specified by text and searches within its contents.
    If mode is URL, searches directly within the provided text string.

    Args:
        text: The input string to search within, or a file path if mode is FILE.
        mode: "FILE" to read from a file, "URL" to search directly in text (default: "URL").

    Returns:
        A tuple containing the start index (inclusive) and end index (exclusive)
        of the substring between the first pair of ^^ markers.
        Returns None if two markers are not found or if file reading fails.
    """
    content = text # Default to using the input text directly

    # If mode is FILE, read the content from the file
    # if mode == "FILE":
    #     try:
    #         with open(text, "r") as f:
    #             content = f.read() # Update content with file data
    #     except FileNotFoundError:
    #         print(f"Error: File not found: {text}")
    #         return None
    #     except Exception as e:
    #         print(f"Error reading file: {e}")
    #         return None

    marker = "^^"
    marker_len = len(marker)

    # Find the first occurrence of the marker in the correct content
    first_pos = content.find(marker) # Use 'content' variable
    if first_pos == -1:
        return None  # First marker not found

    # Calculate the start index of the content (right after the first marker)
    start_index = first_pos + marker_len

    # Find the second occurrence of the marker, starting the search *after* the first one
    second_pos = content.find(marker, start_index) # Use 'content' variable
    if second_pos == -1:
        return None  # Second marker not found

    # The end index of the content is the position where the second marker starts
    end_index = second_pos

    return (start_index, end_index)


def find_injection_point(body=None, url=None, headers=None):
    """
    Check for injection markers (^^) in the request body, URL, and headers.
    
    Args:
        body (str): The request body
        url (str): The request URL
        headers (dict): Dictionary of request headers
        
    Returns:
        tuple: (injection_found, location, markers)
            - injection_found (bool): True if injection point was found
            - location (str): 'body', 'url', or 'headers'
            - markers: For body/url: (start, end) positions
                       For headers: (header_name, header_value, start, end)
    """
    # Check body first
    if body:
        body_markers = find_between_markers(body)
        if body_markers:
            return True, "body", body_markers
    
    # Check URL if no injection found in body
    url_markers = find_between_markers(url)
    if url_markers:
        return True, "url", url_markers
    
    # Check headers if no injection found in body or URL
    for header_name, header_value in headers.items():
        header_markers = find_between_markers(header_value)
        if header_markers:
            start, end = header_markers
            return True, "headers", (header_name, header_value, start, end)
    
    # No injection point found
    return False, None, None

# Example Usage (optional, can be removed or kept for testing)
if __name__ == '__main__':
    test_string1 = "Some text ^^here^^ more text"
    indices1 = find_between_markers(test_string1)
    if indices1:
        start, end = indices1
        print(f"String 1: '{test_string1}'")
        print(f"Indices: {indices1}")
        print(f"Content: '{test_string1[start:end]}'") # Output: 'here'
    else:
        print(f"Markers not found in '{test_string1}'")

    print("-" * 20)

    test_string2 = "No markers here"
    indices2 = find_between_markers(test_string2)
    if indices2:
        start, end = indices2
        print(f"String 2: '{test_string2}'")
        print(f"Indices: {indices2}")
        print(f"Content: '{test_string2[start:end]}'")
    else:
        print(f"Markers not found in '{test_string2}'") # Output: Markers not found...

    print("-" * 20)

    test_string3 = "Only one ^^ marker"
    indices3 = find_between_markers(test_string3)
    if indices3:
         start, end = indices3
         print(f"String 3: '{test_string3}'")
         print(f"Indices: {indices3}")
         print(f"Content: '{test_string3[start:end]}'")
    else:
        print(f"Markers not found in '{test_string3}'") # Output: Markers not found...

    print("-" * 20)

    test_string4 = "Empty between ^^ ^^ markers"
    indices4 = find_between_markers(test_string4)
    if indices4:
         start, end = indices4
         print(f"String 4: '{test_string4}'")
         print(f"Indices: {indices4}") # Output: (15, 15)
         print(f"Content: '{test_string4[start:end]}'") # Output: ''
    else:
        print(f"Markers not found in '{test_string4}'")
