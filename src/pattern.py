
# Print the pattern


string = ""

for i in range(1, 10, 1):
    if i <= 5:
        string = "* "*(i-1)
        string = f"{string}*"
        print(string)
    else:
        string = "* "*(i-1-(i-5)*2)
        string = f"{string}*"
        print(string)
