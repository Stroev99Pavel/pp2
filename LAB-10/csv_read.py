import csv
filename = 'students.csv'
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        #print(row) #['Pavel', '24B031901', '1', '+77472460872']
                   #['Viktor', '24B031902', '1', '+77473460871']
        name,id,study_year,phone_number = row
        # print(name,id,study_year,phone_number) #Pavel 24B031901 1 +77472460872
                                                 # Viktor 24B031902 1 +77473460871