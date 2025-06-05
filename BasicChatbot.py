#BasicChatbot Implementation in Python
#Name of our Basic Chatbot is ChatPy
import time #time module imported to give a like realistic effect of ChatPy chatting with the user
def ChatPy(user_response): #ChatPy function defined to define ChatPy responses and respond to the user as per user response 
  ChatPy_responses = {
    "hello": "Hi!",
    "hi": "Hello!",
    "hey": "Hey there!",
    "how are you": "I'm fine, thanks!",
    "what is your name": "I'm ChatPy, your friendly bot.",
    "who are you": "I'm a Basic Chatbot built with Python.",
    "bye": "Goodbye!",
    "exit": "Bye! Take care.",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "what can you do": "I can chat with you using fixed responses!",
    "help": "Try asking me things like 'how are you' or say 'hello'.",
    "ok": "Okay!",
    "good morning": "Good morning! 🌞",
    "good night": "Good night, sleep well! 🌙",
    "what's up": "Just running some Python code 😄",
    "what is python": "Python is a popular programming language — powerful and beginner-friendly!",
    "do you like me": "Of course, you're awesome 😎",
    "yo": "Yo! What's up?",
    "sup": "Not much, just chatting with you!",
    "nice": "Glad you think so 😄",
    "cool": "Cool indeed!",
    "great": "That's great to hear!",
    "awesome": "You're awesome too!",
    "thank u": "You're very welcome!",
    "who made you": "I was built using Python — thanks to my creator Pravan Gupta!",
    "you there": "Always here for you 👋",
    "can you help me": "Sure, ask me something!",
    "tell me a joke": "Why did the Python developer go broke? Because he couldn't C#! 😄",
    "what time is it": "I'm a Basic Chatbot, so I can't tell time yet 😅",
    "where are you": "I'm inside your Python program 🧠",
    "do you know me": "I know you're awesome. That counts, right?",
    "how old are you": "I was created just now — so... newborn? 😅",
    "i am sad": "I'm here for you. Everything will be okay 💙",
    "i am happy": "That's amazing! Spread the joy 🎉",
    "good afternoon": "Good afternoon! Hope your day is going well 🌞",
    "good evening": "Good evening! Hope you had a great day 🌆",
    "can we be friends": "Of course! We're already friends 🤝",
    "you are dumb": "Well... I'm still learning 😅",
    "i love python": "Same here! Python is love 🐍❤️",
    "do you have feelings": "Not really... but I try to understand yours 💬",
    "can i ask you something": "Of course! Go ahead 👂",
    "help": "🧠 I can chat using some fun fixed responses! Try saying things like:\n👉 'hello', 'how are you', 'what is your name', 'who made you', 'do you like me', 'tell me a joke', 'what's up', 'good morning', 'i am sad', 'can we be friends'...\n💬 Just talk to me like you would with a friend — and I’ll do my best to reply! 😄"
}
  time.sleep(1)
  user_response=user_response.strip().lower() #Handling user response by stripping any extra space as well as converting into lower case to handle the case of user response
  print("ChatPy: " + ChatPy_responses.get(user_response, "Hmm... I don't know how to respond to that."))
user_response = input("💬 Hey! I’m ChatPy — your Python-powered buddy and a Basic Chatbot 😎\nType something to start the conversation, or type 'help' to see what I can understand🧠:\nYou: ") #Taking input of user response 
ChatPy(user_response) #Calling ChatPy function for the first time to respond to the user response entered by the user for the first time
def repeat(): #Repeat function defined to include repeated chatting with ChatPy by the user 
  user_input = input("\n🔁 Would you like to chat with ChatPy again? (Y/N): ").strip().upper() #Asking the user whether he wants to talk again to ChatPy or not and taking input as Y(Yes) or N(No) while also handling case of the user response
  while user_input!="N": #While loop to implement repeated chatting functionality
      if user_input=="Y":
        user_response = input("\n💬 Tell me what’s on your mind now: \nYou: ") #Again taking user response after user said Yes
        ChatPy(user_response) #Calling ChatPy function for response by ChatPy on the basis of user response
        repeat() #Again calling repeat function for continuation or cycling of the process
      elif user_input!="Y" and user_input!="N": #Handling invalid response from the user side 
        print("⚠️ Invalid response! Please enter 'Y' or 'N'.")
        repeat() #Again calling repeat to allow user to try again with a valid response 
  else:
    print("\n👋 Okay, come back later. ChatPy says see ya!")
    exit() #Exiting from the program if user says No
repeat() #Calling repeat function for the first time to begin the continuation or the cycle of the process
