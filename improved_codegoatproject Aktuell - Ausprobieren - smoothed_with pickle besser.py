import pickle
import os

office_list = []
dict_employees = {}






class Office: 

    def __init__(self, office_name, capacity):
        self.office_name = office_name
        self.Monday = self.set_places(capacity)
        self.Tuesday = self.set_places(capacity)
        self.Wednesday = self.set_places(capacity)
        self.Thursday = self.set_places(capacity)
        self.Friday = self.set_places(capacity)
        self.Saturday = self.set_places(capacity)
        self.Sunday = self.set_places(capacity)

    def set_places(self, capacity):                 
        seats_in_office = [None] * int(capacity)
        return seats_in_office
    
    def get_empty_places(self, weekday):
        if weekday == 1:
            empty_places = self.Monday.count(None)
            return empty_places
        if weekday == 2:
            empty_places = self.Tuesday.count(None)
            return empty_places
        if weekday == 3:
            empty_places = self.Wednesday.count(None)
            return empty_places
        if weekday == 4:
            empty_places = self.Thursday.count(None)
            return empty_places
        if weekday == 5:
            empty_places = self.Friday.count(None)
            return empty_places
        if weekday == 6:
            empty_places = self.Saturday.count(None)
            return empty_places
        if weekday == 7:
            empty_places = self.Sunday.count(None)
            return empty_places
        
    def make_reservation(self, name, weekday):
        if weekday == 1:
            for i, element in enumerate(self.Monday):
                if element is None:
                    self.Monday[i] = name
                    break
                if self.Monday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Monday
        if weekday == 2:
            for i, element in enumerate(self.Tuesday):
                if element is None:
                    self.Tuesday[i] = name
                    break
                if self.Tuesday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Tuesday
        if weekday == 3:
            for i, element in enumerate(self.Wednesday):
                if element is None:
                    self.Wednesday[i] = name
                    break
                if self.Wednesday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Wednesday
        if weekday == 4:
            for i, element in enumerate(self.Thursday):
                if element is None:
                    self.Thursday[i] = name
                    break
                if self.Thursday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Thursday
        if weekday == 5:
            for i, element in enumerate(self.Friday):
                if element is None:
                    self.Friday[i] = name
                    break
                if self.Friday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Friday
        if weekday == 6:
            for i, element in enumerate(self.Saturday):
                if element is None:
                    self.Saturday[i] = name
                    break
                if self.Saturday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Saturday
        if weekday == 7:
            for i, element in enumerate(self.Sunday):
                if element is None:
                    self.Sunday[i] = name
                    break
                if self.Sunday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Sunday

    def cancel_reservation(self, name, weekday):
        if weekday == 1:
            for i, element in enumerate(self.Monday):
                if element == name:
                    self.Monday[i] = None
                    break
                if name not in self.Monday:       
                    print('The office is full!')
                    break
            return self.Monday
        if weekday == 2:
            for i, element in enumerate(self.Tuesday):
                if element == name:
                    self.Tuesday[i] = None
                    break
                if name not in self.Tuesday:       
                    print('The office is full!')
                    break
            return self.Tuesday
        if weekday == 3:
            for i, element in enumerate(self.Wednesday):
                if element == name:
                    self.Wednesday[i] = None
                    break
                if name not in self.Wednesday:       
                    print('The office is full!')
                    break
            return self.Wednesday
        if weekday == 4:
            for i, element in enumerate(self.Thursday):
                if element == name:
                    self.Thursday[i] = None
                    break
                if name not in self.Thursday:       
                    print('The office is full!')
                    break
            return self.Thursday
        if weekday == 5:
            for i, element in enumerate(self.Friday):
                if element == name:
                    self.Friday[i] = None
                    break
                if name not in self.Friday:       
                    print('The office is full!')
                    break
            return self.Friday
        if weekday == 6:
            for i, element in enumerate(self.Saturday):
                if element == name:
                    self.Saturday[i] = None
                    break
                if name not in self.Saturday:       
                    print('The office is full!')
                    break
            return self.Saturday
        if weekday == 7:
            for i, element in enumerate(self.Sunday):
                if element == name:
                    self.Sunday[i] = None
                    break
                if name not in self.Sunday:       
                    print('The office is full!')
                    break
            return self.Sunday

    def get_office_name(self):
        return self.office_name



