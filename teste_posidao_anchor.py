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