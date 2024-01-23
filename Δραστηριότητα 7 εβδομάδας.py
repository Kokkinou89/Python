# Εισαγωγή του οδηγού mysql.connector ως mysql.
import mysql.connector as mysql

# Δημιουργία του αντικειμένου σύνδεσης με τη βάση test.
mydb = mysql.connect(host = 'localhost',
                     user = 'root',
                     passwd = '',
                     db = 'test')

# Δημιουργία του αντικειμένου κέρσορα της βάσης test.
cursor = mydb.cursor()

#-----------------------------------------------------------------
# Παράδειγμα για εμάς, ώστε να δούμε μέσω του server τα παρακάτω.
# Δημιουργία του πίνακα gene.
cursor.execute("""CREATE TABLE gene (gene_id INT,
                                     chromosome VARCHAR(40),
                                     hugo_id INT,
                                     go_term INT,
                                     go_evid INT)""")

# Παράδειγμα για την εισαγωγή δεδομένων από έτοιμη λίστα εγγραφών.
example = [(1,'AABBCC',1,1,1),(2,'DDAABB',2,2,2),(3,'CCBBAA',3,3,3),
           (4,'CCAABB',4,4,4),(5,'ABABAB',5,5,5)]


for x in example:
    cursor.execute("""INSERT INTO gene VALUES (%s,'%s',%s,%s,%s)"""
                   %(x[0],x[1],x[2],x[3],x[4]))

mydb.commit()

# ---------------------------------------------------------------

# Από εδώ και κάτω συνεχίζουμε την άσκηση.

# Εισαγωγή του κομματιού που ενδιαφέρει τον χρήστη να βρει στις εγγραφές.
chromosome = input("Δώσε ένα κομμάτι ενός χρωμοσώματος: ")

# Επιλογή όλων των εγγραφών που περιλαμβάνουν το κομμάτι που δόθηκε από τον
# χρήστη.
cursor.execute("""SELECT * from gene WHERE chromosome LIKE '%s'"""
               %('%' + chromosome + '%'))

# Εκχώρηση των εγγραφών αυτών στην μεταβλητή entries.
entries = cursor.fetchall()

# Εκτύπωση των εγγραφών αυτών.
for x in entries:
    print(x)

# Κλείσιμο του κέρσορα και της σύνδεσης με τη βάση.
cursor.close()
mydb.close()




