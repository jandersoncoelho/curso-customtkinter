"""
    Aula 05 - Estruturando o layout e posicionamento da janela.

    Neste exemplo, organizamos a base visual da aplicação com tema
    personalizado e centralização da janela na tela. A estrutura prepara o
    ambiente para posicionar widgets e frames de forma mais controlada e
    responsiva.

    Autor: Janderson de Almeida
    Data: 2024-06-01
"""

from ctk_base_form import CtkBaseForm


def main() -> None:
    janela_principal = CtkBaseForm(
        aparencia="System",
        titulo="Minha Janela customtkinter - Aula 05",
        largura=1024,
        altura=500,
    )
    janela_principal.mainloop()


class Aula05Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        try:
            if 'CtkBaseForm' in globals():
                # nothing to reuse directly; show basic info
                pass
        except Exception:
            pass
        ctk.CTkLabel(self, text="Aula 05 - Layout e posicionamento (embutido)", font=(None, 16)).pack(padx=20,pady=20)

if __name__ == "__main__":
    main()
