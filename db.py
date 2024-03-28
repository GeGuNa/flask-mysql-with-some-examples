import mysql.connector.pooling
#import mysql.connector.pooling

"""
mydb = mysql.connector.connect(
  host="localhost",
  user="kekz",
  password="123456",
  database="qwerty"
)
"""

db_conf = {
  "host":"localhost",
  "user":"kekz",
  "password":"123456",
  "database":"qwerty"
}


mysql = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool", pool_size = 5, **db_conf)

#mysql = mysql.connector.MySQLConnection(pool_name = "mypool",pool_size = 5,**db_conf)


#def mysql_query(connection,query):
"""
def mysql_query(query, params=None, executing="execution"): 
    cursor = mydb.cursor()
    
    cursor.execute(query, params)
    data = cursor.fetchone()

    print(data)

    if executing != "execution":
	mydb.commit()
    

        #cursor.close()

    return data
"""


def mysql_query(query, params=None, executing="z"): 
    """    

    cursor = mydb.cursor()
   

    #if params is None:
    #if params != None:
    if params is not None:
     cursor.execute(query, params)
    else:
     cursor.execute(query)


    data = cursor.fetchone()

    print(data)

    if executing != "z":
     mydb.commit()
     
    mydb.close()

    cursor.close()
    """

#data_1 = "select * from `user` where `id` = %s and `username` = %s"
#val = (12,'FoLLeN')
#qqq_1 = mysql_query(query=data_1, params=val)
#print(qqq_1)


def fetch():
	
	mycursor = mydb.cursor()
	
	mycursor.execute("select * from user")
	
	data = mycursor.fetchall()
	

	mycursor.close()
	#mydb.close()
	
	return data
	
def fetchOne(select: str, data):
	
	mycursor = mydb.cursor()
	
	mycursor.execute(select, data)
	
	data = mycursor.fetchone()
	
	
	
	mycursor.close()
	#mydb.close()
	
	
	return data	

    


def improved_mysql_query(query, params=None, fetchall=False):

    cursor = None

    connection_object = mysql.get_connection()



    try:
        cursor = connection_object.cursor()
        cursor.execute(query,params)

        if fetchall:
            data = cursor.fetchall()
        else:
            data = cursor.fetchone()

        return data

    except Error as e:
        print(f"Error executing query: {err}")
        raise 

    finally:
     if cursor:
       cursor.close()
     if mysql:
       connection_object.close()










def fetchOneFromSpecific(table: str, column: str, uid: int):
	
	mycursor = mydb.cursor()
	
	sql = f"select * from {table} where {column} = {uid}"
	
	mycursor.execute(sql)
	
	data = mycursor.fetchone()
	
	mycursor.close()
	#mydb.close()
	
	
	return data	



def insertInto(table: str, columns, data):
    sql = "INSERT INTO {0} ({1}) VALUES (".format(table, ",".join(columns))
    sql += ", ".join(["%s"] * len(columns))
    sql += ") "
    awww_Data = tuple(data)
    
    mycursor = mydb.cursor()
    
    mycursor.execute(sql, awww_Data)
    mydb.commit()
    
    print(mycursor.rowcount, "record inserted.")
    
    mycursor.close()
    #mydb.close()




def deteleFrom(table, column, uid):


    
    mycursor = mydb.cursor()
    
    
    Tlq1 = f"delete from {table} where {column} = {uid}"
    
    mycursor.execute(Tlq1)
    mydb.commit()
    
    mycursor.close()
   # mydb.close()






#Table = "user"
#Columns = ['name','surname','added_time']
#Data = ['abuhuhqwe_123', 'qwe_11',12412313]

#insertInto(Table, Columns, Data)

#print(mydb)






#mycursor = mydb.cursor()

#mycursor.execute("select * from user")

#for x in mycursor:
  #print(x)
