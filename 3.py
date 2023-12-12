class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.calculateGPA()
        self.setStatus()

    def calculateGPA(self):
        total_credits = sum(course['credits'] for course in self.scores.values())
        weighted_sum = sum(course['score'] * course['credits'] for course in self.scores.values())
        self.gpa = weighted_sum / total_credits if total_credits else 0.0

    def setStatus(self):
        self.status = 'Passed' if self.gpa >= 1.0 else 'Not Passed'

    def showGPA(self):
        print(f"{self.name}'s GPA: {self.gpa:.2f}")

    def showStatus(self):
        print(f"{self.name}'s Status: {self.status}")


courses = {
    'math': {'score': 4.3, 'credits': 4},
    'chemistry': {'score': 3.3, 'credits': 3},
    'english': {'score': 4.0, 'credits': 4}
}

student1 = Student("John Doe", courses)
student1.showGPA()
student1.showStatus()
