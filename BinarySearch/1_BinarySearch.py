def binary_search(list, item):
    low = 0 #lowest index
    high = len(list) - 1 #highest index

    while low<=high:
        mid = (low + high)//2 #find the middle value
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = low + 1
    return None

user_input = str(input("Enter the range you want in the list with a '-' in between. Eg: 10-30 :: "))

x = user_input.split("-")

num1 = int(x[0])
num2 = int(x[1])

my_list = []

if num1<num2:
    for y in range(num1, num2 + 1):
        my_list.append(y)
    print("The List according to your input :: ",my_list)

user_search = int(input("Enter the nyumber you want to search in the list :: "))

output = binary_search(my_list, user_search)
print("The number you searched is at index {}".format(output))
