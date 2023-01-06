{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18629c6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Bank:\n",
    "\tdef _init_(self):\n",
    "    \t\tself.balance=0\n",
    "    \t\tprint(\"__Create an Account__\")\n",
    "    \t\tself.name=input(\"Enter the name :\")\n",
    "    \t\tself.acctno=int(input(\"Enter the account number :\"))\n",
    "    \t\tself.typeofac=input(\"Enter the type of account :\")\n",
    "\tdef deposit(self):\n",
    "    \t\tamount=int(input(\"Enter the amount to be deposited :\"))\n",
    "    \t\tself.balance += amount\n",
    "    \t\tprint(\"Amount Deposited :\",amount)\n",
    "\tdef withdraw(self):\n",
    "    \t\tamount=int(input(\"Enter the amount to be withdrawn :\"))\n",
    "    \t\tif self.balance >= amount:\n",
    "        \t\tself.balance-=amount\n",
    "    \t   \t\tprint(\"Amount Withdrawn :\", amount)\n",
    "    \t\telse:\n",
    "        \t\tprint(\"Insufficient balance!\")\n",
    "\tdef display(self):\n",
    "    \t\tprint(\"Account Balance :\",self.balance)\n",
    "a=Bank()\n",
    "a._init_()\n",
    "while(1):\n",
    "\tprint(\"\\n1.Deposit\\n2.Withdrawal\\n3.Balance\\n4.Exit\\n\")\n",
    "\tch=int(input(\"Enter your choice :\"))\n",
    "\tif ch==1:\n",
    "    \t\ta.deposit()\n",
    "\telif ch==2:\n",
    "    \t\ta.withdraw()\n",
    "\telif ch==3:\n",
    "    \t\ta.display()\n",
    "\telse:\n",
    "    \t\tprint(\"Wrong Choice!\")\n",
    "    \t\texit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f93076a",
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
