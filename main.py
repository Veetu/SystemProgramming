from student import Student

sdnt1 = Student("Meikä", "Manne", "tvt18")
sdnt2 = Student("Daniel", "Manninen", "kto17")
sdnt3 = Student("Valtsu", "Kirsula", "kto16")
sdnt4 = Student("Arttu", "Heikkinen", "tvt18")
sdnt5 = Student("Ollo", "Simp", "tvt17")
sdnt6 = Student("Agile", "Jondo", "kto19")

list = [sdnt1, sdnt2, sdnt3, sdnt4, sdnt5, sdnt6]

for obj in list:
    print(obj.info())