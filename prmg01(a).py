print("Enter the three internals marks (> zero:") 
m1 = int(input("Enter marks1:")) 
m2 = int(input("Enter marks2:")) 
m3 = int(input("Enter marks3:")) 
print("Marks1:", m1) 
print("Marks2:", m2) 
print("Marks3:", m3)  
small=m1 
if small > m2: 
  small = m2 
if small > m3: 
  small = m3 
avg=(m1+m2+m3-small)/2; 
print("Average of best two test out of three test is",avg)
