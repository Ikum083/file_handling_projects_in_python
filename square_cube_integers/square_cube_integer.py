# square all even integers and cube all odd integers
# setup main class
class SquareCube():
## setup main method
    def __init__(self):
### list to contain every number in the text file
        self.numbers = []
        self.even_numbers = []
        self.odd_numbers = []
        self.squared_numbers = []
        self.cubed_numbers = []
### open file iterating every line on the file
        with open("square_cube_integers/integers.txt", "r") as integers:
            for line in integers:
                self.numbers.append(line)
### seperate every number in the file if they're even or odd
        for i in self.numbers:
            if int(i) % 2 == 0:
                self.even_numbers.append(int(i))
            else:
                self.odd_numbers.append(int(i))
        print(self.even_numbers)
        print(self.odd_numbers)
### square every even number and cube every odd number
        for j in self.even_numbers:
            squared_num = j ** 2
            self.squared_numbers.append(squared_num)
        for k in self.odd_numbers:
            cubed_num = k ** 3
            self.cubed_numbers.append(cubed_num)
        print(self.squared_numbers)
        print(self.cubed_numbers)
### input the perspective files into their rightful text file

if __name__ == "__main__":
    SquareCube()
