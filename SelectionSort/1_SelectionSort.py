def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


user_input = str(input("Enter a list of number separated by space in between. Eg: 3 5 78 93 2 :: "))

x = user_input.split(",")
x = list(map(int, x))
print("The list that you entered is::\n", x, "\n and it's length is :: ", len(x))

y = selectionSort(x)
print("Output :: \n", y , "\n and it's length is :: ", len(y))

