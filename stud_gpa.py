class Student:
    def __init__(self):
        self.firstname = input("Enter first name: ")
        self.lastname = input("Enter last name: ")
        self.allmarks = []
        
    
    def setmarks(self, nSemester, nSubjects):
        sem_marks = []
        for i in range(1, nSubjects+1):
            nCreditHours = int(input(f"Enter credit hours for subject {i} in semester {nSemester}: "))
            nGrades=int(input(f"Enter grades for subject {i} in semester {nSemester}: "))
            sem_marks.append({"credit_hours":nCreditHours, "Grades": nGrades})
        self.allmarks.append(sem_marks)

    def findgpa(self):
        print(f"Studnet Name: {self.firstname} {self.lastname}")
        nAllGPA = 0
        SemCount = 1
        for semmarks in self.allmarks:
            nTotalPoints = 0
            nTotalHours = 0
            for marks in semmarks:
                nSubjectGrade = marks['Grades']
                nSubjectHours = marks['credit_hours']
                nTotalPoints = nTotalPoints + (nSubjectGrade * nSubjectHours)
                nTotalHours = nTotalHours + nSubjectHours
            gpa = nTotalPoints/nTotalHours
            print(f"GPA for Semester {SemCount}: {gpa}")
            nAllGPA = nAllGPA + gpa
        cgpa = nAllGPA/len(self.allmarks)
        print(f"CGPA of {self.firstname} {self.lastname}: {nAllGPA}")


students = []
nStudents = int(input("Enter number of students: "))
for i in range(0, nStudents):
    print(f"Student: {i+1}")
    tempStudent = Student()
    students.append(tempStudent)


nSemesters = int(input("Enter number of Semesters: "))
for i in range(0, nSemesters):
    nSubjects = int(input(f"Enter number of subjects in semester {i+1}: "))
    for tempStudent in students:
        tempStudent.setmarks(i+1 ,nSubjects)


for tempStudent in students:
    tempStudent.findgpa()

#for i in range(1, nSemesters+1):
#    for j in range(0, nStudents):

    
