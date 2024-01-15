import random as rnd
import pandas as pd
import prettytable as prettytable
from prettytable import PrettyTable
import sqlite3 as sqlite



POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1


class Professor:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def get_id(self): return self._id
    def get_name(self): return self._name
    def __str__(self): return self._name
    def __eq__(self, other):
        if isinstance(other, Professor):
            return self._id == other._id
        return False
    def __hash__(self):
        return hash(self._id)    
        
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
    def __eq__(self, other):
        if isinstance(other, Room):
            return self._id == other._id
        return False
    def __hash__(self):
        return hash(self._id)
class MeetingTime:
    def __init__(self, id, day, time):
        self._id = id
        self._time = time
        self._day = day
    def get_id(self): return self._id
    def get_day(self): return self._day        
    def get_time(self): return self._time
    def __eq__(self, other):
        if isinstance(other, MeetingTime):
            return self._id == other._id
        return False
    def __hash__(self):
        return hash(self._id)
class Course:
    def __init__(self, id, name, professors, course_type, duration):
        self._id = id
        self._name = name
        self._professors = professors
        self._course_type = course_type
        self._duration = duration
    def get_id(self): return self._id
    def get_name(self): return self._name
    def get_professors(self): return self._professors 
    def get_course_type(self): return self._course_type
    def get_duration(self): return self._duration
    def __str__(self): return self._name

    def __eq__(self, other):
        if isinstance(other, Course):
            return (self._id == other._id and self._name == other._name and 
                    self._professors == other._professors and self._course_type == other._course_type and 
                    self._duration == other._duration)
        return False

    def __hash__(self):
        return hash((self._id, self._name, tuple(self._professors), self._course_type, self._duration))
class Students:
    def __init__(self, id, courses):
        self._id = id
        self._courses = courses
    def get_id(self): return self._id
    def get_courses(self): return self._courses
    def __eq__(self, other):
        if isinstance(other, Students):
            return self._id == other._id
        return False
    def __hash__(self):
        return hash(self._id)
class Department:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def get_id(self): return self._id    
    def get_name(self): return self._name

    def __eq__(self, other):
        if isinstance(other, Department):
            return self._id == other._id
        return False
    def __hash__(self):
        return hash(self._id)
class Subject:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def get_id(self): return self._id
    def get_name(self): return self._name
    def __eq__(self, other):
        if isinstance(other, Subject):
            return self._id == other._id
        return False
    def __hash__(self):
        return hash(self._id)

class Class:
    def __init__(self, id,  students, course):
        self._id = id
        #self._department = department
        self._students = students
        self._course = course
        self._professor = None
        self._meetingTime = None
        self._room = None
    def get_id(self): return self._id
    #def get_department(self): return self._department
    def get_students(self): return self._students
    def get_course(self): return self._course
    def get_professor(self): return self._professor
    def get_meetingTime(self): return self._meetingTime
    def get_room(self): return self._room
    def set_professor(self, professor): self._professor = professor
    def set_meetingTime(self, meetingTime): self._meetingTime = meetingTime
    def set_room(self, room): self._room = room
    def __str__(self): 
        return str(self._students.get_id())+ "," + str(self._course.get_id()) + "," + \
               str(self._room.get_id()) + "," + str(self._professor.get_id()) + "," + str(self._meetingTime.get_id())
    def __eq__(self, other):
        if isinstance(other, Class):
            return (self._id == other._id and self._students == other._students and 
                    self._course == other._course and self._professor == other._professor and 
                    self._meetingTime == other._meetingTime and self._room == other._room)
        return False

    def __hash__(self):
        return hash((self._id, self._students, self._course, self._professor, self._meetingTime, self._room))


