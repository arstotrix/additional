import re, urllib.parse

import urllib.parse
def unicoday(url):
    url = urllib.parse.urlsplit(url)
    url = list(url)
    url[3] = urllib.parse.quote(url[3])
    url = urllib.parse.urlunsplit(url)

def main():
    print(unicoday("https://www.hse.ru/org/persons/?ltr=Все;udept=141971113"))

if __name__ == "__main__":
    main()
