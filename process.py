#opens the txt file so we can access and use it in our code in procces.py and stores that into a variable called log_file
log_file = open("um-server-01.txt")

#defines a function called sales_reports that takes in the argument log_file
def sales_reports(log_file):
#starts a for loop to loop over lines of data in log_file
    for line in log_file:
        #removes trailing white space from the right side
        line = line.rstrip()
        #pulls the value at index of zero and stores it into variable day
        day = line[0:3]
        #if statement saying if that value is equal to Tue
        if day == "Tue":
            #to print out the entire line
            print(line)

#function invoked
sales_reports(log_file)
