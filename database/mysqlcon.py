import mysql.connector
from config import CONFIG_MYSQL, TABLE_NAME


class DBHelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(**CONFIG_MYSQL)
        except:
            self.conn = None
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('''CREATE TABLE {0} (pipe INTEGER, 
                                      temp1 FLOAT, hum1 FLOAT, temp2 FLOAT,
                                      hum2 FLOAT, press FLOAT, 
                                      date_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)'''.format(TABLE_NAME))
        except:
            pass

    def insert_db(self, pipe, tepm1, hum1, temp2, hum2, press):
        self.cursor.execute("INSERT INTO data_dht(pipe, temp1, hum1, temp2, hum2, press) VALUES " +
                       "({0}, {1}, {2}, {3}, {4}, {5})".format(pipe, tepm1, hum1, temp2, hum2, press))
        self.conn.commit()

    def select_pipe(self, pipe):
        resulte = []
        self.cursor.execute("SELECT * FROM data_dht WHERE pipe = {0}".format(pipe))
        row = self.cursor.fetchone()
        while row is not None:
            resulte.append(row)
            row = self.cursor.fetchone()
        return resulte

    def select_pipe_cols(self, pipe, col):
        resulte = []
        self.cursor.execute("SELECT {0} FROM data_dht WHERE pipe = {1}".format(col, pipe))
        row = self.cursor.fetchone()
        while row is not None:
            resulte.append(row)
            row = self.cursor.fetchone()
        return resulte


    def __del__(self):
        # self.cursor.close()
        if self.conn is not None:
            self.conn.close()
