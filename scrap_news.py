import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://inshorts.com/en/read'
req_obj = requests.get(url)
dom_text = req_obj.text
soup = BeautifulSoup(dom_text, "html.parser")
news_title = soup.find_all("span", attrs={"itemprop": "headline"})
print(news_title)
test=[]
for news in news_title:
    print((news.text.strip()))
    test.append(news.text.strip())
# body = soup.find("div", attrs={"class": "container"})
# for entry in body:
#     news_title = entry.find("span", attrs={"itemprop": "headline"})
#     print(news_title)
df_test=pd.DataFrame()
df_test['news_title']=test
df_test.to_csv('test.csv')
print("-----------------------------------------------")

url2 = 'https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en'
req_obj2 = requests.get(url2)
dom_text2 = req_obj2.text
soup2 = BeautifulSoup(dom_text2, "html.parser")
news_title_google = soup2.find_all("a", attrs={"class": "DY5T1d"})
print(news_title_google)
train=[]
for news_go in news_title_google:
    print((news_go.text.strip()))
    train.append(news_go.text.strip())

df_train=pd.DataFrame()
df_train['news_title']=train
df_train.to_csv('train.csv')