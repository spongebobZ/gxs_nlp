from bs4 import BeautifulSoup,re

path = 'C:\\Users\\Ngai\\Desktop\\gxs_white\\whitev3.0.html'
soup  = BeautifulSoup(open(path,'rb'))
print(soup.title)
r = re.compile(r'[a-zA-Z0-9\{\}\-\;\_\/\+\=\.\(\)\'\<\>\:]')
for child in soup.descendants:
    s = child.string
    if s:
        print(r.sub('',s.strip()))