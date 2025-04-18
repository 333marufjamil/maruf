Sem_8th_D = {
    'Maruf Jamil': {
        'student_id': 221311154,
        'courses_taken': {
            'CSE 420': 'A+',
            'CSE 421': 'A+',
            'CSE 422': 'A+',
            'CSE 423': 'B-',
            'CSE 424': 'C',
            'CSE 425': 'A+',
            'CSE 426': 'B+',
            'CSE 439': 'C',
            'CSE 428': 'B+',
        },
        'GPA': 3.49
    },
    'Nahid': {
        'student_id': 221311131,
        'courses_taken': {
            'CSE 420': 'A+',
            'CSE 421': 'A+',
            'CSE 422': 'A+',
            'CSE 423': 'B+',
            'CSE 424': 'C',
            'CSE 425': 'A+',
            'CSE 426': 'B',
            'CSE 439': 'D',
            'CSE 428': 'B+',
        },
        'GPA': 3.87
    },
    'Manowar': {
        'student_id': 221311156,
        'courses_taken': {
            'CSE 420': 'C+',
            'CSE 421': 'A',
            'CSE 422': 'A-',
            'CSE 423': 'B-',
            'CSE 424': 'B+',
            'CSE 425': 'A+',
            'CSE 426': 'B+',
            'CSE 439': 'A+',

        },
        'GPA': 3.45
    },
    'Nuhan': {
        'student_id': 221311121,
        'courses_taken': {
             'CSE 420': 'C+',
            'CSE 421': 'B',
            'CSE 422': 'A+',
            'CSE 423': 'B+',
            'CSE 424': 'B+',
            'CSE 425': 'A+',
            'CSE 426': 'A+',
            'CSE 439': 'A+',
            'CSE 428': 'A-',
        },
        'GPA': 3.67
    },
    'Yousof': {
        'student_id': 221311130,
        'courses_taken': {
            'CSE 420': 'A',
            'CSE 421': 'D',
            'CSE 422': 'A+',
            'CSE 423': 'C+',
            'CSE 424': 'B+',
            'CSE 425': 'A+',
            'CSE 426': 'D',
            'CSE 439': 'A+',
            'CSE 428': 'A+',
        },
        'GPA': 3.28
    },
    'Samiha': {
        'student_id': 221311198,
        'courses_taken': {
            'CSE 420': 'A+',
            'CSE 421': 'A',
            'CSE 422': 'A+',
            'CSE 423': 'B+',
            'CSE 424': 'D',
            'CSE 425': 'A+',
            'CSE 426': 'C',
            'CSE 439': 'A+',
            'CSE 428': 'A-',
        },
        'GPA': 3.75
    },
    'Rifat': {
        'student_id': 221311199,
        'courses_taken': {
            'CSE 420': 'A-',
            'CSE 421': 'A-',
            'CSE 422': 'A',
            'CSE 423': 'B+',
            'CSE 424': 'C',
            'CSE 425': 'A+',
            'CSE 426': 'D',
            'CSE 439': 'C',
            'CSE 428': 'B+',
        },
        'GPA': 3.83
    },
}

course_code = input("Enter the course code: ").strip()
ID = int(input("Enter your student ID: ").strip())

found = False
for student_name, student_info in Sem_8th_D.items():
    if course_code in student_info['courses_taken']:
        print(f"{student_name} - Grade: {student_info['courses_taken'][course_code]}")
        found = True
    else:
        print(f"{student_name} - Grade: This course could not be found.")

if not found:
    print("This course could not be found..")

for student_name, student_info in Sem_8th_D.items():
    if student_info['student_id'] == ID:
        print(f"\n{student_name}, you have achieved a GPA of : {student_info['GPA']}")
