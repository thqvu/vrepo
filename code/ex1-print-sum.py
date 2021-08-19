'''
print("Hello World")
print("First Number:")
first_number = int(input())
print("Second Number:")
second_number = int(input())
sum = first_number + second_number
print("Sum: " + str(sum))
'''
print("Today's date?")
day = input()
print("Breakfast calories?")
breakfast = int(input())
print("Lunch calories?")
lunch = int(input())
print("dinner calories?")
dinner = int(input())
print("snack calories?")
snack = int(input())
sum = breakfast + lunch + dinner + snack
print("Calorie content for", day + ": " + str(sum))