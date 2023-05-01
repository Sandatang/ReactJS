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
        if kwargs:
            self.values_update_specific = tuple(kwargs.values())[1:] + (tuple(kwargs.values())[0],)
            self.header_update_specific = tuple(kwargs.keys())[1:]

    def getData(self):
        cursor = self.db.cursor()
        cursor.execute(f"select * from {self.table}")
        data = cursor.fetchall()
        return data
    
    def getSingleData(self):
        cursor = self.db.cursor()
        query = f"select * from {self.table} where {self.headers} = %s"
        cursor.execute(query, self.values)
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
    
    def updateQuery(self):
        cursor = self.db.cursor()
        query = f"update {self.table} set {', '.join([f'{head} = %s' for head in self.header_update_specific])} where idno = %s"
        cursor.execute(query, self.values_update_specific)
        self.db.commit()
        row = cursor.rowcount
        return True if row > 0 else False