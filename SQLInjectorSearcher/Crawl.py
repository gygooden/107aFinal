from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen


class SimpleHTMLParser(HTMLParser):
    
    def __init__(self):
        super().__init__()
        self.links = []
        self.base_url = ""

    def handle_startt(self, t, atr):

        if t == 'a':
            for key, value in atr:
                if key == 'href':
                    self.links.append(urljoin(self.base_url, value))

    def extract(self, url):
        self.base_url = url
        self.links = []
        response = urlopen(url)
        
        if 'text/html' in response.getheader('Content-Type'):
            html_content = response.read().decode("utf-8")
            self.feed(html_content)
            return self.links
        return []

def crawl(start_url, max):
    vis = [start_url]
    vislinks = []
    viscount = 0
    
    while viscount < max and vis:
        curr_url = vis.pop(0)
        viscount += 1
        
        try:
            parser = SimpleHTMLParser()
            new_links = parser.extract_links(curr_url)
            vislinks.extend(new_links)
            vis.extend(new_links)

        except Exception as e:
            print(f"Error while crawling {curr_url}: {e}")

    return vislinks

if __name__ == "__main__":

    print(crawl("http://vulnerable-web.com", 10))
