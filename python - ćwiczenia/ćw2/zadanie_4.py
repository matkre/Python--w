import random

slowa = ("gdynia","gdansk","sopot")

s = str(random.choice(slowa))

print("Witaj! Podaj poprawne słowo")
print("Możesz 5 razy wylosować literę\n!")

i = 0

print("Liczba liter w słowie: " + str(len(s)))

while i < 5:
	question = input("Zadaj " + str(i + 1) + ". pytanie (literę): ")
	if question in s:
		answer = "tak"
	else:
		answer = "nie"

	print(answer)
	print()
	i = i+1

print("Podaj całe słowo!")
master_answer = input("Jaka jest odpowiedź: ")

if master_answer == s:
	print("Dobrze. Poprawne słowo to: " + master_answer)
else:
	print("Źle: : " + s)
