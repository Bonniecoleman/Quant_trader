import pymysql
import os

db_password = os.getenv('db_password')

print(db_password)

con = pymysql.connect(
    user = 'root',
    passwd = db_password,
    host = '127.0.0.1',
    db = 'shop',
    charset = 'utf8'
)

mycursor = con.cursor()
#
query = """
select * from products;
"""

mycursor.execute(query)
data = mycursor.fetchall()
con.close()

for row in data:
    print(row)
