import calendar
import sys
m = int(sys.argv[1])
y = int(sys.argv[2])
for i in range(1, calendar.monthrange(y, m)[1]):
    if calendar.weekday(2019, m, i) == 4:
        str1 = "\"" + str(m) + "/" + str(i) + "/" + str(y) + ", 10am\" "
        str2 = "\"" + str(m) + "/" + str(i) + "/" + str(y) + ", 11am\" "
        str3 = "\"" + str(m) + "/" + str(i) + "/" + str(y) + ", 12pm\" "
        str4 = "\"" + str(m) + "/" + str(i) + "/" + str(y) + ", 1pm\" "
        print(str1 + str2 + str3 + str4, end="")
	print("")
