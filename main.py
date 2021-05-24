from bs4 import BeautifulSoup 
from openpyxl.workbook import Workbook
import sys
import pandas as pd 
import requests 

url = "https://quotes.toscrape.com"
next_url = "https://quotes.toscrape.com"
cnt = 0

quotes=[]        
authors=[]
tags=[]


try:

    while(True):

        soup = BeautifulSoup(requests.get(next_url).text, "html5lib")
        cnt+=1

        quotes_list = soup.find_all('div',class_= "quote")


        for quote in quotes_list:
            print("Quote: ",quote.span.text)
            print("Author: ",quote.span.next_sibling.next_sibling.small.text)
            tags_soup = quote.div.find_all('a')
            tag_list=[]
            for tag in tags_soup:
                tag_list.append(tag.text)
            print("Tags: ",tag_list)
        
            quotes.append(quote.span.text)
            authors.append(quote.span.next_sibling.next_sibling.small.text)
            tags.append(tag_list)






        print("Page ", cnt," scraped")
        next_page = soup.find('li', class_="next")
        next_url=url+next_page.a['href']
    


except :
    e = sys.exc_info()
    print(e)
    print("Next page not found. Scraping done")

    # print(len(tags))
    # print(tags)

    df = pd.DataFrame({
        "name":authors,
        "quote":quotes,
        "tags":tags
    })

    df.to_excel('quotes.xlsx')



