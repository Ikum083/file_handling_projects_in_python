# odd even seperator
# setup main class
class MainApp():
    def __init__(self):
        # make sure the text files are clear
        open("odd_even_seperator/numbers.txt", "w").close()

        # list to contain every integer
        self.integers = []
        self.even_integers = []
        self.odd_integers = []

# ask user to input numbers
        for i in range(20):
            self.user_input = input("Enter a number: ")
            self.integers.append(self.user_input)

# put all the inputs in a text file 
        for j in self.integers:
            self.mainFile = open("odd_even_seperator/numbers.txt", "a")
            self.mainFile.write(f"{j}\n")
            self.mainFile.close()

# program to read all the numbers in the text file and seperate them to an odd or even text files
        self.mainFile = open("odd_even_seperator/numbers.txt", "r")
        for line in self.mainFile:
            print(line)
            if int(line) % 2 == 0:
                self.even_integers.append(line.replace("\n", ""))
            elif int(line) % 2 != 0:
                self.odd_integers.append(line.replace("\n", ""))
            else:
                continue

        print(self.even_integers)
        print(self.odd_integers)

if __name__ == "__main__":
    MainApp()