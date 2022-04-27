"""
This script is written to extract the information from the site of WHO
"""
import requests as rq
from bs4 import BeautifulSoup as bc

letter = 'N'
url = 'https://web.archive.org/web/20201201053628/https://www.who.int/health-topics'
r = rq.get(url)
# print(r.content)
soup = bc(r.content, 'lxml')
# print(soup.prettify())
elements = soup.find(id='PageContent_C002_Col00')
sibs = elements.findAll('a')
data = []
links = []
result = []
links_2 = []
links_3 = []
for sib in sibs:
    if len(sib.text.strip()) <= 3:
        continue
    else:
        data.append(sib.text)
        links.append(sib['href'])
print(data)
for da in data:
    if da.startswith(letter):
        print(da)
        result.append(da)
"""
if you want to access the details of all the pages uncomment the section below
"""
# count = 0
# for link in links:
#     if not link.index("/web/20201201053628/"):
#         links_2.append(link[20:])
#     elif link.index("/web/20201201053628/"):
#         links_3.append(link)
#
# links_2.extend(links_3)
# print(links_2, len(links_2))
#
# for li in links_2:
#     page = rq.get(li)
#     print(page)
#     soup = bc(page.content, 'lxml')

