"""Template da aula 19 baseado no formulário base reutilizável."""

import customtkinter as ctk

from ctk_base_form import CtkBaseForm


class Aula19Form(CtkBaseForm):
    """Janela template para evoluir os exemplos da aula 19."""

    def __init__(self) -> None:
        # Estado inicial da tela para facilitar expansão nas próximas aulas.
        self.contador = 0
        self.progresso_atual = 0.0

        super().__init__(
            aparencia="Light",
            titulo="Aula 19 - ProgressBar e Status",
            largura=900,
            altura=500,
        )
        self.resizable(False, False)
        self.montar_interface()

    def montar_interface(self) -> None:
        """Monta a estrutura inicial da interface da aula."""
        self.criar_label_de_titulo_da_janela("Aula 19 - progressbar e status")

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True, padx=24, pady=12)

        self.lbl_status = ctk.CTkLabel(
            self.container,
            text="Status: template carregado",
            font=("Arial", 14),
        )
        self.lbl_status.pack(pady=(20, 10))

        self.progresso = ctk.CTkProgressBar(
            self.container,
            width=420,
            height=22,
            corner_radius=10,
            border_width=1,
            border_color=("#0E7490", "#67E8F9"),
            progress_color=("#0EA5E9", "#22D3EE"),
            fg_color=("#E2E8F0", "#1E293B"),
        )
        self.progresso.set(self.progresso_atual)
        self.progresso.pack(pady=(0, 10))

        self.lbl_percentual = ctk.CTkLabel(
            self.container,
            text="Progresso: 0%",
            font=("Arial", 12, "bold"),
        )
        self.lbl_percentual.pack(pady=(0, 16))

        self.btn_acao = ctk.CTkButton(
            self.container,
            text="Testar ação",
            command=self.on_testar_acao,
            height=38,
            corner_radius=10,
            fg_color=("#0EA5E9", "#0284C7"),
            hover_color=("#0284C7", "#0369A1"),
        )
        self.btn_acao.pack(pady=8)

    def on_testar_acao(self) -> None:
        """Incrementa progresso e atualiza o status do template."""
        self.contador += 1
        self.progresso_atual = min(1.0, self.progresso_atual + 0.1)
        percentual = int(self.progresso_atual * 100)

        self.progresso.set(self.progresso_atual)
        self.lbl_percentual.configure(text=f"Progresso: {percentual}%")
        self.lbl_status.configure(text=f"Status: clique {self.contador}")


if __name__ == "__main__":
    app = Aula19Form()
    app.mainloop()
