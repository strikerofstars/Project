

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





# implement office to the system
#office_stgallen = Office("St.Gallen", 5)            # different names of the variables (old code has other variables)
#office_zurich = Office("Zurich", 10)
#office_bern = Office("Bern", 12)

office_list = []

def create_offices():
    office_name = input("\n\nIn which city is the new office located?\nEnter your answer as follows: e.g. for St.Gallen --> St.Gallen\n==> ")
    office_capacity = int(input("\nHow many workplaces are available in this office? Enter your answer as follows: e.g. for 7 workplaces --> 7\n==> "))
    office_list.append(Office(office_name, office_capacity))
    return office_list


dict_employees = {}  

def add_employee():
    #while True:
    key = int(input("\n\nCreate a unique ID for the new employee consisting of 4 numbers.\nEnter the ID as follows: e.g. for ID 1234 --> 1234\n==> "))
    value = input("\nNow assign the new employee his first name.\nEnter the first name as follows: e.g. for Robert --> Robert\n==> ")
    dict_employees[key] = value
    #break
    return dict_employees




"""
office_SG = Office("St.Gallen", 5)
office_ZH = Office("Zurich", 10)
office_BE = Office("Bern", 12)

#list of office objects
office_list = [office_SG, office_ZH, office_BE]
"""









#office_names_list = [office.get_office_name() for office in office_list]




def choice_1(office, name, weekday):
    print(office.make_reservation(name, weekday))
    print(f"Remaining places: {office.get_empty_places(weekday)}")
    #output_string = f"Reservation made: {reservation_output}\nEmpty places: {empty_places}\n"
    #with open("reservation_final2026.txt", "a") as file:
        #file.write(output_string)
    #return reservation_output



def choice_2(office, name, weekday):
    office.cancel_reservation(name, weekday)
    office.get_empty_places(weekday)
    #output_string = f"Reservation made: {reservation_output}\nEmpty places: {empty_places}\n"
    #with open("reservation_final2026.txt", "a") as file:
       # file.write(output_string)





# retrieve names from the offices and put them in a separate list


# employees of the company
#employees_list = ["Louis", "Andrin", "Nik", "Severin", "Nikola"]

def ID_input():
    print("\nWelcome to the office reservation system.")
    while True:
        ID_employee = int(input("To start, please enter your personal ID: "))
        if ID_employee in dict_employees.keys():
            break 
        else:
            print("Given ID not found")
    return dict_employees[ID_employee]
    #return new_name


def location_office_input():
    while True:
        user_input_office = input('Which one?: ')
        if user_input_office in office_list:
            break
        else:
            print("Given Location not found")
    return user_input_office

"""
def location_office_input(ID_employee):

    # Create a dictionary to map lowercase office names to their original form
    office_names_dict = {item.lower(): item for item in office_names_list}

    while True:
        office_list_str = ", ".join(office_names_list)
        print(f"\n{ID_employee}, select your office location to make a reservation.\nChoose between: {office_list_str}.")
        office = input()
        office_lower = office.lower()
        if office_lower in office_names_dict:
            print(f"\nThank you for joining the office in {office_names_dict[office_lower]}!\nWe have returned you to the menu.")
            user_input_office = office_names_dict[office_lower]
            break
        else:
            print("\nOffice not found!")
    return user_input_office
"""


def Weekday_input():
    while True:
        Weekday = int(input("Please enter weekday: "))
        if 1 <= Weekday <= 7:
            return Weekday
            
        else:
            print("Invalid input, insert an integer number between 1 and 7")


def main():

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
            
        #for office in office_list:
                #print(f"{office.get_office_name()} : {office.get_empty_places()} seats available")
                

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

        
        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-4).")


main()







