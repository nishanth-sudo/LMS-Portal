Add the corresponding elements of 2  N element arrays/lists
For example:
Input	
5
10 20 30 40 50
1 2 3 4 5
Result
11 22 33 44 55

Code:
    n=int(input())
    a1=[int(x) for x in input().split()]
    a2=[int(x) for x in input().split()]
    for i in range(n):
        print(a1[i]+a2[i],end=' ')

Check if a given number is a binary number or not.
NOTE: A binary number has only 0 and 1.
Input:
101
Output:
Yes
Input:
203
Output:
No

Code:
 s=input()
 if all(c in '01' for c in s):
    print("Yes")
 else:
    print("No")

Write a program that display equal positive and negative numbers for a given number
Zero should not be displayed
For example:
Input	
6
Result
3 2 1 -1 -2 -3
10
Result
5 4 3 2 1 -1 -2 -3 -4 -5

Code:
#include<stdio.h>
int main(){
    int num,i;
    scanf("%d",&num);
    if (num == 0){
        printf("invalid");
    }
    else{
        for(i=num/2;i>=1;i--){
            printf("%d ",i);
        }
        for(i=-1;i>= -num/2;i--){
            printf("%d ",i);
        } 
        printf("\n");
    }
}
