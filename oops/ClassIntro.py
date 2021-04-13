class MyHome():
    # Class Object Attribute
    # It will be available when we call the Class
    owner = 'Dhruv'

    def __init__(self,address,people_count):
        #Attributes, we take in the argument and assign it using self.attribute_name
        self.address = address
        self.people_count = people_count
        print(self.people_count)
        print(self.address)
        print("################################################################")

    def owner_parents(self,mom,dad):
        self.mom = mom
        self.dad = dad
        self.owner = MyHome.owner # here I referenced the Class object attribute with the Class name, we can call self.owner but to distiguish it's the Class object Attribute, I defined directly
        print(f"We are are family Amma {mom}, Appa {dad}, paiyan {MyHome.owner}!!!!")
        print(f"Our home address is {self.address} and we are count of {self.people_count} people")

# First I am setting the class to a variable and with the variable calling the method and passing the values required for the method. 
# Now I can use the variable assinged to class to use the values of the Class and Method
home = MyHome("7 Butcher Crescent",3)
home.owner_parents('Calai','Pat')
dad = home.dad
mom = home.mom
print(dad)
print(mom)


# pr = home.owner
# print(pr)


