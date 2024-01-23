class Triangle:

    def __init__(self, angles):
        self.angles = angles
        Triangle.number_of_sides = 3

    def check_angles(self):
        s = 0
        for i in self.angles:
            s += i

        if s == 180:
            return True
        else:
            return False


triangleX = Triangle([20 ,30 ,40])

print('Ο αριθμός των πλευρών του είναι:', triangleX.number_of_sides,
      '\nEίναι το άθροισμα των γωνιών 180 μοίρες;', triangleX.check_angles())
      
        
    
    
