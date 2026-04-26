"""Aula 11 - exemplo de entrada de texto com CustomTkinter."""

import customtkinter as ctk

from ctk_base_form import CtkBaseForm


class Aula11Form(CtkBaseForm):
    """Janela da aula 11 com foco em entrada e exibição de texto."""

    def __init__(self) -> None:
        self.campo_entrada: ctk.CTkEntry | None = None
        self.label_resultado: ctk.CTkLabel | None = None
        super().__init__(
            aparencia="Dark",
            titulo="Entry - Aula 11",
            largura=700,
            altura=300,
        )
        self.resizable(width=False, height=False)
        self.montar_interface()

    def montar_interface(self) -> None:
        """Sobrescreve a base para concentrar toda a estrutura de widgets."""
        self._criar_mensagem_inicial()
        self.campo_entrada = self._criar_campo_entrada()
        self.label_resultado = self._criar_label_resultado()
        self._criar_botao_enviar()

    def _criar_mensagem_inicial(self) -> None:
        ctk.CTkLabel(
            self,
            text="Digite algo na caixa de entrada abaixo e clique no botão.",
            text_color="#F0F0F0",
            font=("Arial", 18, "bold"),
        ).pack(pady=(20, 10), padx=20, anchor="center")

    def _criar_campo_entrada(self) -> ctk.CTkEntry:
        campo_entrada = ctk.CTkEntry(
            self,
            width=300,
            height=40,
            placeholder_text="Digite algo aqui...",
            font=("Arial", 14),
            corner_radius=10,
        )
        campo_entrada.pack(pady=10, padx=20, anchor="center")
        return campo_entrada

    def _criar_label_resultado(self) -> ctk.CTkLabel:
        label_resultado = ctk.CTkLabel(
            self,
            text="",
            text_color="#011427",
            fg_color="#F0F0F0",
            width=400,
            height=40,
            corner_radius=10,
            font=("Arial", 16, "bold"),
        )
        label_resultado.pack(pady=10, padx=20, anchor="center")
        return label_resultado

    def _criar_botao_enviar(self) -> None:
        ctk.CTkButton(
            self,
            text="Enviar",
            command=self.processar_entrada,
            width=150,
            height=40,
            font=("Arial", 14, "bold"),
        ).pack(pady=10, padx=20, anchor="center")

    def obter_texto_digitado(self) -> str:
        if self.campo_entrada is None:
            return ""
        return self.campo_entrada.get().strip()

    def gerar_mensagem_resultado(self, texto_digitado: str) -> str:
        if not texto_digitado:
            return "Você não digitou nenhum texto."
        return f"Você digitou: {texto_digitado}"

    def atualizar_resultado(self, mensagem: str) -> None:
        if self.label_resultado is not None:
            self.label_resultado.configure(text=mensagem)

    def limpar_campo_entrada(self) -> None:
        if self.campo_entrada is not None:
            self.campo_entrada.delete(0, ctk.END)

    def processar_entrada(self) -> None:
        texto_digitado = self.obter_texto_digitado()
        mensagem = self.gerar_mensagem_resultado(texto_digitado)
        self.atualizar_resultado(mensagem)
        self.limpar_campo_entrada()


def main() -> None:
    """Ponto de entrada da aplicação."""
    app = Aula11Form()
    app.mainloop()


if __name__ == "__main__":
    main()
