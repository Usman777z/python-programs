n=int(input("Enter the number of students:"))
studlist=[]
for i in range(0,n):
    stud={}
    stud["Name"]=input("Enter name:")
    stud["Roll No"]=int(input("Enter roll number:"))
    stud["Attendance"]=int(input("Enter attendance percentage:"))
    studlist.append(stud)
for i in range(1,n):
    for j in range(0,n-1):
        if(studlist[j]["Attendance"]<studlist[j+1]["Attendance"]):
            temp=studlist[j]
            studlist[j]=studlist[j+1]
            studlist[j+1]=temp
print("Attendance list")
for i in range(0,n):
    print(studlist[i])
