import pymysql

class DBHelper:
    def connect(self, database='crimemap'):
        return pymysql.connect(host='localhost', user='root', password='', db=database)

def get_all_puts(self):
    connection = self.connect()
    try:
        query = "SELECT description FROM crimes;"
        with connection.cursor() as cursor:
            cursor.execute(query)
        return cursor.fetchall()
    finally:
        connection.close()

def add_input(self, data):
    connection = self.connect()
    try:
        #The following introduces a deliberate security flaw.
        query = "INSERT INTO crimes (description) VALUES('{}');".format(data)
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    finally:
        connection.close()

def clear_all(self):
    connection = self.connect()
    try:
        query = "DELETE FROM crimes;"
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    finally:
        connection.close()