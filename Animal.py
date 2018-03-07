# Animal Class
class Animal(object):
    # Attributes: name, health
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    # Methods:
    
    # walk: decreases health by one
    def walk(self):
        self.health -= 1
        return self

    # run: health decreases by five
    def run(self):
        self.health -= 5
        return self
    
    # display health: print to the terminal the animal's health.
    def displayHealth(self):
        print (self.name + " Health: " + str(self.health) )
        print (' ')
        return self

# Create an instance of the Animal...
cat = Animal( 'Whiskers', 100)
#...have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed.
cat.walk().walk().walk().run().run().displayHealth()


# Dog Class: inherits everything from Animal
class Dog(Animal):
    # Attributes: default health of 150
    # I interpreted the above instruction as passing 150 as initial health when creating an instance of dog.
    # However, the code block below, when uncommented, will force an initial value of 150 for health regardless of the value passed.
    # def __init__(self, name, health):
    #     Animal.__init__(self, name, health)
    #     self.health = 150
    
    # Methods:
    
    # pet: increases health by 5
    def pet(self):
        self.health += 5
        return self

# Have the Dog...
Boxer = Dog('Rex', 150)
# walk() three times, run() twice, pet() once, and have it displayHealth().
Boxer.walk().walk().walk().run().run().pet().displayHealth()

# Dragon Class: inherits everything from Animal
class Dragon(Animal):
    # Attributes: default health of 170
    # As with Dog, the code block below will force the specified value for health, regardless of the value passed by a user during instance creattion
    # def __init__(self, name, health):
    #   Animal.__init__(self, name, health)
    #   self.health = 170
    
    # Methods:
    
    # fly: decreases health by 10
    def fly(self):
        self.health -= 10

    # display health: prints health by calling the parent method and prints "I am a Dragon"
    def displayHealth():
        print ('I am a Dragon!')
        super(Dragon).displayHealth()

# Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and its displayHealth() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().

Porcupine = Animal('Spine', 100)

if not hasattr( Porcupine, 'fly' ):
    print 'Porcupines cannot fly()'
if not hasattr( Porcupine, 'pet'):
    print "Porcupines can't be pet()"
Porcupine.displayHealth()
print "Porcupines aren't dragons."

