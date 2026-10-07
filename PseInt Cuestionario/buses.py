import os
import random
import time

GREEN = "\033[32m"
END = "\033[0m"


def buses(n1, n2):
    output = []
    output.append("15" + " ")
    output.append((n1 * " ") + "__________" + ((100 - n1) * " ") + "1")
    output.append((n1 * " ") + "|_______\\_" + ((97 - n1) * " ") + "1")
    output.append((n1 * " ") + "|  _  _  |\\" + ((96 - n1) * " ") + "1")
    output.append((n1 * " ") + "|_______/  |" + ((95 - n1) * " ") + "1")
    output.append((n1 * " ") + " (O)---(O)-" + ((95 - n1) * " ") + "1")
    output.append("15" + " ")
    output.append((n2 * " ") + "__________" + ((100 - n2) * " ") + "1")
    output.append((n2 * " ") + "|_______\\_" + ((97 - n2) * " ") + "1")
    output.append((n2 * " ") + "|  _  _  |\\" + ((96 - n2) * " ") + "1")
    output.append((n2 * " ") + "|_______/  |" + ((95 - n2) * " ") + "1")
    output.append((n2 * " ") + " (O)---(O)-" + ((95 - n2) * " ") + "1")

    return "\n".join(output)


# Bucle para animar el avance de los buses
pos_bus1 = 0
pos_bus2 = 0

while pos_bus1 < 80 and pos_bus2 < 80:
    # Limpia la terminal en cada iteración
    os.system("cls" if os.name == "nt" else "clear")

    # Incrementa las posiciones de forma aleatoria
    pos_bus1 += random.randint(1, 3)
    pos_bus2 += random.randint(1, 3)

    # Imprime los buses en color verde
    print(GREEN + buses(pos_bus1, pos_bus2) + END)

    # Pausa breve para dar el efecto de animación
    time.sleep(0.1)