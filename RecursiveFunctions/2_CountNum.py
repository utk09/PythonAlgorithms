print("Enter a list of numbers to count the number of items in the list recursively - ")

user_input = str(input("Enter the numbers with a comma in between. Eg. 2,3,5,21 :: "))

x = user_input.split(',')
x = list(map(int, x))

def count_num(list):
    if list == []:
        return 0
    return 1 + count_num(list[1:])

print("The list that you entered is::\n", x)

y = count_num(x)
print("\n And it's length is :: ", y)
