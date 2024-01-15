import sqlite3 as sql
conn = sql.connect('University.db')
c = conn.cursor()


c.execute("""create table Department 
        (ID_Department  TEXT PRIMARY KEY,
	    Name            TEXT
        )""")

c.execute("insert into Department Values ('D1', 'FTIMS'),"
          "('D2', 'Centrum Sportu'),"
          "('D3', 'Censtrum Językowe')")

c.execute("""create table Room
        (ID_Room    TEXT PRIMARY KEY, 
        Name        TEXT,
        Lab         INTEGER,
        Building    TEXT
        )""")

c.execute("insert into Room Values ('R1', 'F1', 0, 'B14'),"
        "('R2', 'F2', 0, 'B15'),"
        "('R3', 'F3', 0, 'B15'),"
        "('R4','F4', 0, 'B15'),"
        "('R5','F5', 0, 'B15'),"
        "('R6','F6', 0, 'B15'),"
        "('R7','Lab1', 1, 'B15'),"
        "('R8','Lab2', 1, 'B15'),"
        "('R9','Zatoka sportu', 0, 'Zatoka sportu'),"
        "('R10', 'Centrum kształcenia językowego', 0, 'Centrum kształcenia językowego')")



c.execute("""create table MeetingTime
          (ID_MeetingTime   TEXT PRIMARY KEY, 
          Day               TEXT,
          Time              TEXT
          )""")

c.execute("insert into MeetingTime (ID_MeetingTime, Day, Time) Values ('MON_01', 'Monday', '08:00-10:00'),"
                                        "('MON_02', 'Monday', '10:00-12:00'),"
                                        "('MON_03', 'Monday', '12:00-14:00')," 
                                        "('MON_04', 'Monday', '14:00-16:00'),"
                                        "('TUE_01', 'Tuesday', '08:00-10:00'),"
                                        "('TUE_02', 'Tuesday', '10:00-12:00'),"
                                        "('TUE_03', 'Tuesday', '12:00-14:00'),"
                                        "('TUE_04', 'Tuesday', '14:00-16:00'),"
                                        "('WED_01', 'Wednesday', '08:00-10:00'),"
                                        "('WED_02', 'Wednesday', '10:00-12:00'),"
                                        "('WED_03', 'Wednesday', '12:00-14:00'),"
                                        "('WED_04', 'Wednesday', '14:00-16:00'),"
                                        "('THU_01', 'Thursday', '08:00-10:00'),"
                                        "('THU_02', 'Thursday', '10:00-12:00'),"
                                        "('THU_03', 'Thursday', '12:00-14:00'),"
                                        "('THU_04', 'Thursday', '14:00-16:00'),"
                                        "('FRI_01', 'Friday', '08:00-10:00'),"
                                        "('FRI_02', 'Friday', '10:00-12:00'),"
                                        "('FRI_03', 'Friday', '12:00-14:00'),"
                                        "('FRI_04', 'Friday', '14:00-16:00')")

c.execute("""create table Students 
        (ID_Students    TEXT PRIMARY KEY,
	    Degree          INTEGER,
        Semester        INTEGER, 
	    Major           TEXT,
	    Department_ID   TEXT,
	    FOREIGN KEY (Department_ID) REFERENCES Department(ID_Department)
        )""")


c.execute("insert into Students VALUES ('MS01_01', 1, 1, 'Matematyka stosowana', 'D1'),"
        "('MS01_02', 1, 2, 'Matematyka stosowana', 'D1'),"
        "('MS01_03', 1, 3, 'Matematyka stosowana', 'D1'),"
        "('MS01_04', 1, 4, 'Matematyka stosowana', 'D1')")

c.execute("""create table Subject 
        (ID_Subject TEXT PRIMARY KEY,
        Name TEXT,
        Students_ID TEXT,
	    FOREIGN KEY (Students_ID) REFERENCES Students(ID_Students)
        )""")


