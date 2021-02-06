from __future__ import unicode_literals
from django.db import models
import MySQLdb
db=MySQLdb.connect('localhost',"root",'','grocery')
cursor=db.cursor()
print("Connetion Done Myadmin")