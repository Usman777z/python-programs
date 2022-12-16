n=int(input("Enter the number of students:"))
studlist=[]
for i in range(0,n):
    stud={}
    stud['name']=input("Enter name:\n")
    stud["branch"]=input("Enter branch:\n")
    stud["roll no"]=int(input("Enter roll no:\n"))
    studlist.append(stud)
print("Name  Branch  Roll no")
print()
print()
for i in range(0,n):
    print(studlist[i])