c.execute("insert into Subject VALUES ('SUB01', 'Analiza matematyczna I', 'MS01_01' ),"
        "('SUB02', 'Algebra liniowa z geometrią analityczną I', 'MS01_01'),"
        "('SUB03', 'Technologie informatyczne I', 'MS01_01'),"
        "('SUB04', 'Wstęp do obliczeń symbolicznych', 'MS01_01'),"
        "('SUB05', 'Wstęp do logiki i teorii mnogości', 'MS01_01'),"
        "('SUB06', 'Topologia przestrzeni metrycznych', 'MS01_02'),"
        "('SUB07', 'Technologie informatyczne II', 'MS01_02'),"
        "('SUB08', 'Algebra liniowa z geometrią analityczną II', 'MS01_02'),"
        "('SUB09', 'Komputerowe obliczenia matematyczne', 'MS01_02'),"
        "('SUB10', 'Podstawy ekonomii i przedsiębiorczości', 'MS01_02'),"
        "('SUB11', 'Podstawy probabilistyki', 'MS01_02'),"
        "('SUB12', 'Analiza matematyczna II', 'MS01_02'),"
        "('LMOD01', 'Język obcy moduł 1', 'MS01_02'),"
        "('SPORT01', 'Wychowanie fizyczne', 'MS01_02'),"
        "('SUB13', 'Algebra abstrakcyjna', 'MS01_03'),"
        "('SUB14', 'Analiza matematyczna III', 'MS01_03'),"
        "('SUB15', 'Podstawy statystyki', 'MS01_03'),"
        "('SUB16', 'Wstęp do matematyki finansowej i ubezpieczeniowej', 'MS01_03'),"
        "('SUB17', 'Wstęp do teorii miary i całki', 'MS01_03'),"
        "('SPORT02', 'Wychowanie fizyczne', 'MS01_03'),"
        "('LMOD02', 'Język obcy moduł 2', 'MS01_03'),"
        "('SUB18', 'Funkcje zespolone', 'MS01_04'),"
        "('SUB19', 'Programowanie obiektowe w języku Java', 'MS01_04'),"
        "('SUB20', 'Wprowadzenie do szeregów czasowych', 'MS01_04'),"
        "('SUB21', 'Wstęp do równań różniczkowych', 'MS01_04'),"
        "('SUB22', 'Matematyczne podstawy analizy danych', 'MS01_04'),"
        "('SUB23', 'Testowanie hipotez statystycznych', 'MS01_04'),"
        "('LMOD03', 'Język obcy moduł 3', 'MS01_04'),"
        "('SUB25', 'Finanse osobiste', 'MS01_04'),"
        "('SUB26', 'Elementy kombinatoryki i teorii grafów', 'MS01_04'),"
        "('SUB27', 'Podstawy programowania w VBA', 'MS01_04'),"
        "('SUB28', 'Wybrane zagadnienia miary i kategorii', 'MS01_04'),"
        "('SUB29', 'Teoria liczb z zastosowaniami w kryptografii', 'MS01_04')")


c.execute("""create table Professor
          (ID_Professor   TEXT PRIMARY KEY, 
          Name            TEXT,
          Department_ID   TEXT,
          FOREIGN KEY (Department_ID) REFERENCES Department(ID_Department)
          )""")

