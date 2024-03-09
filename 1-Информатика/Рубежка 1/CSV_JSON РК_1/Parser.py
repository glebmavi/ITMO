inputFile = open("input", "r")
inputText = inputFile.read()


inputText = inputText.split("\n")
outputText = '['

for i in inputText:
    if i == inputText[0]:
        i = i.partition(',')
        key = i[0]
        data = i[2]
    else:
        i = i.partition(',')
        outputText += '\n\t{' + '\n\t\t' + key + ': ' + i[0] + ',\n\t\t' + data + ': ' + i[2] + '\n\t},'


outputFile = open("output.txt", "w")
outputFile.write(outputText)
