from Question import Question

question_prompts = [
    "What colore are Apples? \n(a) Red/Green\n(b) Purple \n(c) Orange\n\n",
    "What colore are Bananas? \n(a) Teal\n(b) Magenta \n(c) Yellow\n\n",
    "What colore are strawberries? \n(a) Yellow\n(b) Red \n(c) Blue\n\n"
]


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for que in questions:
        answer = input(que.prompt)
        if answer == que.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)