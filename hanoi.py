import tkinter as tk
import time


class Hanoi(tk.Tk):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Hanoi, cls).__new__(cls)
        else:
            cls._instance.destroy()
        return cls._instance

    def __init__(self, n_discos):
        super(Hanoi, self).__init__()
        self._canvas = tk.Canvas(self, width=420, height=450)
        self._canvas.pack()
        self.bind('<Button-1>', self._click)

        self._texto = "Mova todos os discos para a pilha da direita"
        self.from_ = None
        self.n_discos = n_discos
        self.movimentos = 0

        self._pilhas = [[], [], []]
        self._pilhas[0] = self._discos(100, 50)

        self._desenha()

    def _discos(self, maior, menor):
        delta = (maior-menor) / (self.n_discos - 1)
        lista = [float(maior)]
        while round(maior, 1) > menor:
            maior -= delta
            lista.append(round(maior, 1))
        return lista

    def mudar(self, i, j):
        pilhas = self._pilhas
        if pilhas[i] == []:
            self._texto = "Você não pode tirar um disco de uma pilha vazia."
        elif pilhas[j] == [] or pilhas[i][-1] < pilhas[j][-1]:
            pilhas[j].append(pilhas[i].pop(-1))
            self._texto = ''
            self.movimentos += 1
        else:
            self._texto = ("Erro: um prato de tamanho {} não pode ir sobre um "
                           "prato de tamanho {}.".format(pilhas[i][-1],
                                                         pilhas[j][-1]))
        if len(self._pilhas[-1]) >= self.n_discos:
            self._texto = "Parabéns! Você conseguiu!!!"
            print("número de movimentos: ", self.movimentos)
        self._desenha()

    def update(self):
        if self.from_ is None or self._pilhas[self.from_] == []:
            self.from_ = self.clicked
        else:
            self.mudar(self._instance.from_, self._instance.clicked)
            self.from_ = None

    def _desenha(self):
        for item in self._canvas.find_all():
            self._canvas.delete(item)
        self._canvas.create_text((210, 50), text=self._texto,
                                 font=('helvetiva, 15'), width=400,
                                 justify='center')
        x = 100
        for pilha in self._pilhas:
            y = 400
            self._canvas.create_rectangle((x-5, y, x+5, y-80), fill='black')
            for disco in pilha:
                dx = int(disco/2)
                self._canvas.create_rectangle((x-dx, y, x+dx, y-10),
                                              fill='red')
                y -= 10
            x += 110
        super(Hanoi, self).update()

    def _click(self, event):
        x = event.x
        if 50 < x < 150:
            self.clicked = 0
        elif 160 < x < 260:
            self.clicked = 1
        elif 270 < x < 370:
            self.clicked = 2
        self.update()

    def solve(self, time_sleep):
        def mover(n, i, j, k):
            if n == 1:
                time.sleep(time_sleep)
                print('mover de {} pra {}'.format(i, j))
                self.mudar(i, j)
            else:
                mover(n-1, i, k, j)
                mover(1, i, j, k)
                mover(n-1, k, j, i)
        mover(self.n_discos, 0, 2, 1)


if __name__ == '__main__':
    hanoi = Hanoi(4)
    # hanoi.solve(0.1)
    hanoi.mainloop()
