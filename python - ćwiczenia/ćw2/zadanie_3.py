import random

slowa = ("python","gdansk","dlaczego","gdynia","wsb")
slowo = random.choice(slowa)

popr = slowo
p = ""

while slowo:
	position = random.randrange(len(slowo))
	p += slowo[position]
	slowo = slowo[:position] +slowo[(position +1):]

print(
"""
Witaj w grze 'Wymieszane litery'!
Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter
bez podawania odpowiedzi.)
""")

print("Podaj słowo: ", p)

pod_odp = input("\nOdpowiedź: ")
blad = 0
i = 0
podpowiedz = ""
punkty = len(popr)

while pod_odp != popr and pod_odp != "":
	print("Słowo nie jest poprawne")
	blad += 1

	if (blad% 3 == 0):
		podpowiedz += popr[i]
		i += 1
		print("Podpowiedz: ", podpowiedz)
		if (punkty > 0):
			punkty -=1

	pod_odp = input("Odpowiedź: ")
if pod_odp == popr:
	print("Odpowiedź poprawna")
	print("Masz ", punkty, " punktów.")
	print("")

