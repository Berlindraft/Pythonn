from Questions import Questions

#list of questions
questions = [
    "What is the capital of France?\n(A)London\n(B)Paris\n(C)Berlin\n(D)Rome",
    "Which planet is known as the \"Red planet\"\n(A)Earth\n(B)Jupiter\n(C)Mars\n(D)Venus",
    "What is the chemical symbol for water?\n(A)H\n(B)O\n(C)H2O\n(D)H2",
    "What is the capital of Japan?\n(A) Beijing\n(B) Tokyo\n(C) Seoul\n(D) Bangkok",
    "Who wrote 'Romeo and Juliet'?\n(A) William Shakespeare\n(B) Charles Dickens\n(C) Jane Austen\n(D) Mark Twain",
    "What is the largest mammal in the world?\n(A) Elephant\n(B) Giraffe\n(C) Blue whale\n(D) Gorilla",
    "How many continents are there?\n(A) Four\n(B) Five\n(C) Six\n(D) Seven",
    "Which country is known as the 'Land of the Rising Sun'?\n(A) China\n(B) Japan\n(C) South Korea\n(D) Thailand",
    "Who painted the Mona Lisa?\n(A) Michelangelo\n(B) Leonardo da Vinci\n(C) Vincent van Gogh\n(D) Pablo Picasso",
    "What is the capital of Australia?\n(A) Sydney\n(B) Canberra\n(C) Melbourne\n(D) Brisbane",
    "Which is the longest river in the world?\n(A) Nile\n(B) Amazon\n(C) Yangtze\n(D) Mississippi",
    "What is the boiling point of water in Celsius?\n(A) 0°C\n(B) 100°C\n(C) -273°C\n(D) 50°C"
]
#the prompt and answer keys
question = [
    Questions(questions[0], "B"),
    Questions(questions[1], "C"),
    Questions(questions[2], "C"),
    Questions(questions[3], "B"),
    Questions(questions[4], "A"),
    Questions(questions[5], "C"),
    Questions(questions[6], "D"),
    Questions(questions[7], "B"),
    Questions(questions[8], "B"),
    Questions(questions[9], "B"),
    Questions(questions[10], "A"),
    Questions(questions[11], "B"),

]
#this runs the questions and checks score
def run_prompt():
    score = 0
    total_questions = len(question)
    for quest in question:
        print(quest.prompt)
        answer = input("Enter your answer:")
        if answer.upper() == quest.answer:
            score +=1
    if score == total_questions:
        print("EXCELLENT! Your score is: ", score,  "/", total_questions )
    elif score == (total_questions - 1):
        print("GOOD JOB! Your score is: ", score,  "/", total_questions)
    elif score == (total_questions - 2):
        print("BIT MORE, BUD! Your score is: ", score,  "/", total_questions)
    else:
        print("BETTER LUCK NEXT TIME! Your score is: ", score,  "/", total_questions)

#run prompt function
run_prompt()