c.execute("insert into Professor Values ('P01', 'Wojciech Kryszewski', 'D1'),"
                                    "('P02', 'Agnieszka Drwalewska', 'D1'),"
                                    "('P03','Włodzimierz Fechner', 'D1'),"
                                    "('P04','Marek Galewski', 'D1'),"
                                    "('P05','Filip Strobin', 'D1'),"
                                    "('P06','Michał Karbowańczyk', 'D1'),"
                                    "('P07','Daniel Arendt', 'D1'),"
                                    "('P08','Adam Bryszewski', 'D1'),"
                                    "('P09','Błażej Dziuba', 'D1'),"
                                    "('P10','Roman Krasiukianis', 'D1'),"
                                    "('P11','Jacek Rogowski', 'D1'),"
                                    "('P12','Szymon Głąb', 'D1'),"
                                    "('P13','Henryk Dębiński', 'D1'),"
                                    "('P14','Marek Bienias', 'D1'),"
                                    "('P15','Jacek Jachymski', 'D1'),"
                                    "('P16','Bogdan Balcerzak', 'D1'),"
                                    "('P17','Marcin Ostrowski', 'D1'),"
                                    "('P18','Feliks Kurp', 'D1'),"
                                    "('P19','Robert Stegliński', 'D1'),"
                                    "('P20','Igor Kossowski', 'D1'),"
                                    "('P21','Małgorzata Pietruk', 'D1'),"
                                    "('P22','Marek Martin', 'D1'),"
                                    "('P23','Lesław Gajek', 'D1'),"
                                    "('P24', 'Tomasz Filipczak', 'D1'),"
                                    "('P25', 'Jarosław Swaczyna', 'D1'),"
                                    "('P26', 'Magdalena Nockowska-Rosiak', 'D1'),"
                                    "('P27', 'Włodzimierz Fechner', 'D1'),"
                                    "('P28', 'Żywilla Fechner', 'D1'),"
                                    "('P29', 'Violetta Lipińska', 'D1'),"
                                    "('P30', 'Marek Balcerzak', 'D1'),"
                                    "('P31', 'Artur Bartoszewicz', 'D1'),"
                                    "('P32', 'Piotr Liczberski', 'D1'),"
                                    "('P33', 'Renata Długosz', 'D1'),"
                                    "('P34', 'Grzegorz Andrzejczak', 'D1'),"
                                    "('P35', 'Andrzej Okolewski', 'D1'),"
                                    "('P36', 'Katarzyna Szymańska-Dębowska', 'D1'),"
                                    "('P37', 'Michał Boczek', 'D1'),"
                                    "('P38', 'Przemysław Gordinowicz', 'D1'),"
                                    "('P39', 'Artur Wachowicz', 'D1'),"
                                    "('P40', 'Michał Bełdziński', 'D1'),"
                                    "('P41', 'Maciej Soin', 'D1'),"
                                    "('P42', 'Joanna Sośnicka', 'D1'),"
                                    "('P43', 'Izabela Urbaniak-Mastalerz', 'D1'),"
                                    "('P44', 'Bogdan Przeradzki', 'D1'),"
                                    "('P45', 'Marek Kałuszka', 'D1'),"
                                    "('P46', 'Piotr Kowalski', 'D1'),"
                                    "('P47', 'Marcin Rudź', 'D1'),"
                                    "('P48', 'Dariusz Klimczak', 'D1'),"
                                    "('P49', 'Mateusz Krukowski', 'D1'),"
                                    "('P98','Ewa Brochocka', 'D2'),"
                                    "('P99','Język', 'D3')")

c.execute("""create table Course_Professor
         (Course_ID          TEXT,
	Professor_ID         TEXT,
        FOREIGN KEY (Professor_ID) REFERENCES Professor(ID_Professor),
	FOREIGN KEY (Course_ID) REFERENCES Course(ID_Course)
        )""")


