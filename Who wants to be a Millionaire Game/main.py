questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3,100000],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2,320000],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3,400000],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2,450000],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1,500000],
    ["What is the square root of 64?", "8", "10", "6", "12", 1,1000000],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3,2000000],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3,3000000],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3,4000000],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2,5000000],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2,6000000]
]

# print(questions[0][-2])

win_amount = 0
question_counter =1
for question in questions:
    
    print(f"{question_counter}) {question[0]}")
    print(f" a) {question[1]}")
    print(f" b) {question[2]}")
    print(f" c) {question[3]}")
    print(f" d) {question[4]}")
    
    answer = int(input("Enter your Answer : "))
    if answer == question[-2]:
        win_amount += question[-1]
        print(f"You won {question[-1]}")
        print(f"Total Amount : {win_amount}")
        question_counter += 1
    else:
        print(f"Wrong Answer , The correct Answer is {question[-2]}")
        print("Better Luck next time ")
        break