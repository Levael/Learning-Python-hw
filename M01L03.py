s = input("Name: ")

s = s.strip()    # from spaces
index = s[1:].find((s[1:].strip(s.lower()))) + 1
print(s[:index].strip(), s[index:].strip())

# 1) trim from both sides spaces
# 2) find first letter of Last Name index by subtracting the lowed line from the original
# 3) in case of spaces between: join First Name and Second Name with trim on both sides
