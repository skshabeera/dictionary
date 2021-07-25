import random
teamA={"p1":"a","p2":"b","p3":"c","p4":"d","p5":"e","p6":"f","p7":"g","p8":"h","p9":"i","p10":"j","p11":"k"}
teamB={"p1":"A","p2":"B","p3":"C","p4":"D","p5":"E","p6":"F","p7":"G","p8":"H","p9":"I","p10":"J","p11":"K"}
types_of_ball=["wideball","noball","spin","offspin"]
types_of_score=["out",1,2,3,4,6,0]
print("teamA is going to start")
score=0
wicketsteamA=0
ball=0
over=1
firstover=1
while firstover<=over:
    count_of_ball=1
    while count_of_ball<=6:
        random_ball_num=random.randint(0,3)
        k=count_of_ball
        kaunsaball=types_of_ball[random_ball_num]
        userInput=input("please hit the ball")
        if userInput=="yes":
            if kaunsaball=="wideball" or kaunsaball=="noball":
                print("ye",kaunsaball,"hian")
                score+=1
                count_of_ball=k
            else:
                print("ye",kaunsaball,"hian")
                randomscoreno=random.randint(0,6)
                how_much_score=types_of_score[randomscoreno]
                if how_much_score=="out":
                    wicketsteamA+=1
                else:
                    score+=how_much_score
                count_of_ball+=1
            print("Total-score",score,"wicketsteamA",wicketsteamA,"Total-overs",over,"cureent-over",firstover,"which ball",count_of_ball)
            print(score)    
        else:
            count_of_ball=k

    firstover+=1 

teamB={"p1":"A","p2":"B","p3":"C","p4":"D","p5":"E","p6":"F","p7":"G","p8":"H","p9":"I","p10":"J","p11":"K"}
types_of_ballB=["wideball","noball","spin","offspin"]
types_of_scoreB=["out",1,2,3,4,6,0]
print("teamB is going to start")
scoreB=0
wicketsteamB=0
ballB=0
overB=1
firstoverB=1
while firstoverB<=overB:
    count_of_ballB=1
    while count_of_ballB<=6:
        random_ball_numB=random.randint(0,3)
        J=count_of_ballB
        kaunsaballB=types_of_ballB[random_ball_numB]
        userInput=input("please hit the ball")
        if userInput=="yes":
            if kaunsaballB=="wideball" or kaunsaballB=="noball":
                print("ye",kaunsaballB,"hian")
                scoreB+=1
                count_of_ballB=J
            else:
                print("ye",kaunsaballB,"hian")
                randomscorenoB=random.randint(0,6)
                how_much_scoreB=types_of_scoreB[randomscorenoB]
                if how_much_scoreB=="out":
                    wicketsteamB+=1
                else:
                    scoreB+=how_much_scoreB
                count_of_ballB+=1
            print("Total-score",scoreB,"wicketsteamA",wicketsteamB,"Total-overs",overB,"cureent-over",firstoverB,"which ball",count_of_ballB)
            print(scoreB)    
        else:
            count_of_ballB=J
    firstoverB+=1
if score>scoreB:
    print("teamA won the match")
elif scoreB>score:
    print("teamB won the match")
else:
    print("draw the match")