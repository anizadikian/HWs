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
                print("Please input a number")
def sum ():
    sum = 0 #I dont know here how we can make the operation of adding to create a new list
    for number in input_list():
        sum = sum + number
        return sum

def main():

    input_list()
    sum()
    
main()
