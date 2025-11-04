# name="Anurag"
# new_list=[letter for letter in name]
# print(new_list)
#
# double_list=[n*2 for n in range(1,5)]
# print(double_list)

#
# names=["Anurag", "soumya", "Angela", "Golu", "molu"]
# #
# # new_list=[name for name in names if len(name)<5]
# # print(new_list)
# upper_name =[name.upper() for name in names if len(name)>5]
# print(upper_name)

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
#
# numbers = [int(n) for n in list_of_strings]
# print(numbers)
# even_list = [n for n in numbers if n % 2 == 0]
# print(even_list)
#
# with open("file1.txt") as file1:
#     file1_numbers = [int(line.strip()) for line in file1]
#
# with open("file2.txt") as file2:
#     file2_numbers = [int(line.strip()) for line in file2]
#
# # Use list comprehension to find common elements
# result = [num for num in file1_numbers if num in file2_numbers]
#
# print(result)

"""Dictionary comprehension """
# import random
# names = ["Anurag", "soumya", "Angela", "Golu", "molu"]
# score_dict={name:random.randint(10,100) for name in names}
#
# print(score_dict)
#
# passed={name:marks for name,marks in score_dict.items() if marks>60}
# print(passed)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f={day:int(temp)*9/5 +32 for day,temp in weather_c.items()}
# print(weather_f)

# student_dict={
#     "student":["Angela", "James","Lily"],
#     "score":[56,78,98]
# }
#
# for (value) in student_dict.values():
#
#     print(value)