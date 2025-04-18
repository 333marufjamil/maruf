"""
maruf = {
    "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(maruf) )

jamil = dict(name="maruf",age=23,country="bangladesh")
print(jamil)

num1 =[10,20,10.1]
num2 = (10,20)
num1.append(20.2)
num1.remove(10.1)
num3={
    "name":"naryf",
    "age":23,
    "position":"student"
}
print(num1)
print(num3["age"])

num4=[
    [
     [10,20,30],
     [10,20,30]
    ],
    [100, 200, 300],
    [1000, 2000, 3000]
]

print(num4)
print(num4[1][0])

temp =input("enter a number:")
num1,num2=temp.split(",")
num1 =int(num1)
num2=int(num2)
print(num1 ," ",num2)

num1 , num2 , num3 , num4= map (int ,input("Ënter number").split(","))
print(num1 , " " , num2, " " , num3, " " , num4)

a =[100,200,300,400]
b=[]
for i in range(1,3):
    b.append(a[i])
    print(b)


arr1 =[10,20,30,40,50]

arr2=[arr1[x] for x in range(len(arr1)-1,len(arr1)-4,-1)]

print(arr2)

arr1 =[10,20,30,40,50]

arr2=[arr1[x] for x in range(len(arr1)) if arr1[x] != 20]

print(arr2)


dictionary={
"student1":{
    "name":"maruf",
    "age":23

},
"student2":{
    "name":"marjhon",
    "age":26
}
}
name=[dictionary[i]["name"] for i in dictionary]
print(name)

list1=[10,20,30,40,50,60,70,80]
list2=[list1[x] for x in range(0,len(list1),2)]
print(*list2)

list1=[10,20,30,40,50,60,70,80]
list2=list1[0:3:1]+list1[-1:-4:-1][::-1]
print(list2)

list1=[10,20,30,40,50,60,70,80]
list2=[num for num in list1 if num==20 or num==50]
print(list2)

list1=[10,21,30,41,50,61,70,81]
list2=[]
for num in list1:
    if num==20 or num==50:list2.append(num)
print(list2)

list1=[12,13,45,67]
#list1.reverse()
list1.sort()
print(list1)

list_2d = [
    [1, 2, 3],
    [4, 50, 6]
]
list_3d = [
    [
        [1, 2, 3],
        [4, 50, 6],
    ],
    [
        [7, 8, 9],
        [10, 11, 12],
    ]
]

list_4d = [
    [  # 0th block
        [1, 2, 3],
        [4, 50, 6],
        [7, 8, 9],
        [10, 11, 12]
    ],
    [  # 1st block
        [1, 202, 3],
        [4, 50, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print(list_4d[1][0][1])

original_list =[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
extracted_list = []
mid  = len(original_list)//2
for i in range(mid-1,mid+2):
    extracted_list.append(original_list[i])
    print(extracted_list)

original_list =[10, 20, 30, 40,5,7,13]
extracted_list = []
for i in  original_list:
    if i%2 != 0:
     extracted_list.append(i)
print(extracted_list)

original_list =[10, 20, 30, 40,5,7,13]
extracted_list =[x for x in original_list if x%2!= 0]
print(extracted_list)

semester_8_D = {

    "student1": {
        "name": "John",
        "id": 20,
        "gender": "Male",
    },

    "student2": {
        "name": "Jane",
        "id": 21,
        "gender": "Female",
    },

    "student3": {
        "name": "Bob",
        "id": 22,
        "gender": "Male",
    },

}

name_list = [semester_8_D[student]['name'] for student in semester_8_D]
print(name_list)

id_list = [semester_8_D[student]['id'] for student in semester_8_D]
print(id_list)

#lab report:3 Question: A Dictionary is given there.
 Remove 2002 from it and print to show that it has been removed.
 Then, insert your ID in that place and show it
"""
tuple1 = (10, 20)

Student_list = {
    "Student1": {
        "Name": "Kuhin",
        "Id": 221311155,
        "CGPA": 4.00
    },
    "Student2": {
        "Name": "Nuhan",
        "Id": 221311121,
        "CGPA": 4.00
    },
    "Student3": {
        "Name": "Ronok",
        "Id": 221311127,
        "CGPA": 3.00
    },
    "Student4": {
        "Name": "Ripper",
        "ID": "Confidential",
        "CGPA": "Unknown",
        "Time_Space": [
            [
                [
                    [10, 20, 30],
                    [40, 50, 60]
                ],
                [
                    [100, 200, 300],
                    [400, 500, 600]
                ]
            ],
            [
                [
                    [101, 202, 303],
                    [404, 505, 606]
                ],
                [
                    [1001, 2002, 3003],
                    [4004, 5005, 6006]
                ]
            ]
        ]
    }
}

Student_list["Student4"]["Time_Space"][1][1][0].remove(2002)

print("After removing 2002:", Student_list["Student4"]["Time_Space"])

Student_list["Student4"]["Time_Space"][1][1][0].append(221311154)

print("After adding 221311154:", Student_list["Student4"]["Time_Space"])



#lab report4:


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
