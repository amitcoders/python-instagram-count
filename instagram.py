import requests
from bs4 import BeautifulSoup

def scrap(user):

    url="https://www.instagram.com/{}".format(user)

    r=requests.get(url)
    bs=BeautifulSoup(r.text,"html.parser")

    rep=bs.find("meta",property="og:description").attrs["content"]

    return rep

#now lets create our main function to see results

if __name__ == "__main__":
    user=input("user name \t")
    print(scrap(user))