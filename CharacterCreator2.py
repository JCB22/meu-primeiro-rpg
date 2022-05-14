import tkinter as tk
from tkinter import messagebox


class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("200x150")

        self.nome_personagem = tk.Entry(width=20)
        self.nome_personagem.insert(0, "Nome de Personagem")

        self.label = tk.Label(text="Escolha sua classe:")
        self.label.pack(padx=10, pady=10)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        self.btn1 = tk.Button(self.buttonframe, text="Bárbaro", font=('Roboto', 18), command=Berserker(self.nome_personagem.get))
        self.btn2 = tk.Button(self.buttonframe, text="Bardo", font=('Roboto', 18), command=Bardo(self.nome_personagem.get))
        self.btn3 = tk.Button(self.buttonframe, text="Protetor", font=('Roboto', 18), command=Ranger(self.nome_personagem.get))


class Character:

    def __init__(self, name):

        self.name = name

    def attack(self):
        return self.attack

    def defense(self):
        return self.defense

    def range(self):
        return self.range

    def moves(self):
        return self.moves


class Bardo(Character):
    attack = 50
    defense = 75
    range = 75
    moves = {
        "4 on the floor": "Uma cântiga antiga que motiva os inimigos a tomarem um sono profundo",
        "Walking Waltz": "Música que acalma os nervos dos personagens e tira a ansiedade",
        "Who shot the sheriff?": "Uma arma escondida que surpreende aqueles que estão despreparados"
    }


class Berserker(Character):
    attack = 80
    defense = 80
    range = 40
    moves = {
        "Corte bruto": "Acerta a pessoa dentro do seu range e da o dano baseado no attack",
        "Arremesso descuidado": "Aumenta o alcance em 1.5x, mas perde o machado até recuperá-lo",
        "Grito Selvagem": "Faz um grito que pega os inimigos de surpresa"

    }


class Ranger(Character):
    attack = 85
    defense = 35
    range = 90
    moves = {
        "Flechada no Joelho": "Um tiro certeiro que acabara com a aventura de muitos aspirantes",
        "Dedos metálicos": "Usado para defender seus preciosos dedos, letal no combate a curta distancia",
        "Luz ofuscante": "Uma bomba que cega todos que estiverem próximos demais dela"
    }


def main():
    MyGUI()


if __name__ == '__main__':
    main()


# c1 = Berserker("Jonas Brothers")

# print(f"N: {c1.name} A: {c1.attack} D: {c1.defense} R: {c1.range}")
