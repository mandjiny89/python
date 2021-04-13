##Inheritance example Family Tree

class GrandParents():
    def __init__(self):
        print("\nGrandParents class running\n") # First this method excuted
    def amma_family(self,amma_amma, amma_appa):
        self.amma_appa = amma_appa
        self.amma_amma = amma_amma
        print(f"My patti name {amma_amma}, her dad name {amma_appa}\n")
    def appa_family(self,appa_appa, appa_amma):
        self.appa_appa = appa_appa
        self.appa_amma = appa_amma
        """If I call a variable from another method I have to use self and the variable name, but if I'm calling a variable from 
        same method we can simply call the variable without self"""
        print(f"My tatha name {appa_amma} his dad name {appa_appa} and their Samanthi's are {self.amma_amma} and {self.amma_appa}\n")
### The same function name used in this function and MyFamily function but can generate different values when called
    def current_city(self,city):
        self.city = city
        print(f"Current city of my Dad's parents living in {city}")

class MyParents(GrandParents):
    def __init__(self):
        GrandParents.__init__(self) # First this method excuted and printed when we call MyParents
        print("My Parents class running \n") 
    def sub_tree_1(self,appa,amma):
        self.appa = appa
        self.amma = amma
        print(f"My amma name is {amma} and my appa name is {appa}\n")

class MyFamily(MyParents):
    def __init__(self):
        MyParents.__init__(self)
        print("My Family Class running\n")
    def sub_tree_2(self,me,wife,son):
        self.me = me
        self.wife = wife
        self.son = son
        print(f"This is my name{me}, my wife name is {wife} and my son name is {son}\n")
    def current_city(self,city):
        self.city = city
        print(f"we are living in {city}, running from MyFamily class")

base_tree = MyFamily()
# base_tree.amma_family("Jayalaskshmi", "Jayakkannu")
# base_tree.appa_family("Thiru", "Viruthambal")
# base_tree.sub_tree_1("Mandjiny", "Mangalakshmi")
# base_tree.sub_tree_2("Pat","Calai","Dhruv")
base_tree.current_city("Milton Keyens")
base_tree_2 = GrandParents()
base_tree_2.current_city("Pondicheery")

