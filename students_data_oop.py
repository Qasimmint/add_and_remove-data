import csv

class DataBase:
    def __init__(self):
        self.lst = []
        self.f_names = ["Name", "E-mail", "Salary"]

    def addTo(self, name: str, email: str, salary: float):
        self.name = name
        self.email = email
        self.sal = salary

        # Bug: The dictionary keys should match the field names (self.f_names)
        # Corrected dictionary creation:
        self.data_dict = {
            "Name": name,
            "E-mail": email,
            "Salary": salary
        }

        assert isinstance(name, str) and len(name) <= 10, "Length of Name should be less than or equal to 10"
        assert isinstance(salary, float) and salary >= 5, "Salary should not be less than 5$"
        self.lst.append(self.data_dict)

    def removeFrom(self, *entries):
        for entry in entries:
            for item in self.lst:
                if item["Name"] == entry:
                    self.lst.remove(item)
                    print(f"{entry} deleted successfully!")
                    break
            else:
                print(f"The entry '{entry}' you are trying to remove is not present.")

    def save_to_csv(self):
        with open("database.csv", 'a', newline="") as file:
            save = csv.DictWriter(file, fieldnames=self.f_names)
            save.writeheader()
            save.writerows(self.lst)

    def disPlay(self):
        for i, j in enumerate(self.lst):
            print(i+1, "-->", j)

db_obj = DataBase()
db_obj.addTo("Ash", "ak6334760@gmail.com", 400.0)
db_obj.addTo("Kash", "kk6334760@gmail.com", 2200.0)
db_obj.addTo("Jash", "jk6334760@gmail.com", 1000.0)
db_obj.removeFrom("Kash")
# save  the file into CSV
db_obj.save_to_csv()
# display the updated csv file
db_obj.disPlay()
