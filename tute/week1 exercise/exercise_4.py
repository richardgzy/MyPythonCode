# Q4

dic = {"01" : "January", "02" : "Feburary", "03" : "March", "04" : "April", "05" : "May"\
    , "06" : "June", "07" : "July", "08" : "August", "09" : "September", "10" : "Octotber"\
       , "11" : "November", "12" : "December"}
input = input("Please input a date in format DD/MM/YYYY:")
stringset = input.split("/")
if stringset[0] not in (1, 32) or stringset[1] not in (1, 13): # how to validate the year?
    print("Invalid Input")
else:
    month = dic[stringset[1]]
    date = stringset[0]
    year = stringset[2]
    print("%s %s %s" % (month, date, year))