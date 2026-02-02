# QUIZ GAME:-

questions = ("How many elements in the periodic table?: ",
            "Which animal lays the largets eggs?: ",
            "Who is the most abundant gas in earth's atmosphere?: ",
            "How many bones are there in human body?: ",
            "Which is the hottest planet?: ")
options = (("A. 117", "B. 118", "C. 112", "D. 119"),
           ("A.OSTRICH", "B. HEN", "C. FISH", "NONE"),
           ("A. N2", "B. O2" ,"C. H2", " D. NONE"),
           ("A. 525", "B. 548", "C. 118", "D. 206"),
           ("A. MARS", "B. VENUS", "C. EARTH", "D. MERCURY"))

answers = ("B","A", "A", "D", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT !")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

score = int(score / len(questions) * 100)
print(f"Your score is: {score} %")