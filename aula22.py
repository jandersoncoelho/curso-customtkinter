import customtkinter as ctk

from ctk_base_form import CtkBaseForm


class Aula22Form(CtkBaseForm):
    """Janela template para evoluir os exemplos da aula 22."""

    def __init__(self) -> None:

        super().__init__(
            aparencia="Dark",
            titulo="Aula 22 - Método grid()",
            largura=500,
            altura=200,
        )
        self.valor_do_primeiro_checkbox_atual = ctk.StringVar(value="clicado")
        self.valor_do_segundo_checkbox_atual = ctk.StringVar(value="clicado")
        self.resizable(False, False)
        self.grid_columnconfigure((0, 1), weight=1)
        self.montar_interface()

    def _ao_clicar_no_primeiro_checkbox(self):
        valor_estado_checkbox = self.primeiro_checkbox.get()
        print(f"Primeiro Checkbox: {valor_estado_checkbox}.")

    def _ao_clicar_no_segundo_checkbox(self):
        valor_estado_checkbox = self.segundo_checkbox.get()
        print(f"Segundo Checkbox: {valor_estado_checkbox}.")

    def montar_interface(self) -> None:
        self.botao_demonstracao = ctk.CTkButton(self,
                                                text="Clique no Botão",
                                                command=self.ao_clicar_no_botao_demostracao,
                                                )
        self.primeiro_checkbox = ctk.CTkCheckBox(
            self,
            text="Clique no checkbox",
            variable=self.valor_do_primeiro_checkbox_atual,
            onvalue="selecionado",
            offvalue="não selecionado",
            command=self._ao_clicar_no_primeiro_checkbox
        )
        self.segundo_checkbox = ctk.CTkCheckBox(
            self,
            text="Segundo checkbox",
            variable=self.valor_do_segundo_checkbox_atual,
            onvalue="selecionado",
            offvalue="não selecionado",
            command=self._ao_clicar_no_segundo_checkbox
        )
        self.botao_demonstracao.grid(
            row=0, column=0, pady=20, padx=20, stick="ew", columnspan=2)
        self.primeiro_checkbox.grid(
            row=1, column=0, pady=(0, 20), padx=20, stick="w")
        self.segundo_checkbox.grid(
            row=1, column=1, pady=(0, 20), padx=20, stick="w")

    def ao_clicar_no_botao_demostracao(self):
        print("Botão clicado")


if __name__ == "__main__":
    app = Aula22Form()
    app.mainloop()
