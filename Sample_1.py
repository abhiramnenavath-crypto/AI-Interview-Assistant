questions = ["What's your name?", "Tell us about yourself: ", "Any Achievements?"]
answers = []
score = 0

for q in questions:
    ans  = input(q)
    answers.append(ans)

    if q == "What's your name?":
        continue

    words = len(ans.split())

    if words < 10:
        print(f"Your answer for the question '{q}' is very short, please improve it")
        score += 1
    elif words > 150:
        print(f"Your answer for the question '{q}' is very long, please improve it")
        score += 1
    else :
        print(f"Your answer for the question '{q}' is perfect.")
        score += 2
        


print("\nThanks for Answering :)")
print(f"\nYou'r Confidence score is : {score}/4")

