def translateLetter(letter):
    letter_points = {'A+': 4.3, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
                     'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3,
                     'D': 1.0, 'D-': 0.7}
    return letter_points.get(letter, 0.0)

def translatePercentage(percentage):
    points = [4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7]
    return next(point for point, threshold in zip(points, range(95, 45, -5)) if percentage >= threshold)

def calculateGPA(*args):
    total_points = sum(args[i] * args[i + 1] for i in range(0, len(args), 2))
    total_credits = sum(args[1::2])
    
    return round(total_points / total_credits, 2) if total_credits != 0 else 0.0


gpa = calculateGPA(translateLetter('A+'), 4, translateLetter('B'), 3, translateLetter('C'), 4)
print("Overall GPA:", gpa)
