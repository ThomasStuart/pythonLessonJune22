# Fitness Data Class.
# Create a class that has the properties:
#   1.) name          (Constructor set)
#   2.) step count
#   3.) height        (Constructor set)
#   4.) miles walked.
#

class FitnessData:

    def __init__(self, name, height):
        self.name       = name
        self.stepCount  = 0
        self.height     = height
        self.mileWalked = 0


    def addSteps(self, moreSteps):
        self.stepCount = self.stepCount + moreSteps
        #print("currentSteps==", self.stepCount)

    def getMiles(self):
        #  m = 1/2 height * stepCount
        self.miles = self.stepCount / (1/4 * self.height)
        return self.miles
#END CLASS


#object1
object1 = FitnessData("Joe", 6.0)
# add 500 steps to object1 using the addSteps class function
object1.addSteps(500)
# print the current number of steps
print("object1--step count: ",  object1.stepCount )

#object2
object2 = FitnessData("Tom", 8.0)
object2.addSteps(1000)
print( "object2-- getMiles(): ", object2.getMiles() )