# Additional task #1
# Variation: 372819 % 6 = 3
# This program returns alphabetically all the surnames found in a text
import re

filename: str = input("Enter the name of the file to read: ")
file = open(filename, "r")
text = file.read()
print("\nText from file \'" + filename + "\':\n" + text)

match = r"([А-ЯA-Z][-а-яa-z]*)\s*[А-ЯA-Z][\.\s]*[А-ЯA-Z]\."
surname_list = re.findall(match, text)
surname_list.sort()
print("\nList of surnames: ")
for x in range(len(surname_list)):
    print(surname_list[x])
