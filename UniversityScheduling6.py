import random as rnd
import prettytable as prettytable
from operator import length_hint
from prettytable import PrettyTable
import sqlite3 as sqlite


"""

    BASIC CLASSES

"""

"""
Class Professor
"""
class Professor:
    
    def __init__(self, id, name, availability):
        self._id = id
        self._name = name
        self._availability = availability
        self.CourseClass = []
    
    def get_id(self): 
        return self._id
    
    def get_name(self): 
        return self._name
    
    def get_availability(self):
        return self._availability
    
    def addCourseClass(self, courseClass):
        self.CourseClasses.append(courseClass)
    
    def __str__(self): 
        return self._name
    
    
    def __eq__(self, other):
        if isinstance(other, Professor):
            return self._id == other._id
        return False
    
    def __hash__(self):
        return hash(self._id)           

"""
Class Room
"""

class Room:
    
    def __init__(self, id, name, lab,Capacity, building):
        self._id = id
        self._name = name
        self._lab = lab
        self._Capacity=Capacity
        self._building = building

    
    def get_id(self): 
        return self._id
    
    def get_name(self): 
        return self._name
    
    def get_lab(self): 
        return self._lab
    def get_Capacity(self):
        return self._Capacity
    def get_building(self): 
        return self._building
    
 
    
    def __eq__(self, other):
        if isinstance(other, Room):
            return self._id == other._id
        return False
    
    def __hash__(self):
        return hash(self._id)

"""
Class Meeting Time
"""
    
    
class MeetingTime:
    
    def __init__(self, id, day, time):
        self._id = id
        self._time = time
        self._day = day
    
    def get_id(self): 
        return self._id
    
    def get_day(self): 
        return self._day        
    
    def get_time(self): 
        return self._time
    
    
    def __eq__(self, other):
        if isinstance(other, MeetingTime):
            return self._id == other._id
        return False
    
    def __hash__(self):
        return hash(self._id)    
    

""" 
Class Course
"""

class Course:
    
    def __init__(self, id, name, professors, course_type,Numgrstudents,duration):
        self._id = id
        self._name = name
        self._professors = professors
        self._course_type = course_type
        self._Numgrstudents=Numgrstudents
        self._duration = duration
    
    def get_id(self): 
        return self._id
    
    def get_name(self): 
        return self._name
    
    def get_professors(self): 
        return self._professors 
    
    def get_course_type(self): 
        return self._course_type
    
    def get_Numgrstudents(self):
        return self._Numgrstudents
    
    def get_duration(self): 
        return self._duration
    
    def __str__(self): 
        return self._name

    def __eq__(self, other):
        if isinstance(other, Course):
            return (self._id == other._id and self._name == other._name and 
                    self._professors == other._professors and self._course_type == other._course_type and
                    self._Numgrstudents==other._Numgrstudents and
                    self._duration == other._duration)
        return False

    def __hash__(self):
        return hash((self._id, self._name, tuple(self._professors), self._course_type,self._Numgrstudents,self._duration))
    
    
    """ 
    Class Students
    """
    
class Students:
    
    def __init__(self, id, courses):
        self._id = id
        self._courses = courses
    
    def get_id(self): 
        return self._id
    
    def get_courses(self): 
        return self._courses
    
    def __eq__(self, other):
        if isinstance(other, Students):
            return self._id == other._id
        return False
    
    def __hash__(self):
        return hash(self._id)
    
""" 
Class Department    
"""

class Department:
    
    def __init__(self, id, name):
        self._id = id
        self._name = name
    
    def get_id(self): 
        return self._id    
    
    def get_name(self): 
        return self._name

    def __eq__(self, other):
        if isinstance(other, Department):
            return self._id == other._id
        return False
    
    def __hash__(self):
        return hash(self._id)

"""
Class Subject
"""

class Subject:
    
    def __init__(self, id, name):
        self._id = id
        self._name = name
    
    def get_id(self): 
        return self._id
    
    def get_name(self): 
        return self._name
    
    def __eq__(self, other):
        if isinstance(other, Subject):
            return self._id == other._id
        return False
    
    def __hash__(self):
        return hash(self._id)

