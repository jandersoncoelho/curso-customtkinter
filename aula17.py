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

    def verificar_selecao_checkbox(self) -> None:
        """Verifica o estado do checkbox e atualiza o label de resultado."""
        estado_checkbox = self.checkbox_var.get()
        resultado_texto = "Checkbox selecionado!" if estado_checkbox else "Checkbox não selecionado."
        print(resultado_texto)

    def criar_label_de_resultado(self, estado: bool) -> None:
        """Cria um label para exibir o resultado da seleção do checkbox."""
        pass

    def criar_exemplo_checkbox(self) -> None:
        """Cria um checkbox na janela."""
        self.checkbox = ctk.CTkCheckBox(
            self,
            text="Clique para selecionar",
            variable=self.checkbox_var,
            onvalue=True,
            offvalue=False,
            command=self.verificar_selecao_checkbox,
        )
        self.checkbox.pack(pady=20)

    def montar_interface(self) -> None:
        self.criar_label_de_titulo_da_janela(
            "Criando um checkbox com CustomTkinter")
        self.criar_exemplo_checkbox()
        self.criar_label_de_resultado(False)
        self.verificar_selecao_checkbox()


if __name__ == "__main__":
    aula17 = Aula17Form()
    aula17.mainloop()
