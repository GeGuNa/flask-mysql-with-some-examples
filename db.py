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
	mydb.close()
	
	return data
	
def fetchOne(select: str, data):
	
	mycursor = mydb.cursor()
	
	mycursor.execute(select, data)
	
	data = mycursor.fetchone()
	
	
	
	mycursor.close()
	mydb.close()
	
	
	return data	
	

#print(mydb)



#mycursor = mydb.cursor()

#mycursor.execute("select * from user")

#for x in mycursor:
  #print(x)
