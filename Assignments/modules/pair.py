## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##   
##   CS 234 code download
##   Version date: March 2022
##   File name: pair.py
##   
## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##
class Pair:
    """
    Fields: first (Any), second (Any) 

    """

    def __init__(self, f, s):
        """
        Pair(f, s) produces a Pair with first f and second s.
        Effects: Creates a new Pair.
        __init__: Any Any -> Pair

        """
        self.first = f
        self.second = s

    def __repr__(self):
        """
        repr(self) produces a string representing self.
        __repr__: Pair -> Str

        """        
        return "Pair(First = " + str(self.first) + ", Second = " +  \
        str(self.second) + ")"

    def pair_first(self):
        """
        self.pair_first() produces the first of self.
        pair_first: Pair -> Any

        """        
        return self.first

    def pair_second(self):
        """
        self.pair_second() produces the second of self.
        pair_second: Pair -> Any

        """        
        return self.second
    
    def __contains__(self, value):
        """
        value in self produces True if value is first or second.
        __contains__: Pair Any -> Bool

        """
        return value == self.first or value == self.second

    def add_first(self, data):
        """
        self.add_first(data) replaces first with data.
        Effects: Mutates self by replacing first with data.
        add_first: Pair Any -> None

        """
        self.first = data

    def add_second(self, data):
        """
        self.add_second(data) replaces second with data.
        Effects: Mutates self by replacing second with data.
        add_second: Pair Any -> None

        """
        self.second = data

    def __eq__(self, other):
        """
        self == other produces True if self and other have equal first and
            second fields.
        __eq__: Pair Pair -> Bool

        """
        return self.first == other.first and self.second == other.second

    

