import customtkinter as ctk

from ctk_base_form import CtkBaseForm


class Aula18Form(CtkBaseForm):
    """Janela da aula 18 com foco em RadioButton."""

    def __init__(self) -> None:
        super().__init__(
            aparencia="Dark",
            titulo="Aula - 18 - CTkRadioButton",
            largura=800,
            altura=500,
        )
        self.resizable(width=False, height=False)
        self.sexo_escolhido = ctk.StringVar(value="Masculino")
        self.label_resultado: ctk.CTkLabel | None = None
        self.montar_interface()

    def ao_clicar_no_radiobutton(self) -> None:
        """Obtém o valor selecionado e atualiza o label de resultado."""
        sexo_escolhido = self.sexo_escolhido.get()

        if self.label_resultado is not None:
            self.label_resultado.configure(
                text=f"Sexo selecionado: {sexo_escolhido}")

    def criar_grupo_de_radiobutton(self) -> None:
        """Cria o grupo de seleção de tema da interface."""
        frame_opcoes = ctk.CTkFrame(self)
        frame_opcoes.pack(pady=20)

        ctk.CTkRadioButton(
            frame_opcoes,
            text="Sexo masculino",
            variable=self.sexo_escolhido,
            value="Masculino",
            command=self.ao_clicar_no_radiobutton,
        ).pack(pady=8, padx=20, anchor="w")

        ctk.CTkRadioButton(
            frame_opcoes,
            text="Sexo feminino",
            variable=self.sexo_escolhido,
            value="Feminino",
            command=self.ao_clicar_no_radiobutton,
        ).pack(pady=8, padx=20, anchor="w")

        
    def criar_label_resultado(self) -> None:
        """Cria o label que exibe o tema selecionado."""
        self.label_resultado = ctk.CTkLabel(
            self,
            text="Sexo selecionado: Masculino",
            width=360,
            height=40,
            corner_radius=10,
            font=("Arial", 16, "bold"),
        )
        self.label_resultado.pack(pady=10)

    def montar_interface(self) -> None:
        """Monta os widgets da janela."""
        self.criar_label_de_titulo_da_janela(
            "Criando RadioButtons com CustomTkinter")
        self.criar_grupo_de_radiobutton()
        self.criar_label_resultado()


if __name__ == "__main__":
    aula18 = Aula18Form()
    aula18.mainloop()
