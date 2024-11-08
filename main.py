import sys
#Algorithm_1: If the entered number is greater than 7, then print “Hello”

print('Enter any unmber, please!')
input_number = int(input())
if input_number > 7:
    print('Hello')
else:
    sys.exit(0)


#Algorithm_2: If the entered name matches “John”, then output “Hello, John”, if not, then output "There is no such name"
name = input("Enter your name: ")
if name == "John" or name == "john":
    print("Hello, John")
else:
    print("There is no such name")



#Algorithm_3: There is a numeric array at the input, it is necessary to output array elements that are multiples of 3

arr = list(map(int, input("Enter numbers separated by the space: ").split()))
num_mult_of_3 = []
for num in arr:
    if num % 3 == 0:
        num_mult_of_3.append(num)
print("There are numbers multiples of 3:", *num_mult_of_3, sep=' ')






#Answer the questions
#Given bracket sequence: [((())()(())]]
#Can this sequence be considered correct?
#If the answer to the previous question is “no”, then what needs to be changed in it to make it correct?

# We need to check if every opening bracket has a closing bracket and that the brackets are properly nested.
# In our case we have: 1 opening bracket '[', 2 closing brackets ']', 6 opening brackets '(' and 5 closing brackets ')'
# So the sequence is not correct because the initial two brackets are unmatched: closing ']' and opening '('.
# We should put one opening '[' at the begining and one closing bracket ')' to make the sequence correct.
