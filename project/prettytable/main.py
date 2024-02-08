# from turtle import Turtle, Screen
#
# tommy = Turtle()
# print(tommy)
#
#
# tommy.shape("turtle")
# tommy.color("cyan3")
# tommy.forward(200)
#
# tommy_screen = Screen()
#
# print(tommy_screen.canvheight)
# tommy_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","squirt","Charmender"])
table.add_column("Power",["elctric","water","fire"])
table.align["Pokemon Name"] = "l"
table.align["Power"] = "l"

print(table)
