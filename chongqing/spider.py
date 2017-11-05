import requests
from bs4 import BeautifulSoup
import datetime
from .models import QCSSC


def crawl_bulk(start, end):

    dd = d + '_' + d
    url = 'http://chart.cp.360.cn/kaijiang/kaijiang?lotId=255401&spanType=2&span=%s' % dd

    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'lxml')
    rs = []

    for td in soup.find(attrs={'class': 'tr-odd1', 'width': '100%'}).find_all(attrs={'class': 'red big'}):
        if td.string:
            rs.append(td.string)

    for td in soup.find(attrs={'class': 'tr-odd2', 'width': '100%'}).find_all(attrs={'class': 'red big'}):
        if td.string:
            rs.append(td.string)

    for td in soup.find(attrs={'class': 'tr-odd3', 'width': '100%'}).find_all(attrs={'class': 'red big'}):
        if td.string:
            rs.append(td.string)
    return rs


def crawl_once():
    url = 'http://www.cqcp.net/'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'lxml')
    rs = []

    for li in soup.find(attrs={'class': 'kjggul_2', 'id': 'ulkj_2', 'onmouseover': 'ShowKjgg(2)'}).find_all('li'):
        if li.string:
            rs.append(li.string)

    rs[0] = rs[0][0:9]
    return rs
