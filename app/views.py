



@app.route('/')
@app.route('/index')
def index():
    method = request.args.get('m')
    if method:
        if method == 'pcap':
            return redirect('/pcap')
        else:
            return render_template('html/show.html', content=method)
    else:
        return render_template('html/index.html',content='Hello World!')

@app.route('/data')
def getdata():
    pass

''''@app.route('/test')
def test():
    testdb.testdb()'''

@app.route('/pcap')
def pcap():
    print(url_for('pcap'))
    return models.runPcap()
