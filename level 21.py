Write a program to find the first digit in a given number
For example:
Input	Result
30    3
4056  4
Code:
  print(input()[0])

Write a program to count the number of digits in a given number
For example:
Input	Result
7896  4
Code:
  print(len(input()))

You are given a number N. Find the total count of set bits. First covert the number to binary and count the number of 1s in the number. That is the number of set bits.
In this program you have to count the number of set bits from 1 to the given number. For example if the input is 5
    1 - 01 - 1 set bit
    2 - 10 - 1 set bit
    3 - 11 - 2 set bits
    4 - 100 - 1 set bit
    5 - 101 - 2 set bits
So totally 7 should be the answer
If the input is 4 then the number of set bits would be 5
Input Format
The first line of input contains an integer T denoting the number of test cases. Testcases follow. The first line of each test case is N.
Constraints
1 <= T <= 100 1 <= N <= 103
Output Format
For each testcase, in a new line, print the total count of all bits
For example:
Input	Result
1     5
4
Code:
    T = int(input())
    for _ in range(T):
        n =int(input())
        c=0
        for i in range(1,n+1):
            b=i
            while b:
                b&=(b-1)
                c+=1
        print(c)


input
341
Result:
3
4 
1

Code:
  for i in input():
    print(i)
