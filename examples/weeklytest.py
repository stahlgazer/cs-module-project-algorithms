# Print out all of the numbers in the following array that are divisible by 3:
divis = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# The expected output for the above input is:
# 27
# 81
# 9
# 27
# 99
# 63
# 42
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# modulo
# for loop
for item in divis:
    if item%3 == 0:
        print(item)
    else: pass