# Λίστα με τις δυνατές ενέργειες του χρήστη.
actions = ['1. Εισαγωγή νέας εγγραφής',
           '2. Διαγραφή εγγραφής',
           '3. Εκτύπωση εγγραφής',
           '4. Έξοδος']

# Εκτύπωση της παραπάνω λίστας.
for x in actions:
    print(x)

# Εισαγωγή του αναγνωριστικού ενέργειας από το χρήστη.
# Επειδή είναι ακέραιος χρησιμοποιούμε την int().
action_taken = int(input('Δώστε αναγνωριστικό ενέργειας: '))

# Εισαγωγή της κλάσης Sequence.
from sequence import Sequence

# Εισαγωγή του οδηγού mysql.connector ως mysql.
import mysql.connector as mysql

# Δημιουργία του αντικειμένου σύνδεσης με τη βάση test.
mydb = mysql.connect(host = 'localhost',
                     user = 'root',
                     passwd = '',
                     db = 'test')

# Δημιουργία του αντικειμένου κέρσορα της βάσης test.
cursor = mydb.cursor()

# Περιπτώσεις για τις δυνατές πράξεις του χρήστη.

# Περίπτωση που θα δώσει την τιμή 1.
if action_taken == 1:

    # Εισαγωγή των δεδομένων που θέλει να εισάγει στον πίνακα Sequence ο χρήστης.
    new_entry_id = int(input('Δώστε αναγνωριστικό εγγραφής: '))
    new_entry_kind = input('Δώστε είδος αλληλουχίας: ')
    new_entry_seq = input('Δώστε την βιολογική αλληλουχία: ')
    new_entry_year = int(input('Δώστε έτος καταχώρησης: '))

    # Δημιουργία αντικειμένου Sequence με τη χρήση των δεδομένων που δόθηκαν
    # από τον χρήστη.
    new_entry = Sequence(new_entry_id,
                         new_entry_kind,
                         new_entry_seq,
                         new_entry_year)
    
    # Λίστα που περιλαμβάνει τις περιπτώσεις που το αποτέλεσμα της validate()
    # επικυρώνει την αλληλουχία.
    right = ['DNA sequence is valid.','RNA sequence is valid.']

    # Στην περίπτωση που δεν είναι έγκυρη η ακολουθία, δηλαδή το αποτέλεσμα της
    # validate() δεν ανήκει στην παραπάνω λίστα, θα έχει δοθεί λανθασμένη
    # αλληλουχία και θα τερματίζει το πρόγραμμα με το κλείσμο του κέρσορα και της
    # σύνδεσης με τη βάση.
    if new_entry.validate() not in right:
        print('Wrong sequence given.')
        cursor.close()
        mydb.close()

    # Αν είναι έγκυρη η ακολουθία θα εισάγεται η καινούρια πληροφορία ως μία
    # καινούρια εγγραφή στον πίνακα Sequence.
    else:
      cursor.execute("""INSERT INTO Sequence VALUES(%s,'%s','%s',%s)"""
                     %(new_entry_id,
                       new_entry_kind,
                       new_entry_seq,
                       new_entry_year))
      mydb.commit()

# Περίπτωση που θα δώσει την τιμή 2.
elif action_taken == 2:
    
    # Δίνεται από τον χρήστη το αναγωριστικό της εγγραφής που θέλει να διαγράψει.
    entry_id = int(input('Δώστε αναγνωριστικό εγγραφής: '))

    # Επιλέγονται όλα τα πεδία του πίνακα Sequence.
    cursor.execute("""SELECT * from Sequence""")

    # Εκχωρούνται όλες οι εγγραφές του πίνακα Sequence στην μεταβλητή entries.
    entries = cursor.fetchall()

    # Διαγράφεται η εγγραφή με το αναγνωριστικό που δόθηκε από το χρήστη.
    cursor.execute("""DELETE from Sequence WHERE ID = %s""" %(entry_id))
    mydb.commit()

    # Επιλέγονται ξανά όλα τα πεδία του πίνακα Sequence μετά την διαγραφή.
    cursor.execute("""SELECT * from Sequence""")

    # Εάν το πλήθος των εγγραφών πριν την διαγραφή ισούται με το πλήθος μετά,
    # τότε δεν διαγράφθηκε κάποια από τις εγγραφές. Επομένως, δεν υπήρχε
    # εγγραφή με το αναγνωριστικό που δόθηκε.
    if len(entries) == len(cursor.fetchall()):
            print('Δεν υπάρχει εγγραφή με αναγνωριστικό %s.' %(entry_id))   
        
# Περίπτωση που θα δώσει την τιμή 3.
elif action_taken == 3:

    # Εισαγωγή των δεδομένων εγγραφής που θέλει να εκτυπώσει ο χρήστης.
    entry_id = int(input('Δώστε αναγνωριστικό της ζητούμενης εγγραφής: '))
    entry_kind = input('Δώστε είδος της ζητούμενης αλληλουχίας: ')
    entry_seq = input('Δώστε την ζητούμενη βιολογική αλληλουχία: ')
    entry_year = int(input('Δώστε το ζητούμενο έτος καταχώρησης: '))

    # Επιλογή των εγγραφών που επαληθεύουν τα δεδομένα που δόθηκαν από
    # τον χρήστη, λαμβάνοντας υπόψη την περίπτωση που η αλληλουχία δόθηκε
    # με μικρούς ή κεφαλαίους χαρακτήρες.
    cursor.execute("""SELECT * from Sequence WHERE ID = %s AND
                                                   KIND = '%s' AND
                                                   (BIO_SEQ = '%s' OR
                                                   BIO_SEQ = '%s') AND
                                                   YEAR = %s"""
                   %(entry_id, entry_kind,
                     entry_seq.upper(), entry_seq.lower(),
                     entry_year))

    # Εκχώρηση των αποτελεσμάτων - εγγραφής που επαληθεύουν τα παραπάνω.
    entries = cursor.fetchall()

    # Εάν βρέθηκε εγγραφή, δηλαδή η λίστα entries δεν είναι άδεια, δημιουργούμε
    # αντικείμενο με τα δεδομένα της εγγραφής αυτής, ώστε να χρησιμοποιήσουμε
    # τη μέθοδο print_info() της κλάσης Sequence, για την εκτύπωση της εγγραφής
    # που βρήκαμε.
    if len(entries) > 0:
        entry = Sequence(entries[0][0],
                         entries[0][1],
                         entries[0][2],
                         entries[0][3])

        entry.print_info()
        
# Περίπτωση που θα δώσει την τιμή 4.
elif action_taken == 4:
    
    # Επιλέγονται όλα τα πεδία του πίνακα Sequence.
    cursor.execute("""SELECT * from Sequence""")

    # Εκχωρούνται όλες οι εγγραφές του πίνακα Sequence στην μεταβλητή entries.
    entries = cursor.fetchall()

    # Το κάθε στοιχείο της παραπάνω λίστας περιλαμβάνει τα τέσσερα πεδία της
    # αντίστοιχης εγγραφής. Επομένως, για κάθε στοιχείο της λίστας, δημιουργούμε
    # αντικείμενο της κλάσης Sequence, ώστε να χρησιμοποιήσουμε τη μέθοδο
    # print_info().
    for x in entries:
        entry = Sequence(x[0],x[1],x[2],x[3])
        entry.print_info()

    # Τερματισμός του κέρσορα και της σύνδεσης με τη βάση.
    cursor.close()
    mydb.close()
    






