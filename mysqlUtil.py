import MySQLdb as mysql
class DB:
    def __init__(self,host,user,password,db):
        #print host + ' ' + user + " " + password + " " + db
        self.host = host
        self.user = user
        self.password = password
        self.db = db
    def execute(self,sql):
        self.connect()
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
        except Exception as e:
            print e

        fetch_all_dict = cursor.fetchall()
        cursor.close()
        self.conn.commit()
        self.conn.close()
        return fetch_all_dict

    def connect(self):
        self.conn = mysql.connect(host=self.host,user=self.user,passwd=self.password,db=self.db,charset='utf8')
        
    
