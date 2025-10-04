testScore = 0
testfile = open("geography_test.txt")
for line in testfile:
    # Strip and split each line, accommodating potential whitespace
    parts = line.strip().split('|')
    if len(parts) != 5:
        print("Line is not in the correct format:", line)
        continue
    question, answer1, answer2, answer3, correctAnswer = parts
    print(question)
    print("1:", answer1)
    print("2:", answer2)
    print("3:", answer3)
    userAnswer = input("Enter 1, 2 or 3: ")
    if userAnswer == correctAnswer:
        testScore += 1
print(f"Your score: {testScore}/10")
