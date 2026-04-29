# square all even integers and cube all odd integers
# setup main class
class SquareCube():
## setup main method
    def __init__(self):
### list to contain every number in the text file
        self.numbers = []
### open file iterating every line on the file
        with open("square_cube_integers/integers.txt", "r") as integers:
            for line in integers:
                self.numbers.append(line)
### seperate every number in the file if they're even or odd
### square every even number and cube every odd number
### input the perspective files into their rightful text file
