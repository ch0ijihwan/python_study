class score:
    
    math_score = 0
    korean_score = 0
    english = 0

    name = ""

    def __init__(self,w):
        list =  w.split('/')
        self.math_score = int(list[3])
        self.english =int (list[2])
        self.korean_score = int ( list[1])
        self.name = list[0]




    def mean (self):
        mean = (self.math_score + self.english+self.korean_score)/3
        
        print(self.name,"의 시험점수 평균은 ",mean,"이다.")
        return 




    def hap(self):
        hap = self.math_score + self.english+self.korean_score
        
        print(self.name,"의 시험점수 합계은 ",hap,"이다.")
        return 





print("합계와 평균을 구해드립니다.")
a = input("학생의 정보를 입력하세요(이름/국어점수/영어점수/수학점수)")

s1 = score(a)
s1.hap()
s1.mean()

