#Note for classes use PascalCase naming convention, first letter capitalized 
#We use PascalCase and snake_case naming conventions 

"""
How can i specify all these starting variables? Constructors 
When a object is being initialized we can set variables or counters to their starting values 
We do this by using the init function which is a special function that is used to initialize attributes 

Attributes are the things an object will have... how do we set the attribute in the init function 
Note that when we specify these two attributes that means whenever we call this object it will require two parameters 
"""

class User:

    def __init__(self, user_id, username) -> None:
    #Basically whats going on is that when the object User is being created we will pass in the user_id and this user_id will be equal to the attribute of id
    #Normal convention is that you will see the name of the parameter to be the name of the attribute 
        self.id = user_id
        self.username = username
        #Default value for an attribute 
        self.followers = 0 
        self.following = 0

    #Unlike a function a method always needs to have a self parameter as the first parameter, because when you call this method it will know what object called it 
    def follow(self, user):
        user.followers += 1 
        self.following += 1 


# user_1 = User() 
# user_1.id = "001"
# user_1.username = "Scott"

# print(user_1.id)

user_1 = User("001","Scott")
user_2 = User("002", "test")

user_1.follow(user_2)
breakpoint()

"""
Adding methods to a class - the things that the object does 
Remember when a function is attached to an object it is called a method 
"""


