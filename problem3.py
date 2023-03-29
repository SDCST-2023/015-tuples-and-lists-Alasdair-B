#! python3
"""
Ask the user to enter a maximum of 10 positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added

inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""
import math
numbers=[]
def Input():
    for i in range(0,10):
        n = int(input(f"Enter a positive integer ({(10-(i))} spaces remaining), if you have no more numbers to enter, input '-1': "))
        if n == -1:
            return
        else:
            numbers.append(int(n))



Input()
numbers.sort(reverse=True)
print(f"The largest number you entered is {numbers[0]}")
