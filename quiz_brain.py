import html

class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list 
        self.score=0  

    def nextQuestion(self):
        self.current_question=self.question_list[self.question_number]
        self.question_number+=1
        q_text=html.unescape(self.current_question.text)
        # user_answer=input(f"Q.{self.question_number}: {q_text} (True/False): ") 
        return f"Q.{self.question_number}: {q_text}"
        # self.check_answer(user_answer)

    def still_has_question(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            False

    def check_answer(self,user_answer):
        correct_answer=self.current_question.answer
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            return True
        else:
            return False
