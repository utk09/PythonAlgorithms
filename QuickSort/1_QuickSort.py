def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

# print(quicksort([10,5,3,2,11,32,1]))

user_input = str(input("Enter a list of number separated by comma in between. Eg: 3,5,78,93,2 :: "))

x = user_input.split(",")
x = list(map(int, x))
print("The list that you entered is::\n", x, "\n and it's length is :: ", len(x))

y = quicksort(x)
print("Output :: \n", y , "\n and it's length is :: ", len(y))



    