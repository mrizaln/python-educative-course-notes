# Information Hiding

    # Information hiding refers to the concept of hiding the inner workings of a class and simply providing an interface 
    # through which the outside world can interact with the class without knowing what’s going on inside.

    # The purpose is to implement classes in such a way that the instances (objects) of these classes should not be able 
    # to cause any unauthorized access or change in the original contents of a class.

## Components of data hiding
    # 1. Encapsulation
        # Encapsulation in OOP refers to binding data and the methods to manipulate that data together in a single unit,
        # that is, class.

        # When encapsulating classes, a good convention is to declare all variables of a class private.
        # This will restrict direct access by the code outside that class.

        # One has to implement public methods to let the outside world communicate with this class. These methods are 
        # called getters and setters. We can also implement other custom methods.

        # Advantages of encapsulation
            # Classes make the code easy to change and maintain.
            # Properties to be hidden can be specified easily.
            # We decide which outside classes or functions can access the class properties.

        # Getter and setter
            # A getter method allows reading a property’s value.
            # A setter method allows modifying a property’s value.

class User:
    def __init__(self, username = None):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setUsername(self, x):
        self.__username = x


steve = User('Steve')
print("Before setting:", steve.getUsername())
steve.setUsername('Steven')
print("After setting :", steve.getUsername())
print()
    
    # 2. Abstaction

# =================================================================================================================
# Encapsulation Example: login credentials

class User:
    def __init__(self, username = None, password = None):
        self.__username = username
        self.__password = password

    def login(self, username, password):
        if (self.__username.lower() == username.lower()) and (self.__password == password):
            print("Access Granted for usename:", username)
        else:
            print("Invalid Credentials!")


steve = User('steven', 12345)

steve.login('steve', 21343)
steve.login('steve', 12345)
steve.login('steven', 12345)

steve.__password  # bakal error pas execute