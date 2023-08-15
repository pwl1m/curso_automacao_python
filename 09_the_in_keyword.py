#1.0
# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Digite algo que voce assistiu recentemente: ")

# if user_movie in movies_watched:
#     print(f"Eu assisti {user_movie} tambem!")
# else:
#     print(f"Eu nao assisti {user_movie} ainda")

# 2.0
number = 7

user_input=input("Digite 'y' se voce quiser jogar: ")

# if user_input == "y": # é trocada por:

if user_input in ("y", "Y"):
    user_number = int(input("Adivinhe um numero: "))
    if user_number == number:
        print("Voce acertou!")
    #abs(number - user_number) == 1: # é trocada por:
    elif number - user_number in (1, -1):
        print("Voce errou por 1")
    else:
        print("Voce errou!")