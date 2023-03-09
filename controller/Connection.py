import mysql.connector

class Connection:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

        

    def executeInsert(self, table,nvalues,tuple):
        self.cursor.execute(f"INSERT INTO {table} values ({nvalues})",tuple)
    
    def executeSelect(self,variable,table,sentence,values=None):
        self.cursor.execute(f"SELECT {variable} FROM {table} {sentence}= %s",(values,))
    
    def executeUpdate(self,table,variable,value,idv):
        print(idv)
        self.cursor.execute(f"UPDATE {table} set {variable}=%s where id={idv}",(value,))

    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def close(self):
        self.cursor.close()
        self.connection.close()

