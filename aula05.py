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


if __name__ == "__main__":
    main()
