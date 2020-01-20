from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# URl to web scrap from.
page_url = "https://s5.sir.sportradar.com/betradarvg/en/1/season/1746902/standings"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product from the store page
containers = page_soup.findAll("div", {"class": "panel margin-bottom"})

# name the output file to write to local disk
out_filename = "standings.csv"
# header of csv file to be written
headers = "pos,team,P,W,D,L,GF,GA,DIFF,PTS"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)

for container in containers:
    content = container.table.select("tbody")

    f.write(content)


f.close()