def create_offices():
    office_name = input("\n\nIn which city is the new office located?\nEnter your answer as follows: e.g. for St.Gallen --> St.Gallen\n==> ")
    office_capacity = int(input("\nHow many workplaces are available in this office? Enter your answer as follows: e.g. for 7 workplaces --> 7\n==> "))
    office_list.append(Office(office_name, office_capacity))
    


def add_employee():
    key = int(input("\n\nCreate a unique ID for the new employee consisting of 4 numbers.\nEnter the ID as follows: e.g. for ID 1234 --> 1234\n==> "))
    value = input("\nNow assign the new employee his first name.\nEnter the first name as follows: e.g. for Robert --> Robert\n==> ")
    dict_employees[key] = value
    return dict_employees




def choice_1(office, name, weekday):
    print(office.make_reservation(name, weekday))
    print(f"Remaining places: {office.get_empty_places(weekday)}")
    

def choice_2(office, name, weekday):
    office.cancel_reservation(name, weekday)
    office.get_empty_places(weekday)
    

def ID_input():
    print("\nWelcome to the office reservation system.")
    while True:
        ID_employee = int(input("To start, please enter your personal ID: "))
        if ID_employee in dict_employees.keys():
            break 
        else:
            print("Given ID not found")
    return dict_employees[ID_employee]


def location_office_input():
    while True:
        user_input_office = input('Which office in which city?: ')
        for element in office_list:
            if element.get_office_name() == user_input_office:
                return user_input_office        
        print("Given input not found")


def Weekday_input():
    while True:
        Weekday = int(input("Please enter weekday: "))
        if 1 <= Weekday <= 7:
            return Weekday
        else:
            print("Invalid input, insert an integer number between 1 and 7")



def main():

    global office_list
    global dict_employees

    if os.path.exists("office_list_storage.pickle"):
        with open("office_list_storage.pickle", 'rb') as file:
            office_list = pickle.load(file)
            print("Office list has been loaded")

    else:
        with open("office_list_storage.pickle", 'wb') as file:
            pickle.dump(office_list, file)
            print("Office list has been created")


    if os.path.exists("dict_employees_storage.pickle"):
        with open("dict_employees_storage.pickle", "rb") as file:
            dict_employees = pickle.load(file)
            print("Employees dictionary has been loaded")

    else:
        with open("dict_employees_storage.pickle", "wb") as file:
            pickle.dump(dict_employees, file)
            print("Employees dictionary has been created")


    while True:
        print("\n\nWelcome to Office'er, valantic's internal application that helps employees managing their office.\n\nPlease choose below what you want to do.")
        print("1. Workplace reservation")
        print("2. Cancel workplace reservation")
        print("3. Request number of available workplaces")
        print("4. Add new employee (only possible for administrator)")
        print("5. Add new office (only possible for administrator)")
        print("6. Exit")
        print(" ")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = ID_input()
            location = location_office_input()
            weekday = Weekday_input()
            office_found = False
            for office in office_list:
                name_1 = office.get_office_name()
                if name_1 == location:
                    choice_1(office, name, weekday)
                    office_found = True
                    break
            if office_found == False:
                print("This office does not exist")
        
        elif choice == '3':
            name = ID_input()
            location = location_office_input()
            weekday = Weekday_input()
            for office in office_list:
                name_1 = office.get_office_name()
                if name_1 == location:
                    print(f"Remaining seats: {office.get_empty_places(weekday)}")
                    office_found = True
                    break
            if office_found == False:
                print("This office does not exist")
                
        elif choice == '2':
            name = ID_input()
            location = location_office_input()
            weekday = Weekday_input()
            office_found = False
            for office in office_list:
                name_1 = office.get_office_name()
                if name_1 == location:
                    choice_2(office, name, weekday)
                    office_found = True
                    break
            if office_found == False:
                print("This office does not exist")
        
        elif choice == '4':
            add_employee()
        

        elif choice == '5':
            create_offices()
            print(office_list)

        elif choice == '6':
            print("Exiting the program.")
            with open("office_list_storage.pickle", 'wb') as file:
                pickle.dump(office_list, file)
                print("Office list has been saved")

            with open("dict_employees_storage.pickle", "wb") as file:
                pickle.dump(dict_employees, file)
                print("Employees dictionary has been saved")
            
            break

        else:
            print("Invalid choice. Please enter a valid number (1-6).")



main()








