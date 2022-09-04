import requests as re
from bs4 import BeautifulSoup
from loader import db



async def getURL(url: str):
    
    session=re.session()
    cookie=session.cookies
    result=session.get(url)
    soop=BeautifulSoup(result.content,"html.parser")
    tags=soop.find_all("a",href=True)

    for tag in tags:
        await db.add_Updates(title=tag.text.strip(),link=tag['href'])
        





if __name__=='__main__':
    pass