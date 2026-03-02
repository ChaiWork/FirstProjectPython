questions=("1. How does drinking warm water primarily help relieve nasal and throat congestion?",
           "2. The text explains that warm water can aid in weight loss for which of the following reasons?",
           "3. Which of the following is a key internal benefit of warm water related to blood vessels?",)

options=(("a) By increasing the body's core temperature to fight off viruses.","b) By acting as a natural expectorant to loosen phlegm.","c) By coating the throat with a protective layer of moisture.","d) By reducing blood flow to the inflamed areas."),
         ("a) It chemically dissolves fat cells on contact.","b) It acts as a powerful appetite suppressant for the entire day.","c) It may temporarily increase metabolism and help break down fat deposits.","d) It prevents the body from absorbing calories from food."),
         ("a) It acts as a vasodilator, improving blood circulation.","b) It thickens the blood to prevent clotting.","c) It constricts blood vessels to reduce swelling.","d) It has no effect on the cardiovascular system."),
         )

answers=("B","C","A")

guesses=[]

score=0

question_num=0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in  options [question_num]:
        print(option)
    
    guess = input("ENTER (A B C D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("Correct")
    else:
        print("incorrect")
        print(f"{answers[question_num]} is the correct answer")
         
    question_num+=1
      
print("----------------------------")
print("         RESULT             ")
print("----------------------------")

print("Answer: ", end="")
for answer in  answers:
    print(answer, end =" ")
print()    

print("guesses: ", end="")
for guess in  guesses:
    print(guess, end =" ")
print()    

score =int(score / len(questions) * 100)

print(f"Your score is :{score}%")