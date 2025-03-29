import sys
from cmd import Cmd

from utils.args_parser import parse_arguments
from utils.check_injection import find_injection_point,find_between_markers
from utils.get_file import get_file

from utils.misc import get_file_content


class Term(Cmd):
    prompt="LFI Shell > "

    METHOD="GET"
    MODE="FILE"

    URL=None
    FILE_CONTENT=None

    # injection_found=False
    # injection_in=None
    start_index=0
    end_index=0

    def __init__(self):
        super().__init__()
        self.args = parse_arguments()

        if self.args.url:
            self.handle_url()
        elif self.args.request:
            self.handle_request()
        else:
            print("Error: No URL or Request file was given.")
            sys.exit(1)

    def handle_url(self):
        injection_found , _ , (s,e) = find_injection_point(url=self.args.url)
        if injection_found:
            self.MODE="URL"
            self.URL=self.args.url

            # self.injection_found=True
            # self.injection_in=injection_in
            
            self.start_index=s
            self.end_index=e

            if self.args.method:
                self.METHOD=self.args.method
            return
        else:
            print('Error: No Injection Markers were found in URL!')
            sys.exit(1)
    
    def handle_request(self):
        self.MODE="FILE"
        file_content=get_file_content(self.args.request)
        if file_content:
            markers = find_between_markers(file_content)
            if markers:
                self.FILE_CONTENT=file_content
                self.start_index=markers[0]
                self.end_index=markers[1]
                return
            else:
                print("Error: No injection point found.")
                sys.exit(1)
        else:
            print("Error: Request file not found.")
            sys.exit(1)

    def do_exit(self):
        return 1 # return and exit
    
    def do_EOF(self):
        print()
        return 1 # return and exit
    
    def default(self, file: str) -> None:
        if self.MODE=="FILE":
            get_file(content=self.FILE_CONTENT,filename=file,start_index=self.start_index,end_index=self.end_index,mode=self.MODE)
            return
        elif self.MODE=="URL":
            get_file(content=self.URL,filename=file,start_index=self.start_index,end_index=self.end_index,mode=self.MODE,method=self.METHOD)
            return
        else:
            return

    
