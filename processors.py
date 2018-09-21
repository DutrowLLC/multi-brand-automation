import MySQLdb as mdb
from settings import user, passwd, host, db

class Processors(object):
    def __init__(self):
        pass

    def mysql_connect(self):
        self.conn = mdb.connect(
            user = user,
            passwd = passwd,
            host = host,
            db = db
        )
        self.cur = self.conn.cursor()

    def mysql_close(self):
        self.conn.commit()
        self.conn.close()

