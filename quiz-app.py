import random

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
        
    def checkAnswer(self, answer):
        if answer not in self.choices:
            raise ValueError("warning")
        return self.answer == answer
    
class Quiz:
    def __init__(self, questions):
        self.questions = random.sample(questions, len(questions))
        self.questionIndex = 0
        
    def getQuestion(self):
        return self.questions[self.questionIndex]
        
    def displayQuestion(self):
        question = self.getQuestion()
        
        print(f"question {self.questionIndex + 1}: {question.text}")
        
        for q in question.choices:
            print("-" + q)
            
        
q1 = Question("Which is the best programming language.", ["python", "c#", "java", "dart"], "python")
q2 = Question("Which is the most popular programming language?", ["python", "c#", "java", "dart"], "python")
q3 = Question("Which is the most profitable programming language?", ["python", "c#", "java", "dart"], "python")    

questions = [q1, q2, q3]

quiz = Quiz(questions)

print(quiz.displayQuestion())