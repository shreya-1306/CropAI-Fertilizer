import requests
from bs4 import BeautifulSoup
import sys
file1 = open("links.txt","a")
links = []
count = 0
def search(url):
  source_code = requests.get(url)
  plain_text=source_code.text
  soup = BeautifulSoup(plain_text)
  info=[]
  for link in soup.findAll('td'):
    info.append(link.text)
  print(info)
  if "Arti Jayesh Bagadia " in info:
  	links.append(url)
  	file1.write(url+"\n")
  	print(url)
  	count = 1
  for j in info:
	  if "Arti Jayesh Bagadia" in j:
	  	links.append(url)


for i in range(3000,3339):
	url = "https://navkarpariwar.com/nawkar-certificate/view-users.php?page="+str(i)
	print(url)
	search(url)
	if count == 1:
		break
	# if i > 1000:
	# 	break
	# break

print(links)

for x in links:
	file1.write(x+"\n") 
# file1.writelines(L) 
file1.close()
