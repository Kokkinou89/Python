import mysql.connector as mysql
mydb=mysql.connect(host="localhost", user="root", passwd="", db="menu")

my_cursor = mydb.cursor()

#είσοδος από το χρήστη
option = input ('Number:')
stroption='%'+str(option)+ '%'

#δημιουργία της επερώτησης
statement = "select * from gene where chromosome LIKE '%s'" %stroption
print(statement)

#εκτέλεση της επερώτησης
command = cur.execute(statement)
results = cur.fetchall()

#εκτύπωση των αποτελεσμάτων
for record in results:
print(record[0] , ",", record[1] , ",", record[2],",", record[3],",", record[4])
