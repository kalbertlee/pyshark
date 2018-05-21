#-*- coding=utf-8 -*-
import os
from pickle import dumps,loads
import scapy.all as scapy
from scapy.layers import http
from app import config
from app.models import *

def analyze():
    return 'analyze'

def readpcap(pname):
    db_clean()
    path = os.path.join(config.UPLOAD_DIR, pname)
    rd = scapy.rdpcap(path)
    p = Pcap(pname)
    p.add()
    for i in rd.res:
        print('*'*40)
        print(type(i))
        print(i)
        pr = PcapRes(p.pid,dumps(i))
        pr.add()
    return repr(p)

def loadpcap():
    p_res = PcapRes.query.all()
    thead = ''
    tbody = ''
    content = ''
    for i in p_res:
        thead,tbody = i.tableformat(layer=loads(i.raw),filter='IP')
        content += tbody
    return '<div class="table-responsive" style="width:300%"><table data-toggle="table" class="table table-condensed table-striped text-nowrap" style="table-layout:fixed"><colgroup>'+'<col class="col-md-12">'*(thead.count('<th'))+'</colgroup><thead>'+thead+'</thead><tbody>'+content+'</tbody></table></div>'