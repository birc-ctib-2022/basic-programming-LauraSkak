
# You should write a loop around this question, and keep asking until
# the answer is "yes" (lower case).

answer = None

while answer != "yes":
    print("Hello, World!")
    answer = input('Do you want to stop? ')
    if answer == "yes":
        break