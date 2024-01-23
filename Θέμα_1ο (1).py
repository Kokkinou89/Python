# Εισαγωγή του οδηγού mysql.connector ως mysql.
import mysql.connector as mysql

# Δημιουργία του αντικειμένου σύνδεσης με τη βάση test.
mydb = mysql.connect(host = 'localhost',
                     user = 'root',
                     passwd = '',
                     db = 'test')

# Δημιουργία του αντικειμένου κέρσορα της βάσης test.
cursor = mydb.cursor()

# Δημιουργία του πίνακα Sequence με τα ζητούμενα 4 πεδία, όπου:
# 1. Το πρώτο πεδίο παίρνει ακέραιες τιμές.
# 2. Το δευτερο πεδίο παίνρει αλφαριθμητικές τιμές μήκους 3.
# 3. Το τρίτο πεδίο παίρνει αλφαριθμητικές τιμές μεταβαλλόμενου μήκους έως 40.
# 4. Το τέταρτο πεδίο παίρνει ακέραιες τιμές.
cursor.execute("""CREATE TABLE Sequence (ID INT,
                                         KIND CHAR(3),
                                         BIO_SEQ VARCHAR(40),
                                         YEAR INT)""")

# Εφαρμογή των αλλαγών στην βάση.
mydb.commit()
