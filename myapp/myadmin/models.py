from django.db import models
import MySQLdb
db=MySQLdb.connect('localhost',"root",'',"book_my_meal")
cursor=db.cursor()
print("Connection Done My admin")
# Create your models here.
