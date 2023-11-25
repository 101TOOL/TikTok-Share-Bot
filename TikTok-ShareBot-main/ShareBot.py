import requests; import threading; from pystyle import Colorate, Colors, Write, Add, Center; import os 
banner1 = '''
                                                                                           
    88     ,a8888a,         88  888888888888    ,ad8888ba,      ,ad8888ba,    88           
  ,d88   ,8P"'  `"Y8,     ,d88       88        d8"'    `"8b    d8"'    `"8b   88           
888888  ,8P        Y8,  888888       88       d8'        `8b  d8'        `8b  88           
    88  88          88      88       88       88          88  88          88  88           
    88  88          88      88       88       88          88  88          88  88           
    88  `8b        d8'      88       88       Y8,        ,8P  Y8,        ,8P  88           
    88   `8ba,  ,ad8'       88       88        Y8a.    .a8P    Y8a.    .a8P   88           
    88     "Y8888P"         88       88         `"Y8888Y"'      `"Y8888Y"'    88888888888    
'''
text = "Welcome to 101TOOL/Sharebot"
print(Colorate.Horizontal(Colors.blue_to_purple, Add.Add(banner1, text, 4)))
from pystyle import Box
print(Box.Lines("Please insert Please enter the information requested"))
VideoURI     = str(Write.Input("Video ID > ", Colors.blue_to_purple, interval=0.0001))
amount       = int(Write.Input("Amount (0=inf) > ", Colors.blue_to_purple, interval=0.0001))
sendType     = int(Write.Input("[1] - Launch > ", Colors.blue_to_purple, interval=0.0001)); 
view_bot = sendType=0
share_bot = sendType=1
share_amount = 0
daemon = True
while share_bot == 1:
    share_amount = share_amount+1
    print(Colorate.Horizontal(Colors.blue_to_purple, "[+] Sending shares on " + str(VideoURI) + ", amount of shares : [" + str(share_amount) + "]"))
    os.system("title Sent [" + str(share_amount) + "] shares")
else: 
    print('| Error |')
request = 'request(url),loop'
loop = 'url&share&+1&'
