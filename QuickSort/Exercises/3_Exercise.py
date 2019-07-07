print("Find the Maximum Number in a list using Recursive Function.")

user_input = str(input("Enter a list of numbers separated by commas. Eg: 2,3,4,98 :: "))

x = user_input.split(",")
x = list(map(int, x))

def max_num(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max_num(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print("List you entered is :: ",x)
print("The largest number in List is :: ",max_num(x))