import datetime
from bs4 import BeautifulSoup
import requests
import urllib.request
import pymysql

now = datetime.datetime.now()
nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')
print(nowDate)

print('<< 오늘의 헤드라인 >>\n')
webpage = urllib.request.urlopen('https://www.naver.com')
#print(type(webpage),type(webpage.read()))
#resp = requests.get('https://www.naver.com')
#print(type(resp),type(resp.text))

soup=BeautifulSoup(webpage,'html.parser')
#print(soup.find_all('a',"issue"))
for temps in soup.find_all('a',"issue"):
    print('-->',temps.get_text())
print('\n')

print('<<오늘의 음원 종합 TOP 10 >>\n')
resq=urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EC%9D%8C%EC%9B%90%EC%B0%A8%ED%8A%B8')
toptenlist=[]
artistlist=[]
Rank=10
soup = BeautifulSoup(resq,'html.parser')

for topten in soup.find_all('a','tit'):
    toptenlist.append(topten.get_text())
for artist in soup.select('.dsc_area span:last-child a'):
    artistlist.append(artist.get_text())

for i in range(Rank):
    print(' - %2d위 : %s - %s'%(i+1,artistlist[i],toptenlist[i]))

#주식 정보
def get_company_list(url):
    resp = requests.get(url)
    resp.raise_for_status()
    resp.encoding=None
    #resp.encoding='euc-kr'
    html=resp.text
    soup = BeautifulSoup(html, 'html.parser')
    company_dic = {}
    for i in soup.find_all('a','tltle'):
        company_dic[i.get_text()] = i['href'].split('=')[1]
    return company_dic

mysql_host = "127.0.0.1"
mysql_user = "root"
mysql_passwd = '1234'
mysql_db = "shop"
mysql_port = 3306
conn = pymysql.connect(host=mysql_host, user=mysql_user, password=mysql_passwd, db=mysql_db, port=mysql_port, charset='utf8')
conn.autocommit(True)
cur = conn.cursor()
#CREATE TABLE COMPANY2 (
#  company_id varchar(11) NOT NULL DEFAULT '',
#  company_name varchar(255) DEFAULT '',
#  company_type tinyint(10) DEFAULT NULL,
#  PRIMARY KEY (`company_id`)
#) DEFAULT CHARSET=utf8;
url = 'https://finance.naver.com/sise/sise_quant.naver'
url_kos = 'https://finance.naver.com/sise/sise_quant.naver?sosok=1'
company_info=get_company_list(url)
for k,v in company_info.items():
    cur.execute("REPLACE INTO COMPANY2 (company_id, company_name, company_type) VALUES (%s, %s, %s)", (v, k, 1))
kosdaq_info=get_company_list(url_kos)
for k,v in kosdaq_info.items():
    cur.execute("replace into COMPANY2 (company_id, company_name, company_type ) values ('{}', '{}', '{}')".format( v, k, 0 ))
