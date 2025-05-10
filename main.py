from CreateQuiz import GenerateQuiz
from EmailTemplateHTML import generate_email_html_N_plaintext
from SendEmail import SendEmail
import sys

def SendQuizToSubscribers(name, emailId):
    concept_descp = "<div style='margin-bottom: 20px;'><h4 style='color: #2c3e50;'>🧠 Concept Mastery</h4><p style='font-size: 16px; color: #333;'>Explain the concept given below in your own words. Include real-world scenarios where this concept can be applied, and demonstrate its use with a simple code example. This will help you internalize how and when to use the concept effectively.</p></div>"
    traceCode_descp = "<div style='margin-bottom: 20px;''><h4 style='color: #2c3e50;'>🔍 Trace the Code</h4><p style='font-size: 16px; color: #333;'>Review the given code snippet carefully. Analyze how it runs, and try to predict its final output <strong>without running it</strong>. This sharpens your logic and debugging skills, which are essential for all developers.</p></div>"
    solveNCode_descp = '<div style="margin-bottom: 20px;"><h4 style="color: #2c3e50;">💡 Solve &amp; Code</h4><p style="font-size: 16px; color: #333;">Read the problem statement thoroughly and write a Python program that solves it. Focus on correct logic, clean structure, and test your solution with different inputs. This helps you become a confident problem solver.</p></div>'
    question_sources = [
        ("ProgrammingConceptsRevision.csv","ProgrammingConceptsRevisionRemoved.csv",concept_descp),
        ("programmingquiz.csv","programmingquizRemoved.csv",traceCode_descp),
        ("ProgrammingTasks.csv","ProgrammingTasksRemoved.csv",solveNCode_descp)
        ]
    quizQuestions = GenerateQuiz(question_sources)
    quizEmailTemplate = generate_email_html_N_plaintext(name, quizQuestions)
    SendEmail(quizEmailTemplate[0], quizEmailTemplate[1], emailId)
    print("Quiz sent successfully!")
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <name> <email>")
        sys.exit(1)
    SendQuizToSubscribers(sys.argv[1], sys.argv[2])
