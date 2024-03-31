import mysql.connector.pooling 

class Db:
        
    sql = None
        
    def __init__(self, host, user, password, database):
        
        db_conf = {
          "host":host,
          "user":user,
          "password":password,
          "database":database
        }

        self.sql = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool", pool_size = 5, **db_conf)


    def improved_mysql_query(self, query, params=None, fetchall=False):

        cursor = None

        connection_object = self.sql.get_connection()



        try:
            cursor = connection_object.cursor()
            cursor.execute(query,params)

            if fetchall == False:
                data = cursor.fetchall()
            else:
                data = cursor.fetchone()

            return data

        except TypeError as err:
            print(f"Error executing query: {err}")
            raise 

        finally:
         if cursor:
           cursor.close()
         if self.sql:
           connection_object.close()

    
qqq = Db(host="localhost",user="kekz",password="123456",database="qwerty")



usr_tbl = qqq.improved_mysql_query("select * from user")

print(usr_tbl)
