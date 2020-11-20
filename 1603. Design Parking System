class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big;
        #print (self.big)
        self.medium = medium;
        #print (self.medium)
        self.small = small;
        #print (self.small)
    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        #print (carType)
        if carType == 1:
            self.big = self.big-1 
            #print (self.big)
            if self.big < 0:
                return False
            return True
        
        elif carType == 2:
            self.medium = self.medium-1
            if self.medium < 0:
                return False
            return True
        
        elif carType == 3:
            self.small = self.small-1
            if self.small < 0:
                return False
            return True

        
      
        
        
        
        
            
            
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
