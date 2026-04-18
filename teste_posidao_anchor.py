"""
    Teste de posicionamento com anchor no Tkinter.

    Neste exemplo, demonstramos como o parâmetro anchor influencia o
    posicionamento de widgets usando o método place. O script mostra o
    alinhamento de elementos em diferentes cantos da janela de forma simples.

    Autor: Janderson de Almeida
    Data: 2024-06-01
"""

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# O ponto (0, 0) é o canto superior esquerdo da janela.
# Com anchor="nw", o próprio canto do label vai para (0,0).
label = tk.Label(root, text="Olá!", bg="lightblue")
label.place(x=0, y=0, anchor="nw")   # colado no topo-esquerdo

# Com anchor="se", o canto inferior-direito vai para (300, 200).
btn = tk.Button(root, text="Fechar", command=root.destroy)
btn.place(x=300, y=200, anchor="se")  # colado no canto inferior-direito

root.mainloop()
