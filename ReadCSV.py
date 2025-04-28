import csv

readCSV ="C:\\Users\\Shruti\\OneDrive\\Desktop\\Python Shruti Folder\\csv_text_csv.csv"
with open( readCSV, "r",encoding="utf-8" ) as Read_CSV:
    CSV_File_Var=csv.reader(Read_CSV)
    for i in CSV_File_Var:
        print(i)
