from django.shortcuts import render
import datetime
from . import spider
from .models import QCSSC


# Create your views here.


def index(request):
    last = QCSSC.objects.last()
    rs = spider.crawl_once()
    if last.qihao != rs[0]:
        spider.crawl_bulk(last.qihao, rs[0])

    return render(request, 'chongqing/index.html', {'last': last, 'rs': rs})


def dbsync(request):
    pass
