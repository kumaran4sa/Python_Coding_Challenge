import sqlite3

db = sqlite3.connect("C:\\Users\\kumar\\OneDrive\\Desktop\\users.db")
cursor = db.cursor()

# cursor.execute("Create table if not exists user (ID Integer primary key autoincrement, Name Text, Age Integer, City Text)")


def insertdata(name,age,city):
    cursor.execute("Insert into user(Name,Age,City) values (?,?,?);",(name,age,city))
    db.commit()
    print("Data Added successfully...")

def updatedata(name,city,id):
    cursor.execute("Update user set Name=?,City=? Where ID=?;",(name,city,id))
    db.commit()
    print("Data Updated successfully...")



name = input('Enter Name :')
# age = int(input('Enter Age :'))
city = input('Enter City :')
id = int(input('Enter Id :'))

# insertdata(name,age,city)
updatedata(name,city,id)




cursor.execute("Select * from user")
rows = cursor.fetchall()

for row in rows:
    print(row)