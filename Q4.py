total_marks=0
count=0
while count<5:
    marks=float(input("enter marks:"))
    total_marks +=marks
    count +=1
average_marks=total_marks / 5
print(f"total marks:{total_marks}")
print(f"average marks:{average_marks}")