c.execute("insert into Course_Professor Values ('C01', 'P01'),"
                                            "('C02', 'P02'),"
                                            "('C02', 'P03'),"
                                            "('C02', 'P04'),"
                                            "('C03', 'P05'),"
                                            "('C04', 'P05'),"
                                            "('C05', 'P06'),"
                                            "('C05', 'P07'),"
                                            "('C05', 'P08'),"
                                            "('C06', 'P11'),"
                                            "('C06', 'P13'),"
                                            "('C07', 'P12'),"
                                            "('C08', 'P12'),"
                                            "('C08', 'P14'),"
                                            "('C09', 'P15'),"
                                            "('C10', 'P15'),"
                                            "('C10', 'P16'),"
                                            "('C11', 'P17'),"
                                            "('C11', 'P18'),"
                                            "('C12', 'P16'),"
                                            "('C13', 'P19'),"
                                            "('C13', 'P19'),"
                                            "('C14', 'P20'),"
                                            "('C14', 'P21'),"
                                            "('C14', 'P16'),"
                                            "('C14', 'P13'),"
                                            "('C15', 'P22'),"
                                            "('C16', 'P23'),"
                                            "('C17', 'P05'),"
                                            "('C18', 'P01'),"
                                            "('C19', 'P01'),"
                                            "('C20', 'P99'),"
                                            "('C21', 'P98'),"
                                            "('C22', 'P24'),"
                                            "('C23', 'P16'),"
                                            "('C23', 'P05'),"
                                            "('C23', 'P25'),"
                                            "('C24', 'P26'),"
                                            "('C25', 'P26'),"
                                            "('C25', 'P05'),"
                                            "('C26', 'P27'),"
                                            "('C27', 'P28'),"
                                            "('C27', 'P24'),"
                                            "('C28', 'P28'),"
                                            "('C29', 'P29'),"
                                            "('C30', 'P29'),"
                                            "('C30', 'P23'),"
                                            "('C31', 'P30'),"
                                            "('C32', 'P30'),"
                                            "('C32', 'P31'),"
                                            "('C32', 'P24'),"
                                            "('C32', 'P21'),"
                                            "('C32', 'P25'),"
                                            "('C33', 'P99'),"
                                            "('C34', 'P98'),"
                                            "('C35', 'P32'),"
                                            "('C36', 'P32'),"
                                            "('C36', 'P33'),"
                                            "('C37', 'P34'),"
                                            "('C38', 'P34'),"
                                            "('C38', 'P20'),"
                                            "('C39', 'P28'),"
                                            "('C40', 'P28'),"
                                            "('C40', 'P35'),"
                                            "('C41', 'P36'),"
                                            "('C42', 'P36'),"
                                            "('C43', 'P38'),"
                                            "('C44', 'P38'),"
                                            "('C45', 'P38'),"
                                            "('C46', 'P38'),"
                                            "('C47', 'P99')"
                                            )
c.execute("""create table Course
        (ID_Course  TEXT PRIMARY KEY,
        Name        TEXT,
        Subject_ID  TEXT,
        Type        TEXT,
        Duration    TEXT,
        FOREIGN KEY (Subject_ID) REFERENCES Subject(ID_Subject)
        )""")

