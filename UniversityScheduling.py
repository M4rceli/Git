
import random as rnd
import pandas as pd
class Professor:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def get_id(self): return self._id
    def get_name(self): return self._name
    def __str__(self): return self._name
        
class Room:
    def __init__(self, id, name, lab, building):
        self._id = id
        self._name = name
        self._lab = lab
        self._building = building
    def get_id(self): return self._id
    def get_name(self): return self._name
    def get_lab(self): return self._lab
    def get_building(self): return self._building
    
class MeetingTime:
    def __init__(self, id, time):
        self._id = id
        self._time = time
    def get_id(self): return self._id
    def get_time(self): return self._time


class Data:
    ROOMS = [["R1", "F1", "0", "B14"], ["R2", "F2", "0", "B15"], ["R3", "F3", "0", "B15"], ["R7", "Lab1", "1", "B15"]]
    MEETING_TIMES = [["MON_01", "8:00-9:00"], ["MON_02", "9:00-10:00"], ["MON_03", "10:00-11:00"], ["TUE_01", "8:00-9:00"], ["TUE_02", "9:00-10:00"], ["TUE_03", "10:00-11:00"]]
    PROFESSORS = [["P01", "Wojciech Kryszewski"],
                ["P02", "Agnieszka Drwalewska"],
                ["P03", "Włodzimierz Fechner"],
                ["P04", "Marek Galewski"],
                ["P05", "Filip Strobin"],
                ["P06", "Michał Karbowańczyk"],
                ["P07", "Daniel Arendt"],
                ["P08", "Adam Bryszewski"],
                ["P09", "Błażej Dziuba"], 
                ["P10", "Roman Krasiukianis"],
                ["P11", "Jacek Rogowski"], 
                ["P12", "Szymon Głąb"], 
                ["P13", "Henryk Dębiński"],
                ["P14", "Marek Bienias"]]
    def __init__(self):
        self._rooms = []; self._meetingTimes = []; self._professors = []
        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1], self.ROOMS[i][2], self.ROOMS[i][3]))
        for i in range(0, len(self.MEETING_TIMES)):
            self._meetingTimes.append(MeetingTime(self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1]))
        for i in range(0, len(self.PROFESSORS)):
            self._professors.append(Professor(self.PROFESSORS[i][0], self.PROFESSORS[i][1]))
        course1 = Course("C01", "Analiza matematyczna I (wykład)", [self._professors[0]], "Lecture", 60)
        course2 = Course("C02", "Analiza matematyczna I (ćwiczenia)", [self._professors[1], self._professors[2], self._professors[3]], "Exercise", 60)
        course3 = Course("C03", "Algebra liniowa z geometrią analityczną I (wykład)",[self._professors[4]] , "Lecture", 30)
        course4 = Course("C04", "Algebra liniowa z geometrią analityczną I (ćwiczenia)",[self._professors[4]] , "Excercise", 30)
        course5 = Course("C05", "Technologie informatyczne I (laboratorium)", [self._professors[5], self._professors[6], self._professors[7], self._professors[8], self._professors[9]], "Laboratory", 45)
        course6 = Course("C06", "Wstęp do obliczeń symbolicznych (laboratorium)",[self._professors[10]] , "Laboratory", 30)
        course7 = Course("C07", "Wstęp do logiki i teorii mnogości (wykład)",[self._professors[11]] , "Lecture", 30)
        course8 = Course("C08", "Wstęp do logiki i teorii mnogości (ćwiczenia)",[self._professors[11], self._professors[13]] , "Exercise", 30)
        self._courses = [course1, course2, course3, course4, course5, course6, course7, course8]
        student1 = Students("MS01_01", [course1, course2, course3, course4, course5, course6, course7, course8])
        self._students = [student1]
        self._numberOfClasses = 0
        for i in range(0, len(self._students)):
            self._numberOfClasses += len(self._students[i].get_courses())
    def get_rooms(self): return self._rooms
    def get_professors(self): return self._professors
    def get_courses(self): return self._courses
    def get_students(self): return self._students
    def get_meetingTimes(self): return self._meetingTimes
    def get_numberOfClasses(self): return self._numberOfClasses

# Tworzenie instancji klasy Data

data = Data()
# Wyświetlanie listy pokoi
for room in data._rooms:
    print(room)

# Wyświetlanie listy czasów spotkań
for meetingTime in data._meetingTimes:
    print(meetingTime)

# Wyświetlanie listy instruktorów
for professor in data._professors:
    print(professor)
    

