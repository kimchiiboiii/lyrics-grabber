from urllib.request import Request, urlopen
from bs4 import BeautifulSoup




def grabData(url):
    disguisedReq = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data = urlopen(disguisedReq).read()
    return data


htmldata = grabData("https://songmeanings.com/songs/view/3530822107858787765/")
soup = BeautifulSoup(htmldata, "html.parser")
rawHtml = soup.get_text()

for stringStrip in soup.stripped_strings:
    if len(stringStrip) > 60:
        pass
    elif len(stringStrip) < 8:
        pass
    else:
        print(repr(stringStrip))