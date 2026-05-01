import customtkinter as ctk

from ctk_base_form import CtkBaseForm


class Aula21Form(CtkBaseForm):
    """Janela template para evoluir os exemplos da aula 21."""

    def __init__(self) -> None:

        super().__init__(
            aparencia="Dark",
            titulo="Aula 21 - Método pack()",
            largura=400,
            altura=410,
        )
        self.resizable(False, False)
        self.montar_interface()

    def montar_interface(self) -> None:
        """Monta a estrutura inicial da interface da aula."""
        self.criar_label_de_titulo_da_janela(
            "Tela de Login")
        self._criar_widgets_de_login()

    def _criar_widgets_de_login(self):
        caixa_entrada_texto_usuario = ctk.CTkEntry(self,
                                                   placeholder_text="Usuário",
                                                   width=250,
                                                   height=45)
        caixa_entrada_texto_senha = ctk.CTkEntry(self,
                                                 placeholder_text="Senha",
                                                 width=250,
                                                 height=45,
                                                 show="*")
        botao_logar = ctk.CTkButton(self, text="Logar".upper(),
                                    width=250,
                                    height=45)
        
        caixa_entrada_texto_usuario.pack(pady=20)
        caixa_entrada_texto_senha.pack()
        botao_logar.pack(pady=30)


if __name__ == "__main__":
    app = Aula21Form()
    app.mainloop()