class DataMigration:
    def __init__(self):
        self._conn = sqlite.connect('University.db')
        self._c = self._conn.cursor()  # metoda połączenia klasy 
        self._rooms = self.select_rooms()
        self._meetingTimes = self.select_meeting_times()
        self._professors = self.select_professors()
        self._courses = self.select_courses()
        self._students = self.select_students()
        self._numberOfClasses = 0
        for i in range(0, len(self._students)):
            self._numberOfClasses += len(self._students[i].get_courses())
    def select_rooms(self):
        self._c.execute("SELECT * FROM Room")
        rooms = self._c.fetchall()  # metoda czytania query results 
        returnRooms = []
        for i in range(0, len(rooms)):
            returnRooms.append(Room(rooms[i][0], rooms[i][1], rooms[i][2], rooms[i][3]))
        return returnRooms
    def select_meeting_times(self):
        self._c.execute("SELECT * FROM MeetingTime")
        meetingTimes = self._c.fetchall()
        returnMeetingTimes = []
        for i in range(0, len(meetingTimes)):
            returnMeetingTimes.append(MeetingTime(meetingTimes[i][0], meetingTimes[i][1], meetingTimes[i][2]))
        return returnMeetingTimes
    def select_professors(self):
        self._c.execute("SELECT * FROM Professor")
        professors = self._c.fetchall()
        returnProfessors = []
        for i in range(0, len(professors)):
            returnProfessors.append(Professor(professors[i][0], professors[i][1]))
        return returnProfessors
    def select_courses(self):
        self._c.execute("SELECT * FROM Course")
        courses = self._c.fetchall()
        returnCourses = []
        for i in range(0, len(courses)):
            returnCourses.append(Course(courses[i][0], courses[i][1], self.select_course_professors(courses[i][0]), courses[i][3], courses[i][4]))
        return returnCourses
    def select_students(self):
        self._c.execute("SELECT * FROM Students")
        students = self._c.fetchall()
        returnStudents = []
        for i in range(0, len(students)):
            returnStudents.append(Students(students[i][0],  self.select_students_courses(students[i][0])))
        return returnStudents
    def select_course_professors(self, course_id):
        self._c.execute("SELECT * FROM Course_Professor where Course_ID = ?", (course_id,))
        db_professor_records = self._c.fetchall()
        professor_records = []
        for i in range(0, len(db_professor_records)):
            professor_records.append(db_professor_records[i][1])
        returnValue = []
        for i in range(0, len(self._professors)):
            if self._professors[i].get_id() in professor_records:
                returnValue.append(self._professors[i])
        return returnValue
    def select_students_courses(self, studentID):
        self._c.execute("SELECT * FROM Subject WHERE Students_ID = ?", (studentID,))
        db_subjects = self._c.fetchall()
        print(f"Wyniki dla studenta {studentID}: {db_subjects}")
        student_courses = []
        for subject in db_subjects:
            subject_id = subject[0]
            self._c.execute("SELECT * FROM Course WHERE SUBJECT_ID = ?", (subject_id,))
            courses = self._c.fetchall()
            for course in courses:
                course_obj = next((c for c in self._courses if c.get_id() == course[0]), None)
                if course_obj:
                    student_courses.append(course_obj)
        return student_courses        
    def get_rooms(self): return self._rooms
    def get_professors(self): return self._professors
    def get_courses(self): return self._courses
    def get_students(self): return self._students
    def get_meetingTimes(self): return self._meetingTimes
    def get_numberOfClasses(self): return self._numberOfClasses



data_migration = DataMigration()


rooms = data_migration.get_rooms()
professors = data_migration.get_professors()
courses = data_migration.get_courses()
meeting_times = data_migration.get_meetingTimes()
number_of_classes = data_migration.get_numberOfClasses()


