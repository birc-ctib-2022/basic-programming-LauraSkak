import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
has_lower = False
has_upper = False
has_special = False

for i in password:
    if i.isupper():
        has_upper = True
    elif i.islower():
        has_lower = True
    elif i in "$#@":
        has_special = True
    if has_lower and has_upper and has_special and 6<=len(password)<=16:
        is_valid = True
        break


print(is_valid)