class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numbOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True
    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes
    def get_numbOfConflicts(self): return self._numbOfConflicts
    def get_fitness(self):
        if (self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness
    def initialize(self):
        students = self._data.get_students()
        for i in range(0, len(students)):
            courses = students[i].get_courses()
            for j in range(0, len(courses)):
                newClass = Class(self._classNumb, students[i], courses[j])
                self._classNumb += 1
                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(0, len(data.get_meetingTimes()))])
                newClass.set_room(data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])
                newClass.set_professor(courses[j].get_professors()[rnd.randrange(0, len(courses[j].get_professors()))])
                self._classes.append(newClass)
        return self
    def calculate_fitness(self):
        self._numbOfConflicts = 0
        classes = self.get_classes()
        for j in range(0, len(classes)):
            if (j >= i):
                if (classes[i].get_meetingTime() == classes[j].get_meetingTime() and
                classes[i].get_id() != classes[j].get_id()):
                    if (classes[i].get_room() == classes[j].get_room()): self._numbOfConflicts += 1
                    if (classes[i].get_instructor() == classes[j].get_instructor()): self._numbOfConflicts += 1
        return 1 / ((1.0*self._numbOfConflicts + 1))
    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes)-1):
            returnValue += str(self._classes[i]) + ", "
        returnValue += str(self._classes[len(self._classes)-1])
        return returnValue


class Department:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def get_id(self): return self._id    
    def get_name(self): return self._name

class Students:
    def __init__(self, id, courses):
        self._id = id
        self._courses = courses
    def get_id(self): return self._id
    def get_courses(self): return self._courses
    
class Subject:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def get_id(self): return self._id
    def get_name(self): return self._name
    
class Course:
    def __init__(self, id, name, professor, course_type, duration):
        self._id = id
        self._name = name
        self._professor = professor
        self._course_type = course_type
        self._duration = duration
    def get_id(self): return self._id
    def get_name(self): return self._name
    def get_professor(self): return self._professor 
    def get_course_type(self): return self._course_type
    def get_duration(self): return self._duration
  
# Students za department
class Class:
    def __init__(self, id, department, students, course):
        self._id = id
        self._department = department
        self._students = students
        self._course = course
        self._professor = None
        self._meetingTime = None
        self._room = None
    def get_id(self): return self._id
    def get_department(self): return self._department
    def get_students(self): return self._students
    def get_course(self): return self._course
    def get_professor(self): return self._professor
    def get_meetingTime(self): return self._meetingTime
    def get_room(self): return self._room
    def set_professor(self, professor): self._professor = professor
    def set_meetingTime(self, meetingTime): self._meetingTime = meetingTime
    def set_room(self, room): self._room = room
    def __str__(self): 
        return str(self._department.get_name()) + "," + str(self._students.get_name())+ "," + str(self._course.get_id()) + "," + \
               str(self._room.get_id()) + "," + str(self._instructor.get_id()) + "," + str(self._meetingTime.get_id())
    




class DisplayMgr:
    def print_available_data(self):
        print("> All Available Data")
        self.print_department()
        self.print_course()
        self.print_room()
        self.print_professor()
        self.print_meeting_times()

    def print_department(self):
        departments = data.get_departments()
        department_list = []
        for i in range(0, len(departments)):
            courses = departments.__getitem__(i).get_courses()
            tempStr = "["
            for j in range(0, len(courses) - 1):
                tempStr += courses[j].__str__() + ", "
            tempStr += courses[len(courses) - 1].__str__() + "]"
            department_list.append([departments.__getitem__(i).get_name(), tempStr])
        
        # Przekształcanie listy departamentów w ramkę danych i wyświetlanie jej
        departments_df = pd.DataFrame(department_list, columns=['Department', 'Courses'])
        print(departments_df)


'''
## tabele: Professor, Room, Department, Students, Students_group, Subject, Course, Course_Professor, MeetingTime    
import pandas as pd

# Tworzymy puste bloki czasowe
bloki_czasowe = [f"{godzina}:00-{godzina+1}:00" for godzina in range(8, 20)]

# Tworzymy ramkę danych z indeksem ustawionym na nasze bloki czasowe
plan_zajec = pd.DataFrame(index=bloki_czasowe)

# Dodajemy kolumny dla każdego dnia tygodnia
dni_tygodnia = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"]
for dzien in dni_tygodnia:
    plan_zajec[dzien] = ""  # Na początku wszystkie bloki są puste

# Wyświetlamy nasz plan zajęć
print(plan_zajec)

# Dodajemy kilka zajęć do naszego planu
plan_zajec.loc["9:00-10:00", "Poniedziałek"] = "Matematyka"
plan_zajec.loc["10:00-11:00", "Wtorek"] = "Fizyka"
plan_zajec.loc["11:00-12:00", "Środa"] = "Chemia"
plan_zajec.loc["12:00-13:00", "Czwartek"] = "Informatyka"
plan_zajec.loc["13:00-14:00", "Piątek"] = "Biologia"

print(plan_zajec)
'''