print("Pokoje:", rooms)
print("Profesorowie:", professors)
print("Kursy:", courses)
print("Czasy spotkań:", meeting_times)
print("Liczba klas:", number_of_classes)


    
class Data:
    ROOMS = [["R1", "F1", "0", "B14"], ["R2", "F2", "0", "B15"], ["R3", "F3", "0", "B15"], ["R7", "Lab1", "1", "B15"]]
    MEETING_TIMES = [["MON_01", "Monday", "08:00-10:00"], ["MON_02", "Monday", "10:00-12:00"], ["MON_03", "Monday", "12:00-14:00"], ["MON_04", "Monday", "14:00-16:00"]
                     , ["TUE_01", "Tuesday", "08:00-10:00"], ["TUE_02", "Tuesday", "10:00-12:00"], ["TUE_03", "Tuesday", "12:00-14:00"], ["TUE_04", "Tuesday", "14:00-16:00"]
                     , ["WED_01", "Wednesday", "08:00-10:00"], ["WED_02", "Wednesday", "10:00-12:00"], ["WED_03", "Wednesday", "12:00-14:00"], ["WED_04", "Wednesday", "14:00-16:00"]
                     , ["THU_01", "Thursday", "08:00-10:00"], ["THU_02", "Thursday", "10:00-12:00"], ["THU_03", "Thursday", "12:00-14:00"], ["THU_04", "Thursday", "14:00-16:00"]
                     , ["FRI_01", "Friday", "08:00-10:00"], ["FRI_02", "Friday", "10:00-12:00"], ["FRI_03", "Friday", "12:00-14:00"], ["FRI_04", "Friday", "14:00-16:00"]]

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
            self._meetingTimes.append(MeetingTime(self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1], self.MEETING_TIMES[i][2]))
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
        added_courses = set()  # New set to track added courses
        for i in range(0, len(students)):
            courses = students[i].get_courses()
            for j in range(0, len(courses)):
                if courses[j] not in added_courses:  # Check if the course has not been added yet
                    newClass = Class(self._classNumb, students[i], courses[j])
                    self._classNumb += 1
                    newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(0, len(data.get_meetingTimes()))])
                    newClass.set_professor(courses[j].get_professors()[rnd.randrange(0, len(courses[j].get_professors()))])
                    if courses[j].get_course_type() == "Laboratory":
                        lab_rooms = [room for room in self._data.get_rooms() if room.get_lab() == 1]
                        if lab_rooms:
                            newClass.set_room(lab_rooms[rnd.randrange(0, len(lab_rooms))])
                        else:
                            print("No lab")
                    else:
                        newClass.set_room(self._data.get_rooms()[rnd.randrange(0, len(self._data.get_rooms()))]) 
                    self._classes.append(newClass)
                    added_courses.add(courses[j])  # Add the course to the set of added courses
        return self
    def calculate_fitness(self):
        self._numbOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            '''if (classes[i].get_room().get_seatingCapacity() < classes[i].get_course().get_maxNumbOfStudents()):
                self._numbOfConflicts += 1'''
            for j in range(0, len(classes)):
                if (j != i):
                    if classes[i].get_meetingTime() == classes[j].get_meetingTime():
                        if (classes[i].get_room() == classes[j].get_room()): self._numbOfConflicts += 1
                        if (classes[i].get_professor() == classes[j].get_professor()): self._numbOfConflicts += 1
                        if classes[i].get_students() == classes[j].get_students(): self._numbOfConflicts += 1
        return 1 / ((1.0*self._numbOfConflicts + 1))
    def __str__(self):
        if not self._classes:  # Check if the _classes list is empty
            return "No classes"
        returnValue = ""
        for i in range(0, len(self._classes)-1):
            returnValue += str(self._classes[i]) + ", "
        returnValue += str(self._classes[len(self._classes)-1])
        return returnValue

class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size): self._schedules.append(Schedule().initialize())
    def get_schedules(self): return self._schedules

class GeneticAlgorithm:
    def evolve(self, population): return self._mutate_population(self._crossover_population(population))
    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop
    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population
    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if (rnd.random() > 0.5): crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else: crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule
    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            if(MUTATION_RATE > rnd.random()): mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule
    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop
