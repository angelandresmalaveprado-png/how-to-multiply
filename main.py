import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


speak("hello do you want to learn how to multiply numbers?")

say = input("yes or no ")

if say.lower() == "yes":
    speak("Greaat! Let's start with some simple multiplication problems.")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 * num2
    speak(f"The result of {num1} multiplied by {num2} is {result}.")

    speak("Do you want to try another multiplication problem?")
    say_again = input("yes or no ")
    if say_again.lower() == "yes":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 * num2
        speak(f"The result of {num1} multiplied by {num2} is {result}.")

        speak("the main secret to how to multiply whole numers is to remember the multiplication table. You can also use the distributive property to break down larger numbers into smaller ones. For example, to multiply 12 by 3, you can break it down into (10 + 2) * 3 = (10 * 3) + (2 * 3) = 30 + 6 = 36.")
        speak("have any questions about how to multiply whole numbers?")
        question = input("yes or no ")
        if question.lower() == "yes":
            question = input("Enter your question: ")
            speak(f"Great question! Let me explain that...")


    else:
        speak("Okay, let's stop for now.")



