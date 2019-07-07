print("Enter a array of numbers with a comma in between and find the sum of all numbers recursively")
user_input = str(input("Eg - 2,3,4 :: "))
x = user_input.split(",")
x = list(map(int, x))


def recursive_sum(list):
    if list == []:
        return 0
    return list[0] + recursive_sum(list[1:])


print(recursive_sum(x))
