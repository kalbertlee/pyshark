#-*- coding=utf-8 -*-
from ext import db
from pickle import dumps,loads
from html import escape

class Pcap(db.Model):
    __tablename__ = 'pcap_list'
    pid = db.Column(db.Integer,primary_key=True,autoincrement=True,index=True)
    pname = db.Column(db.String(255),nullable=False)

    def __init__(self, pname):
        self.pname = pname

    def __repr__(self):
        return '[{}] {}'.format(self.pid,self.pname)

    def add(self):
        db.session.add(self)
        db.session.commit()

class PcapRes(db.Model):
    __tablename__ = 'pcap_result'
    rid = db.Column(db.Integer,primary_key=True,autoincrement=True,index=True)
    pid = db.Column(db.Integer)
    raw = db.Column(db.LargeBinary(1500))

    def __init__(self, pid, raw):
        self.pid = pid
        self.raw = raw

    def __repr__(self):
        return '[{}]-{} {}'.format(self.rid, self.pid, loads(self.raw))

    def __str__(self):
        return '[{}]-{} {}'.format(self.rid, self.pid, self._layer2str(loads(self.raw)))

    def _layer2str(self, layer=None):
        layer_str = ''
        if hasattr(layer, 'fields'):
            layer_str += '<br/>&lt;' + layer.name + ' '
            for i in layer.fields:
                layer_str += i + '="' + escape(str(layer.fields[i])) + '" '
            layer_str += '&gt;'
            if hasattr(layer, 'payload'):
                if layer.payload.name == 'NoPayload':
                    return layer_str
                layer_str += self._layer2str(layer=layer.payload)
        return layer_str

    def _layer2dict(self, layer=None, filter=None):
        layer_dict = {}
        if hasattr(layer, 'fields'):

            for i in layer.fields:
                layer_dict[layer.name+'.'+i]=escape(str(layer.fields[i]))
            if hasattr(layer, 'payload'):
                if layer.payload.name == 'NoPayload':
                    return layer_dict
                layer_dict = dict(layer_dict ,**self._layer2dict(layer=layer.payload))
        return layer_dict

    def add(self):
        db.session.add(self)
        db.session.commit()

    def tableformat(self, layer=None, filter=None):
        thead = '<tr>'
        tbody = '<tr>'
        layer_dict = self._layer2dict(layer=layer,filter=filter)
        for k in layer_dict:
            thead += '<th title="'+k.split('.')[0]+'">'+k.split('.')[1]+'</th>'
            tbody += '<td>'+layer_dict[k]+'</td>'
        thead += '</tr>'
        tbody += '</tr>'
        return (thead,tbody)


class PcapFlt(db.Model):
    __tablename__ = 'pcap_filter'
    fid = db.Column(db.Integer, primary_key=True, autoincrement=True,index=True)
    pid = db.Column(db.Integer)
    fstr = db.Column(db.String(1024))
    flist = db.Column(db.String(1024))

    def __init__(self, pid, fstr):
        self.pid = pid
        self.fstr = fstr


class PcapTCPStream(db.Model):
    __tablename__ = 'pcap_tcpstream'
    sid = db.Column(db.Integer, primary_key=True, autoincrement=True,index=True)
    pid = db.Column(db.Integer)
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

def db_clean():
    db.drop_all()
    db.create_all()


def runPcap():
    db.drop_all()
    db.create_all()

    pcap = Pcap('p2.pcap')
    pcap.add()
    print(pcap.pid)
    pcap_res = PcapRes(pcap.pid,b'1234')
    pcap_res.add()
    npcap = PcapRes.query.get(1)#filter_by(pid=1).first()
    print(npcap)
    return str(npcap)