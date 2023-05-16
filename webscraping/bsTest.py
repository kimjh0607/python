#pip install

from bs4 import BeautifulSoup
#from 모듈 import 변수/from 모듈 import 함수
#from 모듈 import 클래스/from 모듈 import *

hfile = './input/scraping.html'
with open(hfile, encoding='utf-8') as fp:
    html_str=fp.read()
#print(html_str)

soup = BeautifulSoup(html_str, 'html5lib')
print(soup.prettify()+'\n')

title=soup.title
print(title)
print(title.string+'\n')

print(type(soup))
print(type(title))
print(type(title.string))

e=soup.head
result = [
    e.title,
    e.parent,
    e.contents,
    list(e.children),
    e.previous_sibling,
    e.next_sibling,
    e.previous_element,
    e.title.next_element
]
for r in result:
    print(r)
    print('=============')
print(e.parent.name)
print(e.parent.parent.name)

for c in e.contents:
    print('[{}]{}'.format(type(c),c.name))

e=soup.div
result=[
    e.name,
    e.h1['id'],
    e.h1.attrs,
    e.h1.string,
    list(e.strings),
    e.text
]
for r in result:
    print(r)
    print('=============')

print(soup.find('p'))
print(soup.find(class_='example'))
print(soup.find(attrs={'class':'example'}))
print(soup.find('p',class_='example'))
print(type(soup.find('p',class_='example')))

print(soup.select("title"))
print(soup.select('p'))
print(soup.select_one('p'))

print(soup.select("div a"))
print(soup.select("head > title"))
print(soup.select("div > #link1"))
print(soup.select("#ling1 ~ .sister"))
print(soup.select("#ling1 + .sister"))
print(soup.select(".sister"))