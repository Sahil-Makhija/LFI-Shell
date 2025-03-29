from typing import Tuple, Dict, Optional


def parse_http_request(content: str) -> Tuple[str, str, Dict[str, str], Optional[str]]:
    """
    Parse an HTTP request from a file.

    Args:
        file_path (str): Path to the file containing the HTTP request

    Returns:
        Tuple[str, str, Dict[str, str], Optional[str]]: A tuple containing:
            - HTTP method
            - URL
            - Headers dictionary
            - Request body (None if no body present)

    Raises:
        ValueError: If the request format is invalid
        FileNotFoundError: If the file doesn't exist
    """
    try:

        # Split request into headers and body
        request_parts = content.split("\n\n", 1)
        header_lines = request_parts[0].splitlines()
        body = request_parts[1] if len(request_parts) > 1 else None

        # Parse request line
        if not header_lines:
            raise ValueError("Empty request")
            
        try:
            method, url, _ = header_lines[0].split()
        except ValueError:
            raise ValueError("Invalid request line format")

        # Parse headers
        headers = {}
        for line in header_lines[1:]:
            if not line:
                continue
            try:
                key, value = line.split(":", 1)
                headers[key.strip()] = value.strip()
            except ValueError:
                raise ValueError(f"Invalid header format: {line}")

        return method, url, headers, body

    except :
        print("Unable to parse HTTP request.")
