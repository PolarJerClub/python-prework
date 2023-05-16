#Question 1

def hello_name(user_name):
    print(f"hello_{user_name.upper()}!")

hello_name("username")

#Question 2

def first_odds():
    for num in range(1,101):
        if num % 2 == 1:
            print(num)
print(first_odds())

#Question 3

def max_num_in_list(a_list):
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num
a_list = [1,1000000, 88, 1234, 9209, 411, 9,999999999]
print("maxboii",max_num_in_list(a_list))

#Question 4

def is_leap_year(a_year):
  if a_year % 4 == 0:
    return True
  if a_year % 100 != 0:
    return True
  if a_year % 400 == 0:
    return True
  else:
    return False
a_year = 1984
if is_leap_year(a_year):
  print("It's a leap year!?!")
else:
  print("Nope.")

#Question 5

def is_consecutive(a_list):
    a_list.sort()
    for num in range(len(a_list) - 1):
        if a_list[num] + 1 != a_list[num + 1]:
            return False
    return True
a_list = [1,2,3,4]
print(is_consecutive(a_list))