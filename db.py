import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="kekz",
  password="123456",
  database="qwerty"
)


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
