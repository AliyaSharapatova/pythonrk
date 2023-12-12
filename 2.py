def read_credits(filename):
    with open(filename) as file:
        return {line.split(':')[0]: int(line.split(':')[1]) for line in file}

def read_grades(directory, credits):
    return {course: {'grades': [float(line.strip()) for line in open(f"{directory}/{course}.txt")],
                    'credits': credits[course]} for course in credits}

def translate_scores_to_points(grades):
    return [(score / 5) * 4 for score in grades]

def calculate_overall_GPA(students_grades):
    total_weighted_points = sum(translate_scores_to_points(course_grades['grades'][i]) * course_grades['credits']
                                for course, course_grades in students_grades.items()
                                for i in range(len(course_grades['grades'])))
    total_credits = sum(course_grades['credits'] for course_grades in students_grades.values())
    return total_weighted_points / total_credits

def save_overall_GPA(gpa, output_filename):
    with open(output_filename, 'w') as file:
        file.write(f"{gpa:.2f}")

directory = "grades"
credits_filename = f"{directory}/credits.txt"
output_filename = f"{directory}/overallGPAs.txt"

credits = read_credits(credits_filename)
students_grades = read_grades(directory, credits)
overall_gpa = calculate_overall_GPA(students_grades)
save_overall_GPA(overall_gpa, output_filename)
