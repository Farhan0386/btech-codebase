student=[
    {"name": "Farhan", "gpa": 6},
    {"name": "Moin", "gpa": 7},
    {"name": "Navjot", "gpa":8 },
    {"name": "Satyarth", "gpa": 9},
    ]
top_student=sorted(student, key=lambda x:x['gpa'], reverse=True)
print(top_student)  