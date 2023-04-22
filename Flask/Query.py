from mysql.connector import connect
 
db = {
    "host":"localhost",
    "user":"root",
    "password":"",
    "database":"pythondb"
}   

class Query():
    def __init__(self,table, **kwargs):
        self.db = connect(**db)
        self.table = table
        self.headers = ', '.join(kwargs.keys())
        self.values = tuple(kwargs.values())

    def getData(self):
        cursor = self.db.cursor()
        cursor.execute(f"select * from {self.table}")
        data = cursor.fetchall()
        return data

    def addQuery(self):
        cursor = self.db.cursor()
        query = f"insert into {self.table} ({self.headers}) values({','.join(['%s'] * len(self.values))})"
        cursor.execute(query, self.values)
        self.db.commit()
        row = cursor.rowcount
        return True if row > 0 else False

    def deleteQuery(self):
        cursor = self.db.cursor()
        query = f"delete from {self.table} where {self.headers} = %s"
        cursor.execute(query, self.values)
        self.db.commit()
        row = cursor.rowcount
        return True if row > 0 else False