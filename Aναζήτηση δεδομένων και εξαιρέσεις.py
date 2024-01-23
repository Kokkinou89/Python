#Σύνδεση στην βάση
import mysql.connector as mysql
#σύνδεση στη βάση
mydb = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = 'dna')
cur = mydb.cursor()

#δημιουργία ερωτήματος
statement = "SELECT * FROM gene"
cur.execute(statement)
numrows = int(cur.rowcount)
print(numrows)

#είσοδος από το χρήστη
chromosome = input ('Enter chromosome to search:')
statement = "SELECT * FROM gene where chromosome='%s'"%chromosome

#αναζήτηση
cur.execute(statement)
numrows = int(cur.rowcount)
for x in range(0,numrows):
  row = cur.fetchone()
  print(row)
  
try:
#είσοδος από το χρήστη
 gene_id = input ('Enter gene_id to search:')
 statement2 = "SELECT * FROM gene where gene_id='%s'"%gene_id
#αναζήτηση
 cur.execute(statement2)
 results = cur.fetchall()
 print(results)
except Exception:
 print("Something went wrong")    

                  
        
                  

                
