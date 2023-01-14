class Student:
    def __init__(self, name):
        self.name = name
        self.semesters = []

    def add_semester(self, semester):
        self.semesters.append(semester)

    def calculate_gpa(self):
        total_credits = 0
        total_points = 0
        for semester in self.semesters:
            for course in semester.courses:
                total_credits += course.credits
                total_points += course.points
        if total_credits > 0:
            return total_points / total_credits
        else:
            return None


class Semester:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def calculate_gpa(self):
        total_credits = 0
        total_points = 0
        for course in self.courses:
            total_credits += course.credits
            total_points += course.points
        if total_credits > 0:
            return total_points / total_credits
        else:
            return None


class Course:
    def __init__(self, name, code, credits, grade):
        self.name = name
        self.code = code
        self.credits = credits
        self.grade = grade

    def get_points(self):
        if self.grade == "A":
            return 4 * self.credits
        elif self.grade == "B":
            return 3 * self.credits
        elif self.grade == "C":
            return 2 * self.credits
        elif self.grade == "D":
            return self.credits
        else:
            return 0

    def points(self):
        return self.get_points()


# create a student
student = Student("Alice")

# create semesters
fall_semester = Semester("Fall")
spring_semester = Semester("Spring")

# add courses to semesters
fall_semester.add_course(Course("Calculus", "MATH-101", 4, "A"))
fall_semester.add_course(Course("Computer Science", "CSC-101", 3, "B"))
spring_semester.add_course(Course("Physics", "PHY-101", 3, "C"))
spring_semester.add_course(Course("Biology", "BIO-101", 4, "A"))

# add semesters to student
student.add_semester(fall_semester)
student.add_semester(spring_semester)

# calculate student's GPA
gpa = student.calculate_gpa()
print("Student's GPA:", gpa)
