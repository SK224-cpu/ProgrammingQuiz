from ReadCSV import CreateQuestion

readCSV ="data/csv_text_csv.csv"
updateCSV ="data/RemovedQuestions/Removed_ques.csv"
str=CreateQuestion(readCSV, updateCSV)
print(str)