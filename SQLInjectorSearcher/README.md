# SQLInjectorSearcher
SQLInjectorSearcher is a Python package designed to assist in web crawling and SQL injection point extraction. This package contains two main modules: Crawl.py and extract.py.

# Crawl.py
Crawl.py provides functionalities to crawl web pages and extract links. It utilizes a simple HTML parser (SimpleHTMLParser) to parse HTML content and extract links from anchor tags (<a>).

# Usage
python
Copy code
from Crawl import crawl
```
from Crawl import crawl

print(crawl("http://vulnerable-web.com", 10))

```


# extract.py

extract.py contains functions to extract potential SQL injection points from web page responses. It uses regular expressions to identify URLs with query parameters and modifies them to replace parameter values with a placeholder.

# Usage

python Copy code from extract import extractParam
```
from extract import extractParam

response = """Sample response using URLs with query params"""
print(extractParam(response, 'high', ['blacklisted'], 'PLACEHOLDER'))

```

# Installation
To use the SQLInjectorSearcher package, clone the repository and import the desired modules into your Python scripts.

```
git clone https://github.com/yourusername/SQLInjectorSearcher.git

```

