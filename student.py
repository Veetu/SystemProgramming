class Student:
    def __init__(self, fname, lname, stGroup):
        self.fname = fname
        self.lname = lname
        self.stGroup = stGroup

    def info(self):
        print(" "+ self.fname, self.lname+ " belongs to group "+ self.stGroup)
