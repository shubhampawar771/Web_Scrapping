import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.in/Test-Exclusive_2020_1180-Multi-3GB-Storage/dp/B089MT34QL/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
r = requests.get(url, headers=headers)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup)
# print(soup.prettify)

title = soup.select("#productTitle")[0].get_text().strip()
print(title)


# title = soup.title
#print(title)
#print(type(title))
#print(type(title.string))

paras = soup.find_all('p')
#print(paras)

anchors = soup.find_all('a')
#print(anchors)

#print(soup.find('p').get_text())

#print(soup.get_text())

#for all links on page
#for link in anchors:
#   print(link.get('href'))

#for a in soup.findAll('a',href=True):
 #   price=a.find('div', attrs={'class':'a-size-medium a-color-price priceBlockDealPriceString'})
  #  print(price)

