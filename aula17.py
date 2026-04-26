import customtkinter as ctk

from ctk_base_form import CtkBaseForm


class Aula17Form(CtkBaseForm):
    """Janela da aula 17."""

    def __init__(self) -> None:
        super().__init__(
            aparencia="Dark",
            titulo="Aula - 17 - CTKcheckbox",
            largura=800,
            altura=500,
        )
        self.resizable(width=False, height=False)
        self.checkbox_var = ctk.BooleanVar(value=False)
        self.montar_interface()

    def ao_clicar_no_checkbox(self) -> None:
        """Verifica o estado do checkbox e atualiza o label de resultado."""
        checkbox_clicado = self.checkbox_var.get()
        resultado_texto = "Você está no tema claro." if checkbox_clicado else "Você está no tema escuro."
        self.label_resultado.configure(text=resultado_texto)
        self.aplicar_tema("Light" if checkbox_clicado else "Dark")

    def criar_label_de_resultado(self) -> None:
        """Cria um label para exibir o resultado da seleção do checkbox."""
        self.label_resultado = ctk.CTkLabel(
            self,
            text="",
            width=400,
            height=40,
            corner_radius=10,
            font=("Arial", 16, "bold"),
        )
        self.label_resultado.pack(pady=10, padx=20, anchor="center")

    def criar_exemplo_checkbox(self) -> None:
        """Cria um checkbox na janela."""
        self.checkbox = ctk.CTkCheckBox(
            self,
            text="Clique para selecionar",
            variable=self.checkbox_var,
            onvalue=True,
            offvalue=False,
            command=self.ao_clicar_no_checkbox,
        )
        self.checkbox.pack(pady=20)

    def montar_interface(self) -> None:
        self.criar_label_de_titulo_da_janela(
            "Criando um checkbox com CustomTkinter")
        self.criar_exemplo_checkbox()
        self.criar_label_de_resultado()


if __name__ == "__main__":
    aula17 = Aula17Form()
    aula17.mainloop()
