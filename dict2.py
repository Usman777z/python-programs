{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a9ac2089",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of students:3\n",
      "Enter name:\n",
      "thasnm\n",
      "Enter branch:\n",
      "mca\n",
      "Enter roll no:\n",
      "29\n",
      "Enter name:\n",
      "usmn\n",
      "Enter branch:\n",
      "cs\n",
      "Enter roll no:\n",
      "12\n",
      "Enter name:\n",
      "mrdhl\n",
      "Enter branch:\n",
      "mech\n",
      "Enter roll no:\n",
      "34\n",
      "Name  Branch  Roll no\n",
      "\n",
      "\n",
      "{'name': 'thasnm', 'branch': 'mca', 'roll no': 29}\n",
      "{'name': 'usmn', 'branch': 'cs', 'roll no': 12}\n",
      "{'name': 'mrdhl', 'branch': 'mech', 'roll no': 34}\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"Enter the number of students:\"))\n",
    "studlist=[]\n",
    "for i in range(0,n):\n",
    "    stud={}\n",
    "    stud['name']=input(\"Enter name:\\n\")\n",
    "    stud[\"branch\"]=input(\"Enter branch:\\n\")\n",
    "    stud[\"roll no\"]=int(input(\"Enter roll no:\\n\"))\n",
    "    studlist.append(stud)\n",
    "print(\"Name  Branch  Roll no\")\n",
    "print()\n",
    "print()\n",
    "for i in range(0,n):\n",
    "    print(studlist[i])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0fded5dc",
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
