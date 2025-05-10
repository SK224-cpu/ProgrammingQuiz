from ReadCSV import CreateQuestion
import datetime
import os
from EmailTemplateHTML import generate_email_html_N_plaintext

dataPath = "data/"
removedDataPath = "data/removedData/"

def CheckDataPathExists():
    if not os.path.exists(dataPath):
        os.makedirs(dataPath)
    if not os.path.exists(removedDataPath):
        os.makedirs(removedDataPath)

def GenerateQuiz(question_sources):
    CheckDataPathExists()
    question_texts = []
    for idx, (inputCSV, removedCSV, question_description) in enumerate(question_sources, start=1):
        realtiveDataPath = os.path.join(dataPath, inputCSV)
        realtiveRemovedDataPath = os.path.join(removedDataPath, removedCSV)
        question = CreateQuestion(realtiveDataPath, realtiveRemovedDataPath)
        question_texts.append((question_description, idx, question[0].strip().strip('"')))
    return question_texts
        