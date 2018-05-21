#-*- coding=utf-8 -*-
from flask import  url_for, request, redirect, render_template, make_response, abort
from app import app, models
import app.functions.core as func


@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def index():
    method = request.args.get('m')
    if method:
        return redirect('/'+method)
    else:
        return render_template('index.html',title='Index - Pcap Analyzer',content=func.analyze())

@app.route('/show')
def show():
    return render_template('show.html', title='Show - Pcap Analyzer')

@app.route('/pcap')
def pcap():
    p = func.readpcap('p1.pcap')
    return p

@app.route('/add')
def add():
    return models.runPcap()

@app.route('/query')
def query():
    return render_template('index.html', title='Show - Pcap Analyzer',content=func.loadpcap())

@app.errorhandler(404)
def page_not_found(error):
    return make_response(render_template('404.html', title='404 - Pcap Analyzer'),404)