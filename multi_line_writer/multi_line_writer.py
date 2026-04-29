# multi line writer in python
# boolean to control the while loop
asking_user = True

# while loop that will iterate until the user says to stop
class LineWriter():
    def __init__(self):
        while asking_user:
            ## ask user for their input 
            self.user_input = str(input("Enter line: "))
            ## put the input into a text file named "mylife.txt"
            self.WriterFile = open("mylife.txt", "w")
            self.WriterFile.write(f"{self.user_input}\n")
            self.WriterFile.close()
            ## ask user if to continue or stop
            self.stop_or_continue_loop = str(input("Are there more lines y/n? "))

if __name__ == "__main__":
    LineWriter()





