m = 1
y = 19
for i in range(1, 32):
    if calendar.weekday(2019, m, i) == 4:
        str1 = "\"" + str(m) + "/" + str(i) + "/" + str(y) + ", 10am\" "
        str2 = "\"" + str(m) + "/" + str(i) + "/" + str(y) + ", 11am\" "
        str3 = "\"" + str(m) + "/" + str(i) + "/" + str(y) + ", 12pm\" "
        str4 = "\"" + str(m) + "/" + str(i) + "/" + str(y) + ", 1pm\" "
        print(str1 + str2 + str3 + str4, end="")

