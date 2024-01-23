#Πρώτη περίπτωση όπου περιλαμβάνεται στους αριθμούς μόνο ο x και όχι ο y
def printMulti(x,y):
    if x>y:
        print('Λάθος')
    else:
        for i in range (x,y):
            if i%2 !=0:
              print(i)   


#Δεύτερη περίπτωση όπου περιλαμβάνονται στους αριθμούς και τα όρια(x και y)
def printMulti(x,y):
    if x>y:
        print('Λάθος')
    else:
        for i in range (x,y+1):
            if i%2 !=0:
              print(i)      
                
#Τρίτη περίπτωση όπου δεν περιλαμβάνονται στους αριθμούς τα όρια
def printMulti(x,y):
    if x>y:
        print('Λάθος')
    else:
        for i in range (x+1,y):
            if i%2 !=0:
              print(i)               
#Even number
i%2 ==0
print('even number') 
