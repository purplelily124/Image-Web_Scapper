import requests  
from bs4 import BeautifulSoup  
    
def getdata(url):  
    r = requests.get(url)  
    return r.text  
    
htmldata = getdata("https://www.geeksforgeeks.org/")  
soup = BeautifulSoup(htmldata, 'html.parser')  
ls = []
for item in soup.find_all('img'): 
    ls.append(item['src'])

import pandas as pd 
df = pd.DataFrame(ls,columns=["Links"])
df.to_csv("Links.csv",encoding='utf-8')
