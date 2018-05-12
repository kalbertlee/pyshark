#-*- coding=utf-8 -*-
from ext import db

class Pcap(db.Model):
    __tablename__ = 'pcap_list'
    pid = db.Column(db.Integer,primary_key=True,autoincrement=True,index=True)
    pname = db.Column(db.String(255),nullable=False)

    def __init__(self, pname):
        self.pname = pname

    def __repr__(self):
        return '[{}] {}'.format(self.pid,self.pname)

class PcapRes(db.Model):
    __tablename__ = 'pcap_result'
    rid = db.Column(db.Integer,primary_key=True,autoincrement=True,index=True)
    pid = db.Column(db.Integer)
    raw = db.Column(db.LargeBinary(1500))

    def __init__(self, pid, raw):
        self.pid = pid
        self.raw = raw

    def __repr__(self):
        return self.raw

class PcapFlt(db.Model):
    __tablename__ = 'pcap_filter'
    fid = db.Column(db.Integer, primary_key=True, autoincrement=True,index=True)
    pid = db.Column(db.Integer)
    fstr = db.Column(db.String(1024))

    def __init__(self, pid, fstr):
        self.pid = pid
        self.fstr = fstr

class PcapFltRes(db.Model):
    __tablename__ = 'pcap_filter_result'
    frid = db.Column(db.Integer, primary_key=True, autoincrement=True,index=True)
    fid = db.Column(db.Integer)
    raw = db.Column(db.LargeBinary(1500))

    def __init__(self, fid, raw):
        self.fid = fid
        self.raw = raw

    def __repr__(self):
        return self.raw

class PcapTCPStream(db.Model):
    __tablename__ = 'pcap_tcpstream'
    sid = db.Column(db.Integer, primary_key=True, autoincrement=True,index=True)
    sindex = db.Column(db.Integer)
    raw = db.Column(db.LargeBinary(1500))

    def __init__(self, raw):
        self.raw = raw

class PcapUDPStream(db.Model):
    __tablename__ = 'pcap_udpstream'
    sid = db.Column(db.Integer, primary_key=True, autoincrement=True,index=True)
    pid = db.Column(db.Integer)
    sindex = db.Column(db.Integer)
    raw = db.Column(db.LargeBinary(1500))

    def __init__(self, raw):
        self.raw = raw

def addPcap(pname):
    pcap = Pcap(pname=pname)
    return pcap

def addPcapRes(pcap):
    pcap_res = PcapRes(pid=pcap.pid,raw='123')
    return pcap_res

def runPcap():
    db.drop_all()
    db.create_all()

    pcap = addPcap('p2.pcap')
    print(pcap.pid)
    pcap_res = addPcapRes(pcap)
    db.session.add(pcap)
    db.session.commit()
    npcap = Pcap.query.get(1)#filter_by(pid=1).first()
    print(npcap.pid)
    return str(pcap)