print("welcome to the marks calculator")
total_marks, i = 0 , 0
subject = int(input("Enter the number of subjects: "))
marks = [0] * subject
while i < subject:
    marks[i] = int(input("Enter the marks of subject: "))
    # marks.append(mark)

    i = i+1

i=0
while i < subject:

    total_marks += marks[i]
    i += 1
    print("Total marks: ", total_marks)

average_marks = total_marks / subject

print("Average marks: ", average_marks)

if(average_marks >= 90):
    print("Grade: A+")
elif(average_marks >= 80):
    print("Grade: A")
elif(average_marks >= 70):
    print("Grade: B+")
elif(average_marks >= 60):
    print("Grade: B")
elif(average_marks >= 50):
    print("Grade: C+")
elif(average_marks >= 45):
    print("Grade: C")
else:
    print("Grade: F")