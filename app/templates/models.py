from app import app
from ext import db
db.init_app(app)

class Pcap(db.Model):
    __tablename__ = 'pcap_list'
    pid = db.Column(db.Integer,primary_key=True,autoincrement=True,index=True)
    pname = db.Column(db.String(255),nullable=False)

    def __init__(self, pname):
        self.pname = pname

    def __repr__(self):
        return '['+self.pid+']'+self.pname

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