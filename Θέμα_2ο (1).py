class Sequence:
    # Κατασκευαστής της κλάσης με τα ζητούμενα 4 πεδία.
    def __init__(self,ID,KIND,BIO_SEQ,YEAR):
        self.id = ID
        self.kind = KIND
        self.bio_seq = BIO_SEQ
        self.year = YEAR

    # Συνάρτηση εκτύπωσης της πληροφορίας των αντικειμένων της κλάσης.
    def print_info(self):
        print('ID: %s' %(self.id))
        print('KIND: %s' %(self.kind))
        print('BIOLOGICAL SEQUENCE: %s' %(self.bio_seq))
        print('YEAR: %s' %(self.year))

    # Συνάρτηση για την εγκυρότητα της βιολογικής ακολουθίας.
    def validate(self):
        # Μεταβλητές με τους έγκυρους χαρακτήρες για ακολοθίες DNA και RNA.
        DNA_dic = ['A','C','G','T']
        RNA_dic = ['A','C','G','U']

        # Μεταβλητή με την ακολουθία με κεφαλαίους χαρακτήρες, λαμβάνοντας
        # υπόψη την περίπτωση που περιείχε μικρούς.
        seq = self.bio_seq.upper()

        # Μεταβλητή - μετρητής για τους έγκυρους χαρακτήρες της ακολουθίας.
        lenght = 0

        # Έλεγχος για το είδος της ακολουθίας.

        # Περίπτωση DNA ακολουθίας.
        if self.kind == 'DNA':

            # Εύρεση πλήθους έγκυρων χαρακτήρων στην ακολουθία.
            for x in seq:
                if x in DNA_dic:
                    lenght += 1

            # Στην περίπτωση που οι έγκυροι χαρακτήρες ισούνται με το πλήθος των
            # συνολικών χαρακτήρων της ακολουθίας, τότε θα ήταν έγκυρη.
            if lenght == len(self.bio_seq):
                result = 'DNA sequence is valid.'

            # Διαφορετικά δεν θα ήταν.
            else:
                result = 'DNA sequence is invalid.'

        # Περίπτωση RNA ακολουθίας, αντίστοιχα με την προηγούμενη περίπτωση.
        elif self.kind == 'RNA':
            for x in seq:
                if x in RNA_dic:
                    lenght += 1
            if lenght == len(self.bio_seq):
                result = 'RNA sequence is valid.'
            else:
                result = 'RNA sequence is invalid.'               

        # Αποτέλεσμα της συνάρτησης το κατάλληλο κάθε φορά αλφαρηθμητικό.
        return(result)
            
# Δημιουργία αντικειμένου.
a = Sequence(1,'DNA','AGTAattaCCCGG',2020)

# Εκτύπωση του αποτελέσματος της validate().
print(a.validate())

            
