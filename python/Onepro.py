import requests
from bs4 import BeautifulSoup
import os
import time

def nums(num):
    try:
        url='http://wufazhuce.com/one/'
        url=url+str(num)
        sum=0
        k=requests.get(url).content
        k=BeautifulSoup(k,'html.parser')
        for i in k.find_all('img'):
            sum +=1
            if(sum==2):
                i=i.get('src')
        text1=k.select('div[class="one-cita"]')
        text=text1[0].get_text()
        text=text.lstrip()

        string1='E:\\OnePro\\'+str(num-15)
        if not os.path.exists(string1):
            os.makedirs(string1)
        else:
            return 1
        html1=requests.get(i)
        img=html1.content

        txt=string1+'\\'+str(num-15)+'.txt'
        imgname=string1+'\\'+str(num-15)+'.jpg'
        with open(imgname,'wb') as f:
            f.write(img)
            f.close()
        with open(txt,'a+') as l:
            l.write(text)
            l.close()
        return 1
    except:
        return 1



def xunhuan():
    k=1
    num=15
    while(k==1):
        k=nums(num)
        num +=1
        print(num-15,'\n')
        time.sleep(0.1)



if __name__ == '__main__':
    xunhuan()
