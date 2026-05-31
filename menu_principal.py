"""Menu principal que lista e abre os scripts do workspace.

Baseado em `CtkBaseForm` — cria uma barra lateral com botões
para todos os arquivos `.py` do diretório do projeto (exclui
arquivos de infraestrutura). Cada botão executa o script em
um processo separado usando o interpretador atual.
"""

from __future__ import annotations

import logging
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable, List

import customtkinter as ctk
from tkinter import messagebox

from ctk_base_form import CtkBaseForm

LOGGER = logging.getLogger(__name__)

EXCLUIR = {"ctk_base_form.py", "menu_principal.py", "__init__.py"}


class MenuPrincipal(CtkBaseForm):
    """Janela que exibe uma barra com botões para todos os scripts.

    Ao clicar em um botão, o script é iniciado como um processo
    separado com o interpretador Python em uso (`sys.executable`).
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, titulo="Menu Principal", largura=900, altura=560, **kwargs)
        self.montar_interface()

    def montar_interface(self) -> None:
        # Frame lateral para a barra de botões
        sidebar = ctk.CTkFrame(self, width=220)
        sidebar.pack(side="left", fill="y", padx=(12, 6), pady=12)

        titulo = ctk.CTkLabel(
            sidebar, text="Aulas e Scripts", font=(None, 18, "bold"))
        titulo.pack(pady=(6, 12))

        # Scrollable frame para acomodar muitos botões
        try:
            scroll = ctk.CTkScrollableFrame(sidebar, width=200, height=440)
            scroll.pack(expand=True, fill="both", padx=8, pady=6)
        except Exception:
            # fallback se a versão do customtkinter não tiver o widget
            scroll = ctk.CTkFrame(sidebar)
            scroll.pack(expand=True, fill="both", padx=8, pady=6)

        scripts = list(self._descobrir_scripts())
        if not scripts:
            ctk.CTkLabel(scroll, text="Nenhum script encontrado").pack(pady=20)
        else:
            for caminho in scripts:
                nome = caminho.stem
                btn = ctk.CTkButton(
                    master=scroll,
                    text=nome,
                    width=180,
                    command=lambda p=caminho: self._abrir_script(p),
                )
                btn.pack(pady=6)

        # Área principal de conteúdo
        self.content = ctk.CTkFrame(self)
        self.content.pack(side="right", expand=True,
                     fill="both", padx=(6, 12), pady=12)
        self.current_frame = None

        ctk.CTkLabel(
            self.content,
            text="Clique em um botão para abrir o script embutido na mesma janela.",
            font=(None, 16),
        ).pack(pady=(24, 6))

    def _descobrir_scripts(self) -> Iterable[Path]:
        raiz = Path(__file__).parent
        arquivos: List[Path] = []
        for p in sorted(raiz.glob("*.py")):
            if p.name in EXCLUIR:
                continue
            arquivos.append(p)
        return arquivos

    def _clear_content(self) -> None:
        for child in self.content.winfo_children():
            child.destroy()
        self.current_frame = None

    def _abrir_script(self, caminho: Path) -> None:
        import importlib.util
        try:
            spec = importlib.util.spec_from_file_location(caminho.stem, caminho)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except Exception as erro:
            LOGGER.exception("Falha ao importar o módulo: %s", caminho)
            messagebox.showerror("Erro", f"Não foi possível importar {caminho.name}: {erro}")
            return

        # limpa área de conteúdo
        self._clear_content()

        # procura por subclasses de CTkFrame no módulo
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            try:
                if isinstance(attr, type) and issubclass(attr, ctk.CTkFrame):
                    frame = attr(self.content)
                    frame.pack(expand=True, fill="both")
                    self.current_frame = frame
                    return
            except Exception:
                continue

        # tenta funções conhecidas que constroem widgets no widget fornecido
        builder_names = [
            "criar_widgets", "criar_tabs", "criar_caixa_texto", "criar_option_menu",
            "criar_label", "adicionar_botao", "abrir_dialogo", "criar_label_de_titulo_da_janela",
            "criar_widgets",
        ]
        for name in builder_names:
            if hasattr(module, name):
                func = getattr(module, name)
                try:
                    func(self.content)
                    return
                except TypeError:
                    try:
                        func()
                        return
                    except Exception:
                        pass
                except Exception:
                    pass

        messagebox.showinfo("Não suportado", f"O script {caminho.name} não fornece um frame ou função de construção compatível.")


if __name__ == "__main__":
    app = MenuPrincipal(aparencia="System")
    app.mainloop()
