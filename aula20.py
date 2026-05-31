import customtkinter as ctk

from ctk_base_form import CtkBaseForm


class Aula20Form(CtkBaseForm):
    """Janela template para evoluir os exemplos da aula 20."""

    def __init__(self) -> None:
        # Estado inicial da tela para facilitar expansão nas próximas aulas.
        self.contador = 0
        self.progresso_atual = 0.0

        super().__init__(
            aparencia="Dark",
            titulo="Aula 20 - Aprendendo a usar o método place()",
            largura=900,
            altura=500,
        )
        self.resizable(True, True)
        self.montar_interface()

    def montar_interface(self) -> None:
        """Monta a estrutura inicial da interface da aula."""
        self.criar_label_de_titulo_da_janela(
            "Aula 20 - Aprendendo a usar o método place()")
    
        self.primeiro_botao_de_teste = ctk.CTkButton(
            self,
            text="Botão de teste",
        )
        self.segundo_botao_de_teste = ctk.CTkButton(
            self,
            text="Outro botão de teste",
        )
        self.terceito_botao_de_teste = ctk.CTkButton(
            self,
            text="Mais um botão de teste",
        )
        
        self.primeiro_botao_de_teste.place(x=200, y=200)
        self.segundo_botao_de_teste.place(x=400, y=200)
        self.terceito_botao_de_teste.place(relx=0.7, rely=0.4)        

class Aula20Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        ctk.CTkLabel(self, text="Aula 20 - Método place() (embutido)", font=("Arial", 16)).pack(pady=10)
        self.primeiro_botao_de_teste = ctk.CTkButton(self, text="Botão de teste")
        self.segundo_botao_de_teste = ctk.CTkButton(self, text="Outro botão de teste")
        self.terceito_botao_de_teste = ctk.CTkButton(self, text="Mais um botão de teste")
        self.primeiro_botao_de_teste.place(x=50, y=80)
        self.segundo_botao_de_teste.place(x=200, y=80)
        self.terceito_botao_de_teste.place(relx=0.7, rely=0.4)

if __name__ == "__main__":
    app = Aula20Form()
    app.mainloop()
