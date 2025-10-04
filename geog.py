# Tina has started to write an algorithm which allows a student to take the test. She has stored 10 questions in the file named "geography_test.txt".
# We want to output the questions and all the possible answers and validate with the correct answer. If the user answer is correct, we want to increment the score. The user will input the answer number e.g. 1 or 2 or 3

testScore = 0
testfile = open("geography_test.txt")
for line in testfile:
    parts = line.strip().split('|')
    question, answer1, answer2, answer3, correctAnswer = parts
    # TODO

print(f"Your score: {testScore}/10")
