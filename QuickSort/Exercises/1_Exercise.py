print("Enter a array of numbers with a comma in between and find the sum of all numbers.")
user_input = str(input("Eg - 2,3,4 :: "))
x = user_input.split(",")
x = list(map(int, x))

def recursive_sum(x):
    for i in list(x):
        print(i)

recursive_sum(x)
