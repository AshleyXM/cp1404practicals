NAME_FILENAME = "name.txt"

"""
1. Write code that asks the user for their name, then opens a file called name.txt
and writes that name to it. Use open and close for this question.
"""
name = input("Enter your name: ")
out_file = open(NAME_FILENAME, "w")
print(name, file=out_file)
out_file.close()

"""
2. In the same file, but as if it were a separate program, write code that opens "name.txt"
and reads the name (as above) then prints (note the exact output),
Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable!
Use open and close for this question.
"""
in_file = open(NAME_FILENAME, "r")
name = in_file.read().strip("\n")
print(f"Hi {name}!")
in_file.close()


NUMBER_FILENAME = "numbers.txt"
"""
3. Write code that opens numbers.txt, reads only the first two numbers, 
adds them together then prints the result, which should be... 59. 
Use with instead of open and close for this question.
"""
with open(NUMBER_FILENAME, "r") as in_file:
    num1 = int(in_file.readline().strip("\n"))  # the number on line 1
    num2 = int(in_file.readline().strip("\n"))  # the number on line 2
    print(num1 + num2)


"""
4. Now write a fourth block of code that prints the total for all lines in numbers.txt.
This should work for a file with any number of numbers.
Use with instead of open and close for this question.
"""
with open(NUMBER_FILENAME, "r") as in_file:
    total = 0
    for line in in_file:
        num = int(line.strip("\n"))
        total += num
    print(total)