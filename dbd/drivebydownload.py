import requests
from bs4 import BeautifulSoup

url = "http://example-vulnerable-app.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# Find the links
links = soup.find_all('a')
def downloadcheck():  
    for link in links:
        href = link.get('href')
        if href and href.endswith(('.exe', '.zip', '.msi', '.dmg', '.pkg')):
            print(f"Drive-By Download link : {href}")
        else:
            print(f"Safe-link: {href}")
downloadcheck()
