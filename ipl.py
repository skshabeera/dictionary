import random
TeamA={"player1":"shabeera","player2":"somi","player3":"shirisha","player4":"sindhu","player5":"anusha","player6":"jyothi","player7":"pinky","player8":"shailaja","player9":"laxmi","player10":"sowjanya","palyer11":"jhansi"}
TeamB={"player1":"nayak","player2":"kumar","player3":"shireen","player4":"sandhya","player5":"navya","player6":"manjula","player7":"sarika","player8":"mamatha","player9":"thanjum","player10":"muskhan","player11":"nagendra"}
types_of_ball=["wideball","noball","spin","offspin"]
types_of_score=["out",1,2,3,4,6,0]
print("teamA is going to start")
scoreA=0
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
        whichball=types_of_ball[random_ball_num]
        userInput=input("please hit the ball")
        if userInput=="yes":
            if whichball=="wideball" or whichball=="noball":
                print("the",whichball,"is")
                score+=1
                count_of_ball=k
                print("the",whichball,"is")
            randomscoreno=random.randint(0,6)
            how_much_score=types_of_score[randomscoreno]
            if how_much_score=="out":
                wicketsteamA+=1
            else:
                score+=how_much_score
            count_of_ball+=1
        print("Total-score",score,scoreA,"wicketsteamA",wicketsteamA,"Total-overs",over,"cureent-over",firstover,"which ball",count_of_ball)    
    else:
        count_of_ball=k
    firstover+=1 

TeamB={"player1":"nayak","player2":"kumar","player3":"shireen","player4":"sandhya","player5":"navya","player6":"manjula","player7":"sarika","player8":"mamatha","player9":"thanjum","player10":"muskhan","player11":"nagendra"}
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
        else:
            count_of_ballB=J
    firstoverB+=1
if score>scoreB:
    print("teamA won the match")
elif scoreB>score:
    print("teamB won the match")
else:
    print("draw the match")