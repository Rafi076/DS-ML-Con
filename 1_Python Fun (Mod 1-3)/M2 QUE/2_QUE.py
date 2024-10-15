#Score Tracker
# you are asked to create a score tracker . you'll take the name &
# the score of a student as input . store those by name & print all
# the students name & their score. the input end when the studet name is "stop"

student ={}
while True:
    name = input("Enter the student's name: ").strip()
    if name == "stop": break
    score = input(f"Enter The Score for {name} : ").strip()
    
    score = float(score)
    student[name] = score
    
    
print("\nFinal Scores:")
for name, score in student.items():
    print(f"{name}: {score}")




    


