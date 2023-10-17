import random
uservalue = input("Ваш хід: ")

value = random.choice(["rock", "scissor", "paper"])
print("Суперник:",value)


if uservalue == "rock" in ["rock", "scissor", "paper"] and value == "scissor" in ["rock", "scissor", "paper"]:
     print("Ви перемогли")
elif uservalue == "scissor" in ["rock", "scissor", "paper"] and value == "paper" in ["rock", "scissor", "paper"]:
     print("Ви перемогли")
elif uservalue == "paper" in ["rock", "scissor", "paper"] and value == "rock" in ["rock", "scissor", "paper"]:
     print("Ви перемогли")
elif value == "rock" in ["rock", "scissor", "paper"] and uservalue == "scissor" in ["rock", "scissor", "paper"]:
     print("Ви програли")
elif value == "scissor" in ["rock", "scissor", "paper"] and uservalue == "paper" in ["rock", "scissor", "paper"]:
     print("Ви програли")
elif value == "paper" in ["rock", "scissor", "paper"] and uservalue == "rock" in ["rock", "scissor", "paper"]:
     print("Ви програли")
elif uservalue == value:
     print("Нічия")
else:
 while uservalue == "" and uservalue != "rock" or "paper" or "scissor" in ["rock", "scissor", "paper"]:
    print("Некоректний ввід")
    break
 
