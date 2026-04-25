import customtkinter as ctk

from ctk_base_form import CtkBaseForm


class Aula16Form(CtkBaseForm):
    """Janela da aula 16 com foco em frames e organização de layout."""

    def __init__(self) -> None:
        super().__init__(
            aparencia="Dark",
            titulo="Aula - 16 (Switch)",
            largura=800,
            altura=500,
        )
        self.resizable(width=False, height=False)

    def alterar_tema_do_aplicativo(self) -> None:
        """Altera o tema do aplicativo entre claro e escuro."""
        modo_atual = ctk.get_appearance_mode()
        novo_modo = "Light" if modo_atual == "Dark" else "Dark"
        ctk.set_appearance_mode(novo_modo)
        print(f"Tema alterado para: {novo_modo}")

    def montar_interface(self) -> None:
        ctk.CTkLabel(
            self,
            text="Aula 16 - Estudando switch",
            font=("Arial", 20, "bold"),
        ).pack(pady=(20, 10))
        colocar_switch_na_tela(self)


def colocar_switch_na_tela(janela: "Aula16Form") -> None:
    """Adiciona um switch à janela e exibe seu estado no console."""
    switch = ctk.CTkSwitch(
        janela,
        text="Alternar Tema",
        command=janela.alterar_tema_do_aplicativo,
        onvalue=True,
        offvalue=False,
        fg_color="#555555",
        button_color="#007ACC",
    )
    switch.pack(pady=20)


if __name__ == "__main__":
    aula16 = Aula16Form()
    aula16.mainloop()
