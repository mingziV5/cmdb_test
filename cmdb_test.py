#encoding:utf8
from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import render_template
from functools import wraps
from flask import g
import idc_util
import json

cmdb_test = Flask(__name__)
cmdb_test.secret_key = 'secriet_key'

def login_required(fn):
    @wraps(fn)
    def decorated_function(*args,**kwargs):
        if not 'ming' in session:
            return redirect('/login')
        return fn(*args,**kwargs)
    return decorated_function


@cmdb_test.route('/layout')
def layout():
    return render_template('layout.html')


@cmdb_test.route('/')
@login_required
def index():
    return render_template('index.html')

@cmdb_test.route('/login')
def login_html():
    return render_template('login.html')

@cmdb_test.route('/login/login',methods=['POST'])
def login_action():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'ming' and password == 'ming':
        session[username] = username
        return 'ok'
    else:
        return 'error'

@cmdb_test.route('/login/logout')
def logout():
    username = request.args.get('username')
    if username in session:
        del session[username]
    return redirect('login')

@cmdb_test.context_processor
def inject_username():
    if 'ming' in session:
        return {'username':session['ming']}
    else:
        return {'username': 'default'}

@cmdb_test.route('/idclist')
@login_required
def get_idclist():
    idc_list = idc_util.get_idclist()
    #print idc_list
    return json.dumps(idc_list)

@cmdb_test.route('/addidc',methods=['POST'])
@login_required
def add_idc():
    #print request.form
    idc_name = request.form.get('name')
    idc_address = request.form.get('address')
    idc_contacts = request.form.get('contacts')
    idc_util.add_idc(idc_name,idc_address,idc_contacts)
    return 'ok'

@cmdb_test.route('/delidc',methods=['POST'])
@login_required
def del_idc():
    idc_id = int(request.form.get('idc_id'))
    idc_util.del_idc(idc_id)
    return 'ok'

@cmdb_test.route('/idcbyid')
@login_required
def select_idc_by_id():
    idc_id = int(request.args.get('idc_id'))
    idc_list = idc_util.select_idc_by_id(idc_id)
    return json.dumps(idc_list)

@cmdb_test.route('/updateidc',methods=['POST'])
@login_required
def update_idc_by_id():
    idc_id = int(request.form.get('idc_id'))
    idc_name = request.form.get('idc_name')
    idc_address = request.form.get('idc_address')
    idc_contacts = request.form.get('idc_contacts')
    idc_util.update_idc_by_id(idc_id,idc_name,idc_address,idc_contacts)
    return 'ok'

@cmdb_test.route('/server')
@login_required
def server_index():
    return render_template('server.html')

@cmdb_test.route('/serverlist')
@login_required
def get_srvlist():
    srv_list = idc_util.get_srvlist()
    return json.dumps(srv_list)

@cmdb_test.route('/addserver',methods=['POST'])
@login_required
def add_srv():
    srv_ip = request.form.get('ip')
    srv_hostname = request.form.get('hostname')
    srv_username = request.form.get('username')
    srv_password = request.form.get('password')
    srv_idcid = int(request.form.get('idc_id'))
    srv_remarks = request.form.get('remarks')
    srv_ctime = request.form.get('ctime')
    idc_util.add_srv(srv_ip,srv_hostname,srv_username,srv_password,srv_idcid,srv_remarks,srv_ctime)
    return 'ok'

@cmdb_test.route('/delsrv',methods=['POST'])
@login_required
def del_srv():
    srv_id = int(request.form.get('srv_id'))
    idc_util.del_srv(srv_id)
    return 'ok'

@cmdb_test.route('/srvbyid')
@login_required
def select_srv_by_id():
    srv_id = request.args.get('srv_id')
    srv_list = idc_util.select_srv_by_id(srv_id)
    return json.dumps(srv_list)

@cmdb_test.route('/updatesrv',methods=['POST'])
@login_required
def update_srv_by_id():
    srv_id = int(request.form.get('srv_id'))
    srv_ip = request.form.get('ip')
    srv_hostname = request.form.get('hostname')
    srv_username = request.form.get('username')
    srv_password = request.form.get('password')
    srv_idcid = int(request.form.get('idc_id'))
    srv_remarks = request.form.get('remarks')
    srv_ctime = request.form.get('ctime')
    idc_util.update_srv_by_id(srv_id,srv_ip,srv_hostname,srv_username,srv_password,srv_idcid,srv_remarks,srv_ctime)
    return 'ok'

if __name__  == '__main__':
    cmdb_test.run(host='0.0.0.0',debug=True)
