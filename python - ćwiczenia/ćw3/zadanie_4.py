import math

op = "a" 
while op != "n":
    a = int(input("Podaj bok a "))
	b = int(input("Podaj bok b: "))
	c = int(input("Podaj bok c: "))

    if (a + b) > c and (a + c) > b and (b + c) > a:  
        print "Z podanych boków można zbudować trójkąt"
        if (a**2 + b**2 == c**2 or
                a**2 + c**2 == b**2 or
                b**2 + c**2 == a**2):
            print "Do tego prostokątny!"

        print "Obwód wynosi:", (a + b + c)
        p = 0.5 * (a + b + c) 
        P = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print "Pole wynosi:", P
        op = "n"
    else:
        print "Z podanych odcinków nie można utworzyć trójkąta prostokątnego."
        op = raw_input("Spróbujesz jeszcze raz (t/n): ")

print "Do zobaczenia..."