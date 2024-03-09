# Variation:
# Eyes 372819 % 5 = 4 "="
# Nose 372819 % 4 = 3 "<{"
# Mouth 372819 % 7 = 6 "P"
# This program count the amount of times "=<{P" appears in text'
import re

filename: str = input("Enter the name of the file to read: ")
file = open(filename, "r")
text = file.read()
print("\nText from file \'" + filename + "\':\n" + text)

match = r"=<{P"
matches = re.findall(match, text)
count = len(matches)
print("The amount of times =<{P appeared: ", count)