"""" 
Data Migration
"""
#Selekcja danych przy uzyciu pilku(SQL) z danymi
class DataMigration:
    
    def __init__(self):
    
        self._conn = sqlite.connect('University13.db')
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
            returnRooms.append(Room(rooms[i][0], rooms[i][1], rooms[i][2], rooms[i][3],rooms[i][4]))
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
            returnProfessors.append(Professor(professors[i][0], professors[i][1], self.select_professor_availability(professors[i][0])))
        return returnProfessors
    
    def select_professor_availability(self, professor):
        self._c.execute("SELECT * from Professor_availability where Professor_id = '" + professor + "'")
        professorMTsRS = self._c.fetchall()
        professorMTs = []
        for i in range(0, len(professorMTsRS)): professorMTs.append(professorMTsRS[i][1])
        professorAvailability = list()
        for i in range(0, len(self._meetingTimes)):
            if self._meetingTimes[i].get_id() in professorMTs:
                professorAvailability.append(self._meetingTimes[i])
        return professorAvailability
    
    def select_courses(self):
        self._c.execute("SELECT * FROM Course")
        courses = self._c.fetchall()
        returnCourses = []
        for i in range(0, len(courses)):
            returnCourses.append(Course(courses[i][0], courses[i][1], self.select_course_professors(courses[i][0]), courses[i][3], courses[i][4],courses[i][5]))
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
    
    def get_rooms(self): 
        return self._rooms
    
    def get_professors(self):
        return self._professors
    
    def get_courses(self): 
        return self._courses
    
    def get_students(self): 
        return self._students
    
    def get_meetingTimes(self): 
        return self._meetingTimes
    
    def get_numberOfClasses(self): 
        return self._numberOfClasses



data_migration = DataMigration()

""" 
Class Class
"""

class Class:
    
    def __init__(self, id,  students, course):
        self._id = id
        self._students = students
        self._course = course
        self._professor = None
        self._meetingTime = None
        self._room = None
    
    def get_id(self): 
        return self._id
    
    def get_students(self): 
        return self._students
    
    def get_course(self): 
        return self._course
    
    def get_professor(self): 
        return self._professor
    
    def get_meetingTime(self): 
        return self._meetingTime
    
    def get_room(self): 
        return self._room
    
    def set_professor(self, professor):
        self._professor = professor
    
    def set_meetingTime(self, meetingTime):
        self._meetingTime = meetingTime
    
    def set_room(self, room):
        self._room = room
    
    def __str__(self): 
        student_id = str(self._students.get_id()) if self._students else "None"
        course_id = str(self._course.get_id()) if self._course else "None"
        room_id = str(self._room.get_id()) if self._room else "None"
        professor_id = str(self._professor.get_id()) if self._professor else "None"
        meeting_time_id = str(self._meetingTime.get_id()) if self._meetingTime else "None"
        
        return f"{student_id},{course_id},{room_id},{professor_id},{meeting_time_id}"

       
    def __eq__(self, other):
        if isinstance(other, Class):
            return (self._id == other._id and self._students == other._students and 
                    self._course == other._course and self._professor == other._professor and 
                    self._meetingTime == other._meetingTime and self._room == other._room)
        return False

    def __hash__(self):
        return hash((self._id, self._students, self._course, self._professor, self._meetingTime, self._room))

