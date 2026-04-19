"""Aula 14 - exemplo de slider com reprodução de áudio."""

import importlib.util
from importlib import import_module
from pathlib import Path
from threading import Thread

import customtkinter as ctk

from ctk_base_form import CtkBaseForm

CAMINHO_ARQUIVO_AUDIO = Path(__file__).with_name("musica.mp3")


class Aula14Form(CtkBaseForm):
    """Janela da aula 14 com slider e reprodução opcional de áudio."""

    def __init__(self) -> None:
        self.rotulo_status_reproducao: ctk.CTkLabel | None = None
        super().__init__(
            aparencia="Dark",
            titulo="CtkSlider - Aula 14",
            largura=400,
            altura=220,
        )
        self.resizable(width=False, height=False)

    def montar_interface(self) -> None:
        """Concentra a criação e organização dos widgets da janela."""
        self.rotulo_status_reproducao = self.criar_rotulo_status_reproducao()
        self.criar_controle_volume()
        self.criar_botao_reproduzir()

    def criar_rotulo_status_reproducao(self) -> ctk.CTkLabel:
        """Cria o rótulo que exibe o valor atual do slider e mensagens de status."""
        rotulo_status_reproducao = ctk.CTkLabel(
            self,
            text="Alterar volume: 0%",
            font=("Arial", 16),
        )
        rotulo_status_reproducao.pack(pady=20)
        return rotulo_status_reproducao

    def criar_controle_volume(self) -> None:
        """Cria o slider responsável por atualizar o valor exibido."""
        controle_volume = ctk.CTkSlider(
            self,
            from_=0,
            to=100,
            command=self.atualizar_status_volume,
        )
        controle_volume.set(0)
        controle_volume.pack(pady=10)

    def criar_botao_reproduzir(self) -> None:
        """Cria o botão que inicia a reprodução do áudio."""
        ctk.CTkButton(
            self,
            text="Play",
            command=self.reproduzir_audio,
        ).pack(pady=10)

    def atualizar_status_volume(self, valor: float) -> None:
        """Atualiza o texto exibido com o volume selecionado."""
        percentual_volume = int(float(valor))
        self.atualizar_rotulo_status(f"Alterar volume: {percentual_volume}%")

    def atualizar_rotulo_status(self, mensagem: str) -> None:
        """Exibe mensagens de status no rótulo principal."""
        if self.rotulo_status_reproducao is not None:
            self.rotulo_status_reproducao.configure(text=mensagem)

    def reproduzir_audio(self) -> None:
        """Valida o ambiente e inicia a reprodução do áudio em segundo plano."""
        if not self.dependencias_audio_estao_disponiveis():
            self.atualizar_rotulo_status(
                "Instale pydub para reproduzir o áudio.")
            return

        if not CAMINHO_ARQUIVO_AUDIO.exists():
            self.atualizar_rotulo_status("Arquivo de áudio não encontrado.")
            return

        self.atualizar_rotulo_status("Reproduzindo áudio...")
        Thread(target=self._executar_reproducao_audio, daemon=True).start()

    def dependencias_audio_estao_disponiveis(self) -> bool:
        """Verifica se a dependência opcional de áudio está disponível."""
        return importlib.util.find_spec("pydub") is not None

    def _executar_reproducao_audio(self) -> None:
        """Executa a reprodução sem bloquear a interface gráfica."""
        try:
            modulo_audio = import_module("pydub")
            modulo_reproducao = import_module("pydub.playback")
            faixa_de_audio = modulo_audio.AudioSegment.from_file(
                str(CAMINHO_ARQUIVO_AUDIO))
            modulo_reproducao.play(faixa_de_audio)
            self.after(0, lambda: self.atualizar_rotulo_status(
                "Reprodução finalizada."))
        except Exception as erro:
            mensagem_erro = str(erro)
            self.after(0, lambda: self.atualizar_rotulo_status(
                f"Erro ao tocar áudio: {mensagem_erro}"))


def main() -> None:
    """Ponto de entrada da aplicação."""
    app = Aula14Form()
    app.mainloop()


if __name__ == "__main__":
    main()
