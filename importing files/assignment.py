from date import Date

class Assignment:

    def __init__(self):
        self.name = "Untitled"
        self.start = Date()
        self.due = Date()
        self.end = Date()

    def prompt(self):
        self.name = input("Name: ")
        print("\nStart Date:")
        self.start.prompt()
        print("\nDue Date:")
        self.due.prompt()
        print("\nEnd Date:")
        self.end.prompt()
    
    def display(self):
        print(f"\nAssignment: {self.name}")
        print("Start Date:")
        self.start.display()
        print("Due Date:")
        self.due.display()
        print("End Date:")
        self.end.display()