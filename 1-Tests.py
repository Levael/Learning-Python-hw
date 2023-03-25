s = input("Name: ")

s = s.strip()    # from spaces
index = s.find((s[1:].strip(s.lower())))
print(s[:index].strip(), s[index:].strip())