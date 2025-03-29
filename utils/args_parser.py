import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Chain multiple requests or start with a single one.")

    parser.add_argument("-r", "--request", type=str, help="Specify LFI request file")
    parser.add_argument("-u", "--url", type=str, help="Specify LFI in URL")

    parser.add_argument(
        "-c", "--chain", type=str, action="append",
        help="Specify up to 5 config files (use -c file1 -c file2 ...)"
    )


    # Request Args
    parser.add_argument(
        "-X", "--method", type=str, default="GET",
        help="Specify HTTP request method (default: GET)"
    )
    parser.add_argument(
        "-H", "--header", type=str, action="append",
        help="Specify HTTP request headers (can be used multiple times)"
    )
    return parser.parse_args()
