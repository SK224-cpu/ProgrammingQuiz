import csv
import random
def CreateQuestion(readCSV,removeCSV):
    questionList = []
    
    try:
        with open( readCSV, "r",encoding="utf-8" ) as Read_CSV:
            CSV_File_Var_555=csv.reader(Read_CSV)
            for i in CSV_File_Var_555:
                questionList.append(i)
            #print(len(questionList))

        if len(questionList) >0:
            RandomQue = random.choice(questionList)
            #print(RandomQue)

            questionList.remove(RandomQue)
            #print(len(questionList))

            with open(readCSV, "w",encoding="utf-8" , newline='' ) as Write_CSV:
                writer = csv.writer(Write_CSV)
                for i in questionList:
                    writer.writerow(i)

            with open( removeCSV, "a",encoding="utf-8",newline='' ) as Update_CSV:
                update = csv.writer(Update_CSV)
                update.writerow(RandomQue)
            return RandomQue
        else:
            return "No Questions in the List"
    except FileNotFoundError:
        return("Check file name!")
    except Exception:
        return("Check files, access, priviledge...")
        




        



