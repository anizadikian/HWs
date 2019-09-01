def input_list():
    input_list = []
    n = int(input("How many numbers you want to include in your list?  "))
    for i in range(0, n):
        while True:
            number = (input('Please enter a number: '))
            if (number.isdigit()):
                input_list.append(number)
                break
            else:
                print("Please input a number, such as 1, 2, 3...")
def sum ():
    sum = 0 #I dont know here how we can make the operation of adding to create a new list
    for i in range(n):
        i = i + sum
        sum = i
        input_list.append(number)
    print(input_list())

def main():

    list = input_list()
    sum(list)

main()
