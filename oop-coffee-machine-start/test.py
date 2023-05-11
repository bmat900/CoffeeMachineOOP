# from turtle import Turtle, Screen
#
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color('blue')
# my_screen = Screen()
# timmy.forward(100)
#
#
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ['Pokemon Types', 'Type']
table.add_row(['Pikachu', 'Electric'])
table.add_row(['Squirtle', 'Water'])
table.add_row(['Charmander', 'Fire'])

table.align = 'l'
print(table)