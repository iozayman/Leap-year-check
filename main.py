# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check?\n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


r4 = year % 4
r100 = year % 100
r400 = year % 400

if r4 == 0 and r100 != 0 or r400 == 0:
  print("Leap year.")
else:
  print("Not leap year.")