#To connect mysql in easy way.
import mysql.connector 
#To setup and .env environment.
from decouple import config

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = config('DB_USER'),
    passwd = config('DB_PASSWORD')
)


#Preparing a cursor object
cursorObject = dataBase.cursor()

#Creating a database.
cursorObject.execute("CREATE DATABASE djcrmDB")
