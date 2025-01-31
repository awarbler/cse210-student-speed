import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    """A nutritious substance that snake's like. The responsibility of Food is to keep track of its appearance and position. A Food can move around randomly if asked to do so. 
    
    Stereotype:
        Information Holder
    Attributes: 
        _points (integer): The number of points the food is worth.


        Attributes of actor 
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    """

    def __init__(self):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the food to a random position within the boundary of the 
        screen.
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self._points = 0 # sets the points 
        self.set_text(random.choice(constants.LIBRARY))
        self.reset()


    
    def get_points(self):
        """Gets the points this word is worth.
        
        Args:
            self (Food): an instance of Food.
        Returns:
            integer: The points this food is worth.
        """
        return self._points

    def get_text(self):
        pass

    def check_word(self, word):
        #loop through the range of words
        # set text equal to self.checkWord at current index
        # if letter. get_letter() is equal to word
            # call the set points funtion and pass the current word
            # set the current word to a new random word 
            # return points
        #return 0
        return self.set_text == word

    def reset(self):
        """Resets the word by moving it to a random position within the boundaries of the screen and reassigning the points to a random number.
        
        Args:
            self (Food): an instance of Food.
        """
        self.set_text(random.choice(constants.LIBRARY)) # get word from constants Library
        self._points = random.randint(1, 5)
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x, y)
        self.set_position(position)