import requests
from bs4 import BeautifulSoup
while True:

    url = input('Write The Name Of The WebSite You Want To Scrap (q to quit) :')

    if ('.com' not in url):
        print('write the Correct domain name')

    if url == '.com' or len(url) > 63:
        print('Refine Your Query')
    if (url == 'q'):
        print('Thanks For Your Using !!!')
        exit()

    if 'http://' not in url:
        try:
         print('Also Write http:// In The Starting')
        except:
            print('Put An http:// In The Starting')
    if 'http://' in url:
        context = requests.get(url)   
        r = requests.get(url)
        html = r.content
        # print(html) 
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.prettify)

            
           


