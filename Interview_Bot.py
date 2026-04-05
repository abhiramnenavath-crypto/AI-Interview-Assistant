import os

def speak(text):
    text = text.replace("'", "")
    
    command = (f'powershell -c "Add-Type –AssemblyName System.Speech; '
              f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\');"')
    os.system(command)

questions = ["What is your name?", "Tell us about yourself: ", "Any Achievements?"]
answers = []
score = 0

for q in questions:

    speak(q)

    ans  = input(q)
    answers.append(ans)

    if q == "What is your name?":
        continue

    words = len(ans.split())

    if words < 10:
        feedback = f"Your answer for the question '{q}' is very short, please improve it"
        score += 1
    elif words > 150:
        feednack = f"Your answer for the question '{q}' is very long, please improve it"
        score += 1
    else :
        feedback = f"Your answer for the question '{q}' is perfect."
        score += 2
    
    print(feedback)

    speak(feedback)
    

print("\nThanks for Answering :)")
speak("Thanks for answering")
print(f"\nYou'r Confidence score is : {score}/4")
speak(f"You'r Confidence score is : {score}/4")

