from typing import Counter
import pymysql
import json

# 从config.txt 文件中获取数据库信息
f = open("config.txt", "r", encoding="utf-8")
data = json.loads(f.read())
dbhost = data['dbhost']
dbuser = data['dbuser']
dbpass = data['dbpass']
dbname = data['dbname']

# 连接数据库
db = pymysql.connect(host=dbhost,user= dbuser,password= dbpass, database=dbname)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()