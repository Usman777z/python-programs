{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f8c865f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of students:3\n",
      "Enter name:thsnm\n",
      "Enter roll number:12\n",
      "Enter attendance percentage:89\n",
      "Enter name:usmn\n",
      "Enter roll number:9\n",
      "Enter attendance percentage:75\n",
      "Enter name:junm\n",
      "Enter roll number:8\n",
      "Enter attendance percentage:80\n",
      "Attendance list\n",
      "{'Name': 'thsnm', 'Roll No': 12, 'Attendance': 89}\n",
      "{'Name': 'junm', 'Roll No': 8, 'Attendance': 80}\n",
      "{'Name': 'usmn', 'Roll No': 9, 'Attendance': 75}\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"Enter the number of students:\"))\n",
    "studlist=[]\n",
    "for i in range(0,n):\n",
    "    stud={}\n",
    "    stud[\"Name\"]=input(\"Enter name:\")\n",
    "    stud[\"Roll No\"]=int(input(\"Enter roll number:\"))\n",
    "    stud[\"Attendance\"]=int(input(\"Enter attendance percentage:\"))\n",
    "    studlist.append(stud)\n",
    "for i in range(1,n):\n",
    "    for j in range(0,n-1):\n",
    "        if(studlist[j][\"Attendance\"]<studlist[j+1][\"Attendance\"]):\n",
    "            temp=studlist[j]\n",
    "            studlist[j]=studlist[j+1]\n",
    "            studlist[j+1]=temp\n",
    "print(\"Attendance list\")\n",
    "for i in range(0,n):\n",
    "    print(studlist[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b47e3821",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
