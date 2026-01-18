sentence = input("Enter a sentence: ") 
word_count = len(sentence.split()) 
digit_count = 0 
upper_count = 0 
lower_count = 0 
for char in sentence:
  if char.isdigit(): 
    digit_count += 1 
  elif char.isupper(): 
    upper_count += 1 
  elif char.islower(): 
    lower_count += 1 
print("Number of words:", word_count) 
print("Number of digits:", digit_count) 
print("Number of uppercase letters:", upper_count) 
print("Number of lowercase letters:", lower_count)
