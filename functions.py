import requests
from bs4 import BeautifulSoup as bs
import os

def search_google(keyword:str):
    keyword=keyword.replace(" ","")
    url=f"https://www.google.com/search?q={keyword}&sxsrf=APwXEdeh3xLJCJb7vT3pQqunpknH9V3QZw:1685417438791&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi90PKdjZz_AhWsmlYBHaRWAgsQ_AUoAXoECAEQAw&biw=1488&bih=778&dpr=1.25"
    response=requests.get(url)
    response=response.content
    response=bs(response,features='lxml')
    return response

def get_img_url(response:bs)->list:
    img=response.find_all("img")
    del img[0]
    img_urls=[img[i]['src'] for i in range(len(img))]
    return img_urls

def get_img(img_url:list)->list:
    images=[]
    for url in img_url:
        img=requests.get(url).content
        images.append(img)
    return images

def get_data(keyword:str):
    response=search_google(keyword)
    keyword=keyword.replace(" ","_")
    img_urls=get_img_url(response)
    images=get_img(img_urls)
    try:
        os.system('powershell.exe  rmdir -r ./static/images -Force')
    except:
        pass
    if not os.path.exists("./static/images"):
        os.mkdir("./static/images")
    for i in range(len(images)):
        f=open("./static/images/{}_{}.jpeg".format(keyword,i),'wb')
        f.write(images[i])
        f.close()

# l=os.listdir("./static/images")
# print(l)