c.execute("insert into Course Values ('C01', 'Analiza matematyczna I (wykład)', 'SUB01', 'Lecture', 60),"
                                    "('C02', 'Analiza matematyczna I (ćwiczenia)', 'SUB01', 'Exercise', 60),"
                                    "('C03', 'Algebra liniowa z geometrią analityczną I (wykład)', 'SUB02', 'Lecture', 30),"
                                    "('C04', 'Algebra liniowa z geometrią analityczną I (ćwiczenia)', 'SUB02', 'Excercise', 30),"
                                    "('C05', 'Technologie informatyczne I (laboratorium)', 'SUB03', 'Laboratory', 45),"
                                    "('C06', 'Wstęp do obliczeń symbolicznych (laboratorium)', 'SUB04', 'Laboratory', 30),"
                                    "('C07', 'Wstęp do logiki i teorii mnogości (wykład)', 'SUB05', 'Lecture', 30),"
                                    "('C08', 'Wstęp do logiki i teorii mnogości (ćwiczenia)', 'SUB05', 'Exercise', 30),"
                                    "('C09', 'Topologia przestrzeni metrycznych (wykład)', 'SUB06', 'Lecture', 30),"
                                    "('C10', 'Topologia przestrzeni metrycznych (ćwiczenia)', 'SUB06', 'Exercise', 30),"
                                    "('C11', 'Technologie informatyczne II (laboratorium)', 'SUB07', 'Laboratory', 45),"
                                    "('C12', 'Algebra liniowa z geometrią analityczną II (wykład)', 'SUB08', 'Lecture', 30),"
                                    "('C13', 'Algebra liniowa z geometrią analityczną II (ćwiczenia)', 'SUB08', 'Exercise', 30 ),"
                                    "('C14', 'Komputerowe obliczenia matematyczne (laboratorium)', 'SUB09', 'Laboratory', 30),"
                                    "('C15', 'Podstawy ekonomii i przedsiębiorczości (wykład)' , 'SUB10', 'Lecture', 30),"
                                    "('C16', 'Podstawy probabilistyki (wykład)', 'SUB11', 'Lecture', 30),"
                                    "('C17', 'Podstawy probabilistyki (ćwiczenia)', 'SUB11', 'Exercise', 30),"
                                    "('C18', 'Analiza matematyczna II (wykład)', 'SUB12', 'Lecture', 30),"
                                    "('C19', 'Analiza matematyczna II (ćwiczenia)', 'SUB12', 'Exercise', 45),"
                                    "('C20', 'Język obcy moduł 1 (ćwiczenia)', 'LMOD01', 'Exercise', 30),"
                                    "('C21', 'Wychowanie fizyczne (ćwiczenia)', 'SPORT01', 'Exercise', 30),"
                                    "('C22', 'Algebra abstrakcyjna (wykład)', 'SUB13', 'Lecture', 30),"
                                    "('C23', 'Algebra abstrakcyjna (ćwiczenia)', 'SUB13', 'Exercise', 30),"
                                    "('C24', 'Analiza matematyczna III (wykład)', 'SUB14', 'Lecture', 45),"
                                    "('C25', 'Analiza matematyczna III (ćwiczenia)', 'SUB14', 'Exercise', 45),"
                                    "('C26', 'Podstawy statystyki (wykład)', 'SUB15', 'Lecture', 30),"
                                    "('C27', 'Podstawy statystyki (ćwiczenia)', 'SUB15', 'Exercise', 30),"
                                    "('C28', 'Podstawy statystyki (laboratorium)', 'SUB15', 'Laboratory', 15),"
                                    "('C29', 'Wstęp do matematyki finansowej i ubezpieczeniowej (wykład)', 'SUB16', 'Lecture', 30),"
                                    "('C30', 'Wstęp do matematyki finansowej i ubezpieczeniowej (ćwiczenia)', 'SUB16', 'Exercise', 30),"
                                    "('C31', 'Wstęp do teorii miary i całki (wykład)', 'SUB17', 'Lecture', 30),"
                                    "('C32', 'Wstęp do teorii miary i całki (ćwiczenia)', 'SUB17', 'Exercise', 30),"
                                    "('C33', 'Język obcy moduł 2 (ćwiczenia)', 'LMOD02', 'Exercise', 30),"
                                    "('C34', 'Wychowanie fizyczne (ćwiczenia)', 'SPORT02', 'Exercise', 30),"
                                    "('C35', 'Funkcje zespolone (wykład)', 'SUB18', 'Lecture', 30),"
                                    "('C36', 'Funkcje zespolone (ćwiczenia)', 'SUB18', 'Exercise', 30),"
                                    "('C37', 'Programowanie obiektowe w języku Java (wykład)', 'SUB19', 'Lecture', 30),"
                                    "('C38', 'Programowanie obiektowe w języku Java (laboratorium)', 'SUB19', 'Laboratory', 30),"
                                    "('C39', 'Wprowadzenie do szeregów czasowych (wykład)', 'SUB20', 'Lecture', 30),"
                                    "('C40', 'Wprowadzenie do szeregów czasowych (ćwiczenia)', 'SUB20', 'Exercise', 30),"
                                    "('C41', 'Wstęp do równań różniczkowych (wykład)', 'SUB21', 'Lecture', 30),"
                                    "('C42', 'Wstęp do równań różniczkowych (ćwiczenia)', 'SUB21', 'Exercise', 30),"
                                    "('C43', 'Matematyczne podstawy analizy danych (wykład)', 'SUB22', 'Lecture', 30),"
                                    "('C44', 'Matematyczne podstawy analizy danych (laboratorium)', '', 'Laboratory', 30),"
                                    "('C45', 'Testowanie hipotez statystycznych (wykład)', 'SUB23', 'Lecture', 15),"
                                    "('C46', 'Testowanie hipotez statystycznych (laboratorium)', 'SUB23', 'Laboratory', 30),"
                                    "('C47', 'Język obcy moduł 3 (ćwiczenia)', 'LMOD03', 'Exercise', 30)"
                                    
                                    
                                    
                                    )


                  
conn.commit()
c.close()
conn.close()