class DisplayMgr:
    def print_available_data(self):
        print("> All Available Data")
        #self.print_department()
        #self.print_course()
        #self.print_room()
        #self.print_professor()
        #self.print_meeting_times()
    def print_generation(self, population):
        table1 = prettytable.PrettyTable(['schedule #', 'fitness', '# of conflicts', 'classes [students, course, room, professor, meeting-time]'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row([str(i), round(schedules[i].get_fitness(),3), schedules[i].get_numbOfConflicts(), schedules[i].__str__()])
        print(table1)
    '''def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        classes.sort(key=lambda x: x.get_meetingTime().get_id())
        table = prettytable.PrettyTable(['Class #',  'Room', 'Professor (Id)',  'Meeting Time (Id)'])
        for i in range(0, len(classes)):
            table.add_row([str(i), 
                           classes[i].get_room().get_id(),
                           classes[i].get_professor().get_name() +" (" + str(classes[i].get_professor().get_id()) +")",
                           classes[i].get_meetingTime().get_time() +" (" + str(classes[i].get_meetingTime().get_id()) +")"])
        print(table)'''
    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        classes.sort(key=lambda x: x.get_meetingTime().get_id())

        
        table = PrettyTable()
        table.field_names = ["Class #", "Course (Id)", "Room (Id)", "Professor", "Meeting Time"]

    
        for i, cls in enumerate(classes):
            table.add_row([
                i,
                f"{cls.get_course().get_name()} ({cls.get_course().get_id()})",
                f"{cls.get_room().get_name()} ({cls.get_room().get_id()})",
                f"{cls.get_professor().get_name()} ({cls.get_professor().get_id()})",
                f"{cls.get_meetingTime().get_time()} ({cls.get_meetingTime().get_id()})"])

    
        print(table)

    def print_schedule_by_student(self, schedule, student_id):
        classes = schedule.get_classes()
        student_classes = [cls for cls in classes if cls.get_students().get_id() == student_id]
        student_classes.sort(key=lambda x: x.get_meetingTime().get_id())

        
        table = PrettyTable()
        table.field_names = ["Class #", "Course (Id)", "Room (Id)", "Professor", "Meeting Time"]

    
        for i, cls in enumerate(student_classes):
            table.add_row([
                i,
                f"{cls.get_course().get_name()} ({cls.get_course().get_id()})",
                f"{cls.get_room().get_name()} ({cls.get_room().get_id()})",
                f"{cls.get_professor().get_name()} ({cls.get_professor().get_id()})",
                f"{cls.get_meetingTime().get_time()} ({cls.get_meetingTime().get_id()})"])

    
        print(f"\n> Schedule for student {student_id}")
        print(table)
    def print_timetable_grid(self, schedule):
        days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        days = sorted(list(set(mt.get_day() for mt in schedule._data.get_meetingTimes())), key=days_order.index)
        times = sorted(list(set(mt.get_time() for mt in schedule._data.get_meetingTimes())), key=lambda x: x.split('-')[0])

    
        table = PrettyTable()
        table.field_names = ["Time", "Day", "Course (Room) (Professor)"]

    
        for time in times:
            for day in days:
                classes_at_this_time = [cls for cls in schedule.get_classes() if cls.get_meetingTime().get_day() == day and cls.get_meetingTime().get_time() == time]
                course_info = " / ".join(f"{cls.get_course().get_name()} ({cls.get_room().get_name()}) ({cls.get_professor().get_name()})" for cls in classes_at_this_time)
                table.add_row([time, day, course_info])

    
        print(table)
       

    def print_schedule_by_professor(self, schedule):
        classes = schedule.get_classes()
        professors = set(cls.get_professor().get_id() for cls in classes)

        for professor_id in professors:
            professor_classes = [cls for cls in classes if cls.get_professor().get_id() == professor_id]
            professor_classes.sort(key=lambda x: x.get_meetingTime().get_id())

            table = PrettyTable()
            table.field_names = ["Class #", "Course (Id)", "Room (Id)", "Meeting Time"]

            for i, cls in enumerate(professor_classes):
                table.add_row([
                    i,
                    f"{cls.get_course().get_name()} ({cls.get_course().get_id()})",
                    f"{cls.get_room().get_name()} ({cls.get_room().get_id()})",
                    f"{cls.get_meetingTime().get_time()} ({cls.get_meetingTime().get_id()})"
                ])

            print(f"\n> Schedule for professor {professor_id}")
            print(table)

    def print_schedule_by_room(self, schedule):
        classes = schedule.get_classes()
        rooms = set(cls.get_room().get_id() for cls in classes)

        for room_id in rooms:
            room_classes = [cls for cls in classes if cls.get_room().get_id() == room_id]
            room_classes.sort(key=lambda x: x.get_meetingTime().get_id())

            table = PrettyTable()
            table.field_names = ["Class #", "Course (Id)", "Professor", "Meeting Time"]

            for i, cls in enumerate(room_classes):
                table.add_row([
                    i,
                    f"{cls.get_course().get_name()} ({cls.get_course().get_id()})",
                    f"{cls.get_professor().get_name()} ({cls.get_professor().get_id()})",
                    f"{cls.get_meetingTime().get_time()} ({cls.get_meetingTime().get_id()})"
                ])

            print(f"\n> Schedule for room {room_id}")
            print(table)
    

data = DataMigration()
displayMgr = DisplayMgr()
displayMgr.print_available_data()
generationNumber = 0
print("\n> Generation # "+str(generationNumber))
population = Population(POPULATION_SIZE)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
displayMgr.print_generation(population)
displayMgr.print_schedule_as_table(population.get_schedules()[0])
students = data.get_students()  
for student in students:
    displayMgr.print_schedule_by_student(population.get_schedules()[0], student.get_id())
displayMgr.print_schedule_by_professor(population.get_schedules()[0])
displayMgr.print_schedule_by_room(population.get_schedules()[0])
geneticAlgorithm = GeneticAlgorithm()
while (population.get_schedules()[0].get_fitness() != 1.0):
    generationNumber += 1
    print("\n> Generation # " + str(generationNumber))
    population = geneticAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    displayMgr.print_generation(population)
    displayMgr.print_schedule_as_table(population.get_schedules()[0])
    for student in students:
        displayMgr.print_schedule_by_student(population.get_schedules()[0], student.get_id())
    displayMgr.print_schedule_by_professor(population.get_schedules()[0])
    displayMgr.print_schedule_by_room(population.get_schedules()[0])
print("\n\n")