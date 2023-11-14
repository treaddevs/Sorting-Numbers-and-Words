# Sam Treadwell
# 9/21/2022
# Fall 2022, CS 5001
# Sorting three numbers from largest to smallest

# Since we are dealing with numbers we use the integer function
        
def main():
    print("This program sorts three numbers from largest to smallest")
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
# Now we determine which number is largest and which is smallest
# This the three conditional method
    if a >= b and b >= c:
        print(a, "is the biggest number")
        print(c, "is the smallest number")
    elif a >= c and c > b:
        print(a, "is the biggest number")
        print(b, "is the smallest number")
    elif b > a and a > c:
        print(b, "is the biggest number")
        print(c, "is the smallest number")
    elif b > c and c > a:
        print(b, "is the biggest number")
        print(a, "is the smallest number")
    elif c > a and a > b:
        print(c, "is the biggest number")
        print(b, "is the smallest number")
    elif c > b and b > a:
        print(c, "is the biggest number")
        print(a, "is the smallest number")
# Lastly, we take the average of the three numbers that were entered
    average = (a + b + c) / 3
    print("The average of the numbers is: " + str(average))
main()