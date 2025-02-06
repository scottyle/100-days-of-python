#How to create your own Class in Python
class User: #PascalCase for Classes 
    """Remember that when you add parameters to the constructor you're saying that whenever a new object is being constructed 
    from this class it must provide these parameters""" 
    def __init__(self,user_id, username):
        #Basically everytime you create a new object from this class this init function will be called 
        print("new user being created...")
        #How do we set attributes in the constructor? 
        self.user_id = user_id
        #Its convention to have the name of the parameter be equal to the name of the attribute 
        self.username = username
        #Sometimes when creating our attributes we want a default value to start with to be modified later for example
        #How do we do this? We just set it to a default value 
        self.followers = 0 
        self.following = 0 
        #Lets create a method, unlike a function a method always needs to have a self parameter as the first parameter 
        #The reason for this is so the method knows what object called it 

    def follow(self, user):
        user.followers += 1
        #This self means that the refers to the object that is calling this function 
        self.following += 1 

user_1 = User("001","scott") #Everything else are usually named as snake_case 
user_2 = User("002","jack")

user_1.follow(user_2)
print(f"User2: {user_2.following}")
print(f"User2: {user_2.followers}")
print(f"User1: {user_1.following}")
print(f"User1: {user_1.followers}")

"""This is validate if we wanted to create an object but its prone to error due to typos. 
So what can we do... constructors, which is apart of the blueprint(class) when the object is constructed this is known 
as the object being intitialized.
We could create the constructor by using a special function which is the init function 
Ex.
class Car:
    def __init__(self):
    #initialise the attributes
This init function is used to initialize the attributes 
"""




"""
Adding methods to classes remember attributes at the things the object has and the methods are the things the object does
Class Car():
    def enter_race_mode():
        self.seats = 2 
"""