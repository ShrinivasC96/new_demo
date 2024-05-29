'''
program to add sum of 1 to 50 odd numbers
'''
sum_of_odd = 0

for i in range(1,50,2):
  sum_of_odd += i
print("The sum of odd numbers from 1 to 50 is : ", sum_of_odd)  


'''
program to add sum of 1 to 50 even numbers
'''
sum_of_even = 0

for i in range(2,51,2):
  sum_of_even += i
print("The sum of even numbers from 1 to 50 is : ", sum_of_even)

'''
program the nummber multiple of 7
'''

n = 7
num = 0
for i in range(1,11,1):
  num = n * i
  print("The multiple of 7 is :", num)  
