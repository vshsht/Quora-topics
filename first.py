import requests
from bs4 import BeautifulSoup
import urllib.request

def main_crawler(url):
    source=requests.get(url)
    source=source.text

    soup=BeautifulSoup(source,"html.parser")
    for links in soup.findAll('a',{'class':'question_link'}):
        link=links.get('href')
        if(link[0]=='/'):
            link='https://www.quora.com'+str(link)

        title=links.string
        print('Q ',title)
        print(link)
        print('\n')


def input_quora():
    str1=input();
    s=list(str(str1))
    for i in range(0,len(str1)):
        if s[i]==' ':
            s[i]='-'

    str1=''.join(s)
    str1='https://www.quora.com/'+str(str1)
    source_t=requests.get(str1)
    source_t=source_t.text
    soup2=BeautifulSoup(source_t,"html.parser")
    i=0
    for stuff in soup2.findAll('a',{'class':'question_link'}):
        url=stuff.get('href')
        i=1
        if i==1:
            break

    url='https://www.quora.com'+url
    main_crawler(url)

input_quora()
