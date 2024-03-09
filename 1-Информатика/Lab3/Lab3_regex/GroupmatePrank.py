# Additional task #1
# Variation: 372819 % 4 = 3
# This program returns all the names of students that are not
# from your group and don't have the same initials

import re

filename: str = input("Enter the name of the file to read: ")
file = open(filename, "r")
text = file.read()
group: str = input("Enter your group: ")
print("\nText from file \'" + filename + "\':\n" + text)

line = text.split("\n")
line = list(filter(None, line)) #removes empty strings from list
print(line)
S_re = r"^\s*([А-ЯA-Z])"
I_re = r"\s([А-ЯA-Z])\."
O_re = r"\.([А-ЯA-Z])"
G_re = r"P\d+"
S_lst = re.findall(S_re, text, re.MULTILINE)
print(S_lst)
I_lst = re.findall(I_re, text)
print(I_lst)
O_lst = re.findall(O_re, text)
print(O_lst)
G_lst = re.findall(G_re, text)
print(G_lst)

print("Updated list: \n")
for i in range(len(S_lst)):
    if not (S_lst[i] == I_lst[i] == O_lst[i] and G_lst[i] == group):
        print(line[i])
