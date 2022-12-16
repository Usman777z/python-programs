{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "02184eb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of students:4\n",
      "Enter name:thasnm\n",
      "Enter the mark:90\n",
      "Enter name:usmn\n",
      "Enter the mark:89\n",
      "Enter name:mrdhl\n",
      "Enter the mark:100\n",
      "Enter name:gokl\n",
      "Enter the mark:78\n",
      "{'thasnm': 90, 'usmn': 89, 'mrdhl': 100, 'gokl': 78}\n",
      "['gokl', 'usmn', 'thasnm', 'mrdhl']\n",
      "gokl  78\n",
      "usmn  89\n",
      "thasnm  90\n",
      "mrdhl  100\n"
     ]
    }
   ],
   "source": [
    "stud={}\n",
    "n=int(input(\"Enter the number of students:\"))\n",
    "for i in range(n):\n",
    "        a=input(\"Enter name:\")\n",
    "        stud[a]=int(input(\"Enter the mark:\"))\n",
    "mark=[] \n",
    "print(stud)\n",
    "mark+=stud.values()\n",
    "mark.sort()\n",
    "a=[]\n",
    "for i in mark:\n",
    "    for k,v in stud.items():\n",
    "        if(i==v):\n",
    "            a.append(str(k))\n",
    "print(a)\n",
    "for i in range(n):\n",
    "        print(\"%s  %d\" %(a[i],stud[a[i]]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc3306a8",
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