"""
Class Schedule
"""
class Schedule:
    
    def __init__(self):
        self._data = data
        self._classes = []
        self._numbOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True
        self._conflictingClasses = []
        self._roomSchedule = {room.get_id(): self._data.get_meetingTimes()[:] for room in self._data.get_rooms()}
        
    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes
    
    def get_numbOfConflicts(self):
        return self._numbOfConflicts

    def get_fitness(self):
        if (self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness
    
    def initialize(self):
    
        for student in self._data.get_students():
            courses = student.get_courses()
            for course in courses:
                newClass = Class(self._classNumb, student, course)
                self._classNumb += 1
                
                room = self._select_room_for_course(course)
                newClass.set_room(room)
                
                meeting_time = self._select_meeting_time_for_room(room)
                newClass.set_meetingTime(meeting_time)
                
                newClass.set_professor(course.get_professors()[rnd.randrange(0, len(course.get_professors()))])
                
                self._classes.append(newClass)
        
        return self
    
    def _select_room_for_course(self, course):
        course_type = course.get_course_type()
        if course_type == "Laboratory":
            # Wybieramy tylko sale, gdzie room.get_lab() == 1
            lab_rooms = [room for room in self._data.get_rooms() if room.get_lab() == 1]
            if lab_rooms:
                return rnd.choice(lab_rooms)
            
                
        elif course_type == "Language":
            # Przypisujemy salę R20 dla kursów językowych
            return next((room for room in self._data.get_rooms() if room.get_id() == "R20"), None)
        elif course_type == "Sport":
            # Przypisujemy salę R19 dla kursów sportowych
            return next((room for room in self._data.get_rooms() if room.get_id() == "R19"), None)
        else:
            # Dla pozostałych kursów wybieramy dowolną salę, która nie jest specjalistyczna
            other_rooms = [room for room in self._data.get_rooms() if room.get_id() not in ["R19", "R20"] and room.get_lab() == 0]
            if other_rooms:
                return rnd.choice(other_rooms)
        return None

        
    def _select_meeting_time_for_room(self, room):
        available_times = self._roomSchedule[room.get_id()]
        if available_times:
            meeting_time = available_times.pop(rnd.randrange(len(available_times)))
            return meeting_time
        
            
        return None

    def calculate_fitness(self):
        self._numbOfConflicts = 0
        self._conflictingClasses = []  
        classes = self.get_classes()
        for i in range(0, len(classes)):
            for j in range(0, len(classes)):
                if (j >= i):
                    if (classes[i].get_meetingTime() == classes[j].get_meetingTime() and classes[i].get_course().get_id() != classes[j].get_course().get_id()):
                        
                        if (classes[i].get_room() == classes[j].get_room()):
                            self._numbOfConflicts += 1
                            self._conflictingClasses.append((classes[i], classes[j], "Room conflict"))   
                        
                        if (classes[i].get_professor() == classes[j].get_professor()):
                            self._numbOfConflicts += 1
                            self._conflictingClasses.append((classes[i], classes[j], "Professor conflict"))
                        
                        if (classes[i].get_students() == classes[j].get_students()):
                            self._numbOfConflicts += 1
                            self._conflictingClasses.append((classes[i], classes[j], "Students conflict"))
        return 1 / ((1.0*self._numbOfConflicts + 1))
    
    def get_conflicting_classes(self):
        conflicting_classes = []
        classes = self.get_classes()
        for i in range(len(classes)):
            for j in range(i + 1, len(classes)):
                if classes[i].get_meetingTime() == classes[j].get_meetingTime():
                    
                    if classes[i].get_room() == classes[j].get_room():
                        conflicting_classes.append((classes[i], classes[j], "Room conflict"))
                    if classes[i].get_professor() == classes[j].get_professor():
                        conflicting_classes.append((classes[i], classes[j], "Professor conflict"))
                    if classes[i].get_students() == classes[j].get_students():
                        conflicting_classes.append((classes[i], classes[j], "Students conflict" ))
        return conflicting_classes

    @staticmethod
    def calculate_mutation_rate(best_fitness, last_best_fitness):
        if best_fitness is not None and last_best_fitness is not None and best_fitness == last_best_fitness:
            mutation_rate = 0.2
            return mutation_rate
        return 0.1
    
    
    def __str__(self):
        if not self._classes:  
            return "No classes"
        returnValue = ""
        for i in range(0, len(self._classes)-1):
            returnValue += str(self._classes[i]) + ", "
        returnValue += str(self._classes[len(self._classes)-1])
        return returnValue

        
    

"""
class Population
"""

class Population:
    
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = [Schedule().initialize() for i in range(size)]
    
    def get_schedules(self):
        return self._schedules


#Wprowadzenie klasy algortymu genetycznego
"""
Class GeneticAlgorithm 
"""

POPULATION_SIZE = 10
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1
CROSSOVER_PROBABILITY = 0.75

class GeneticAlgorithm:
    
    def __init__(self, data):
        self._data = data
        self.best_fitness = None
        self.last_best_fitness = None

    
    def evolve(self, population):
        #print("Evolution started") 
        return self._mutate_population(self._crossover_population(population))
    

    def _crossover_population(self, pop):
       # print("Crossover started")
        crossover_pop = Population(0)
        
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
            #print("Crossover started")
        return crossover_pop
        

    def _mutate_population(self, population):
        #print("Mutation started")
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population
    
    
    def _crossover_schedule(self, schedule1, schedule2):
        #print("Crossover schedule",Schedule().initialize())
        crossoverSchedule = Schedule().initialize()
        # cut = rnd.randint(0, len(crossoverSchedule.get_classes()))
        for i in range(0, len(crossoverSchedule.get_classes())):
            if CROSSOVER_PROBABILITY > rnd.random():
                cut = rnd.randint(0, len(crossoverSchedule.get_classes()))
                if i < cut:
                    crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
                else:
                    crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
                    if schedule1.get_classes()[i]!= schedule2.get_classes()[i]:
                        break
        return crossoverSchedule


    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            if(MUTATION_RATE > rnd.random()): mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule        

    def _select_tournament_population(self, pop):
        #print("Tournament selection")
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        self.best_fitness = tournament_pop.get_schedules()[0].get_fitness()
        self.last_best_fitness = tournament_pop.get_schedules()[1].get_fitness()
        return tournament_pop



"""
Class Display
"""

class DisplayMgr:
    
    def print_available_data(self):
        print("> All Available Data")
    
    def print_generation(self, population):
        table3 = prettytable.PrettyTable(['schedule #', 'fitness', '# of conflicts', 'classes [students, course, room, professor, meeting-time]'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table3.add_row([str(i), round(schedules[i].get_fitness(),3), schedules[i].get_numbOfConflicts(), schedules[i].__str__()])
        print(table3)

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        classes.sort(key=lambda x: x.get_meetingTime().get_id())

        
        table4 = PrettyTable()
        table4.field_names = ["Class #", "Course (Id)", "Room (Id)", "Professor", "Meeting Time"]

    
        for i, cls in enumerate(classes):
            table4.add_row([
                i,
                f"{cls.get_course().get_name()} ({cls.get_course().get_id()})",
                
                f"{cls.get_room().get_name()} ({cls.get_room().get_id()})",
                f"{cls.get_professor().get_name()} ({cls.get_professor().get_id()})",
                f"{cls.get_meetingTime().get_time()} ({cls.get_meetingTime().get_id()})"
                ])

    
        print(table4)

    def print_schedule_by_student(self, schedule, student_id):
        classes = schedule.get_classes()
        student_classes = [cls for cls in classes if cls.get_students().get_id() == student_id]
        student_classes.sort(key=lambda x: x.get_meetingTime().get_id())

        
        table = PrettyTable()
        table.field_names = ["Class #", "Course (Id)", "Room (Id)", "Professor", "Meeting Time","Capacity","Max Number of Students"]

    
        for i, cls in enumerate(student_classes):
            table.add_row([
                i,
                f"{cls.get_course().get_name()} ({cls.get_course().get_id()})",
                f"{cls.get_room().get_name()} ({cls.get_room().get_id()})",
                f"{cls.get_professor().get_name()} ({cls.get_professor().get_id()})",
                f"{cls.get_meetingTime().get_time()} ({cls.get_meetingTime().get_id()})",
                f"{cls.get_room().get_Capacity()}",
                f"{cls.get_course().get_Numgrstudents()}"])
            
    
        print(f"\n> Schedule for student {student_id}")
        print(table)

        y=table.get_string(fields=["Room (Id)","Capacity"])
        print(y)
        z=table.get_string(fields=["Course (Id)","Max Number of Students"])
        print(z)
    
    def print_timetable_grid(self, schedule):
        days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        days = sorted(list(set(mt.get_day() for mt in schedule._data.get_meetingTimes())), key=days_order.index)
        times = sorted(list(set(mt.get_time() for mt in schedule._data.get_meetingTimes())), key=lambda x: x.split('-')[0])

    
        table0 = PrettyTable()
        table0.field_names = ["Time", "Day", "Course (Room) (Professor)"]

    
        for time in times:
            for day in days:
                classes_at_this_time = [cls for cls in schedule.get_classes() if cls.get_meetingTime().get_day() == day and cls.get_meetingTime().get_time() == time]
                course_info = " / ".join(f"{cls.get_course().get_name()} ({cls.get_room().get_name()}) ({cls.get_professor().get_name()})" for cls in classes_at_this_time)
                table0.add_row([time, day, course_info])

    
        print(table0)
       

    def print_schedule_by_professor(self, schedule):
        classes = schedule.get_classes()
        professors = set(cls.get_professor().get_id() for cls in classes)

        for professor_id in professors:
            professor_classes = [cls for cls in classes if cls.get_professor().get_id() == professor_id]
            professor_classes.sort(key=lambda x: x.get_meetingTime().get_id())

            table1 = PrettyTable()
            table1.field_names = ["Class #", "Course (Id)", "Room (Id)", "Meeting Time","Availability"]

            for i, cls in enumerate(professor_classes):
                table1.add_row([
                    i,
                    f"{cls.get_course().get_name()} ({cls.get_course().get_id()}) ",
                    f"{cls.get_room().get_name()} ({cls.get_room().get_id()})",
                    f"{cls.get_meetingTime().get_time()} ({cls.get_meetingTime().get_id()})",
                    f"{cls.get_professor().get_availability()}"
                    
                ])

            print(f"\n> Schedule for professor {professor_id}")
            print(table1)

    def print_schedule_by_room(self, schedule):
        classes = schedule.get_classes()
        rooms = set(cls.get_room().get_id() for cls in classes)

        for room_id in rooms:
            room_classes = [cls for cls in classes if cls.get_room().get_id() == room_id]
            room_classes.sort(key=lambda x: x.get_meetingTime().get_id())

            table2 = PrettyTable()
            table2.field_names = ["Class #", "Course (Id)", "Professor", "Meeting Time"]

            for i, cls in enumerate(room_classes):
                table2.add_row([
                    i,
                    f"{cls.get_course().get_name()} ({cls.get_course().get_id()}) ",
                    f"{cls.get_professor().get_name()} ({cls.get_professor().get_id()})",
                    f"{cls.get_meetingTime().get_time()} ({cls.get_meetingTime().get_id()})"
                ])
                print(f"\n> Schedule for room {room_id}")
                print(table2)

            
                

        

            







"""
main
"""

data = DataMigration()
displayMgr = DisplayMgr()
displayMgr.print_available_data()
generationNumber = 0
print("\n> Generation # " + str(generationNumber))
population = Population(POPULATION_SIZE)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
displayMgr.print_generation(population)
displayMgr.print_schedule_as_table(population.get_schedules()[0])
displayMgr.print_schedule_by_professor(population.get_schedules()[0])
#displayMgr.print_schedule_by_room(population.get_schedules()[0])

students = data.get_students()


geneticAlgorithm = GeneticAlgorithm(data)
schedule = population.get_schedules()[0]
conflicting_classes = schedule.get_conflicting_classes()
print(f"\nConflicts in Generation #{generationNumber}:")
for class1, class2, conflict_type in conflicting_classes:
    print(f"Conflict: {class1} and {class2} ({conflict_type})")





                

while (population.get_schedules()[0].get_fitness() != 1.0):
    generationNumber += 1
    population = geneticAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    
    
    if generationNumber % 100 == 0:
        print("\n> Generation # " + str(generationNumber))
        displayMgr.print_generation(population)
        displayMgr.print_schedule_as_table(population.get_schedules()[0])
        displayMgr.print_schedule_by_professor(population.get_schedules()[0])
        displayMgr.print_schedule_by_room(population.get_schedules()[0])
        for student in students:
            displayMgr.print_schedule_by_student(population.get_schedules()[0], student.get_id())
        
         
        schedule = population.get_schedules()[0]


       
    
        
        



        
    
                              
            

print("\n\n")


