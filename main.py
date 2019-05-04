toTranslate = {}
translationBase = {}

key = None

toTranslateFile = "toTranslate.txt"
translationBaseFile = "translationBase.txt"
resultFile = open("result.txt", "w")
otherFile = open("other.txt", "w")


with open(toTranslateFile, "r", encoding="1252") as toTranslateFile:
	for line in toTranslateFile:
		if line != "" or line != "\n":
			if key == None:
				line = line.split('"')
				print(line)
				if len(line) >= 2:
					key = line[1]
			else:
				toTranslate[key] = line
				key = None

with open(translationBaseFile, "r", encoding="1252") as translationBaseFile:
	for line in translationBaseFile:
		if line != "":
			if key == None:
				line = line.split('"')
				key = line[1]
			else:
				translationBase[key] = line[1:-3]
				key = None


for key in toTranslate:
	if key in translationBase:
		resultFile.write('"' + key + '"\n"' + translationBase[key] + '";\n\n')
	else:
		otherFile.write('"' + key + '"\n"' + toTranslate[key] + '";\n\n')

