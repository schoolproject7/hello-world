filename = input('Enter file name here: ')
lines = []
with open(filename, 'r') as f:
    for line in f:
        lines.append(line.strip())

while True:
    print("The file has", len(lines), "lines")
    if len(lines) == 0:
        break
    lineNum = int(input("Enter a line number here: "))
    if lineNum == 0:
        break
    elif lineNum > len(lines):
        print("ERROR")
    else:
        print(lineNum, ": ", lines[lineNum - 1])
