rev = 0 
num = int(input("Enter the number:")) 
temp = num 
n=str(temp) 
while num > 0: 
digit = num%10 
rev = rev*10+digit 
num //= 10    
print("Given Number is", temp) 
print("Reversed Number is", rev) 
if temp == rev: 
print(temp, "is a Palindrome") 
else: 
print(temp, "is not a Palindrome") 
# Finding Number of Digits using built-in function 
print("Number of Digits using Built-in Function: ", len(str(n))) 
#Finding the occurrences of each digit 
s={} 
for i in n: 
if i in s: 
s[i]+=1 
else: 
s[i]=1 
print("Number of occurrences of each digit in the input number are:") 
print(s) 
