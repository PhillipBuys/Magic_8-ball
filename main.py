import random
print("Welcome to the magic 8-ball")

player_question = input("What is your question?")


a1 = "Yeah totally!"
a2 = "oh fo sho"
a3 = "odds look good"
a4 = "Hell yeah!"
a5 = "uhm, I guess?"
a6 = "I doubt that kiddo"
a7 = "you crazy?"
a8 = "sure as shit not"
random_number = random.randint(1, 8)


if random_number == 1:
    print(a1)
elif random_number == 2:
    print(a2)
elif random_number == 3:
    print(a3)
elif random_number == 4:
    print(a4)
elif random_number == 5:
    print(a5)
elif random_number == 6:
    print(a6)
elif random_number == 7:
    print(a7)
else: print(a8)


