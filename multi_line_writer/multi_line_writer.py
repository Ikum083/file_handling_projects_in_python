# multi line writer in python
# while loop that will iterate until the user says to stop
class LineWriter():
    def __init__(self):
        # boolean to control the while loop
        self.asking_user = True
        while self.asking_user:
            ## ask user for their input 
            self.user_input = str(input("Enter line: "))
            ## put the input into a text file named "mylife.txt"
            self.WriterFile = open("multi_line_writer/mylife.txt", "a")
            self.WriterFile.write(f"{self.user_input}\n")
            ## ask user if to continue or stop
            self.stop_or_continue_loop = str(input("Are there more lines y/n? "))
            if self.stop_or_continue_loop.lower() == 'n':
                self.asking_user = False

        self.WriterFile.close()
if __name__ == "__main__":
    LineWriter()





