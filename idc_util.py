import MySQLdb as mysql


def mysql_util(sql):
    conn = mysql.connect(user='cmdb',passwd='ming',host='192.168.31.2',db='cmdb',charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    fetch_all = cur.fetchall()
    cur.close()
    conn.commit()
    return fetch_all

def get_idclist():
    sql = 'select * from idc'
    idc_list = mysql_util(sql)
    return idc_list

def add_idc(name='default',address='default',contacts='default'):
    sql = 'insert into idc (name,address,contacts) values ("%s","%s","%s")' %(name,address,contacts)
    mysql_util(sql)

def del_idc(idc_id):
    sql = 'delete from idc where id=%s' %(idc_id)
    mysql_util(sql)

def select_idc_by_id(idc_id):
    #print '---------------------------------------'
    #print idc_id
    sql = 'select * from idc where id=%s' %(idc_id)
    idc_list = mysql_util(sql)
    return idc_list

def update_idc_by_id(idc_id,idc_name,idc_address,idc_contacts):
    sql = 'update idc set name="%s",address="%s",contacts="%s" where id=%s' %(idc_name,idc_address,idc_contacts,idc_id)
    mysql_util(sql)

def get_srvlist():
    sql = 'select * from servers'
    srv_list = mysql_util(sql)
    return srv_list

def add_srv(srv_ip,srv_hostname,srv_username,srv_password,srv_idcid,srv_remarks,srv_ctime):
    sql = 'insert into servers (ip,hostname,username,password,idc_id,remarks,create_time) values ("%s","%s","%s","%s",%s,"%s","%s")' %(srv_ip,srv_hostname,srv_username,srv_password,srv_idcid,srv_remarks,srv_ctime)
    mysql_util(sql)

def del_srv(srv_id):
    sql = 'delete from servers where id=%s' %(srv_id)
    mysql_util(sql)

def select_srv_by_id(srv_id):
    sql = 'select * from servers where id=%s' %(srv_id)
    srv_list = mysql_util(sql)
    return srv_list

def update_srv_by_id(srv_id,srv_ip,srv_hostname,srv_username,srv_password,srv_idcid,srv_remarks,srv_ctime):
    sql = 'update servers set ip="%s",hostname="%s",username="%s",password="%s",idc_id=%s,remarks="%s",create_time="%s" where id=%s' %(srv_ip,srv_hostname,srv_username,srv_password,srv_idcid,srv_remarks,srv_ctime,srv_id)
    mysql_util(sql)
