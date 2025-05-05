from ReadCSV import CreateQuestion
import datetime

def Consolidated():
    #calling Q1
    readCSV_Coding_test ="data/csv_text_csv.csv"
    removeCSV_Coding_test = "data/RemovedQuestions/"
    question1=CreateQuestion(readCSV_Coding_test, removeCSV_Coding_test)

    #calling Q2
    readCSV_Concepts_test ="data/Programming_Test.csv"
    removeCSV_Concepts_test ="data/RemovedQuestions/programming_quiz.csv"
    question2=CreateQuestion(readCSV_Concepts_test, removeCSV_Concepts_test)

    #calling Q3
    readCSV_Quiz_test ="data/Coding_quiz.csv"
    removeCSV_Quiz_test ="data/RemovedQuestions/removed_coding_quiz.csv"
    question3 = CreateQuestion(readCSV_Quiz_test, removeCSV_Quiz_test)

    return (
    f"Today's {datetime.datetime.now().date()} question paper:\n"
    f"Q1. {question1}\n"
    f"Q2. {question2}\n"
    f"Q3. {question3}\n"
    "Good Luck!"
)


