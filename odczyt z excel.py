file = open("countries.xls")
for line in file.readlines():
    print(line)
file.close
