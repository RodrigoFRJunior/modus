import customtkinter as ctk
import serial
import serial.tools.list_ports
import threading
import json
import os
import webbrowser


# ============================================================
# CONFIGURAÇÕES
# ============================================================

ARQUIVO_CONFIG = "config.json"

CONFIG_PADRAO = {
    "A5:1": {
        "nome": "Google",
        "tipo": "site",
        "destino": "https://www.google.com"
    },
    "A5:2": {
        "nome": "WordPad",
        "tipo": "programa",
        "destino": "write.exe"
    },
    "A5:3": {
        "nome": "Google Drive",
        "tipo": "site",
        "destino": "https://drive.google.com"
    },
    "A5:4": {
        "nome": "YouTube",
        "tipo": "site",
        "destino": "https://youtube.com"
    }
}


# ============================================================
# CONFIGURAÇÃO
# ============================================================

def salvar_config(config):

    with open(
        ARQUIVO_CONFIG,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            config,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def carregar_config():

    if not os.path.exists(ARQUIVO_CONFIG):

        salvar_config(CONFIG_PADRAO)

        return CONFIG_PADRAO.copy()

    try:

        with open(
            ARQUIVO_CONFIG,
            "r",
            encoding="utf-8"
        ) as arquivo:

            return json.load(arquivo)

    except Exception:

        return CONFIG_PADRAO.copy()


# ============================================================
# ENCONTRAR APLICATIVOS DO WINDOWS
# ============================================================

def encontrar_aplicativos():

    pastas = [
        os.path.join(
            os.environ.get("APPDATA", ""),
            "Microsoft",
            "Windows",
            "Start Menu",
            "Programs"
        ),

        os.path.join(
            os.environ.get("PROGRAMDATA", ""),
            "Microsoft",
            "Windows",
            "Start Menu",
            "Programs"
        )
    ]

    aplicativos = {}

    for pasta in pastas:

        if not os.path.exists(pasta):
            continue

        for raiz, diretorios, arquivos in os.walk(pasta):

            for arquivo in arquivos:

                if arquivo.lower().endswith(".lnk"):

                    nome = os.path.splitext(
                        arquivo
                    )[0]

                    caminho = os.path.join(
                        raiz,
                        arquivo
                    )

                    if nome not in aplicativos:

                        aplicativos[nome] = caminho

    return dict(
        sorted(
            aplicativos.items(),
            key=lambda item: item[0].lower()
        )
    )


# ============================================================
# EXECUTAR AÇÃO
# ============================================================

def executar_acao(configuracao):

    tipo = configuracao.get("tipo")
    destino = configuracao.get("destino")

    if not destino:
        return

    try:

        if tipo == "site":

            webbrowser.open(destino)

        elif tipo == "programa":

            os.startfile(destino)

        elif tipo == "pasta":

            os.startfile(destino)

    except Exception as erro:

        print(
            "Erro ao executar:",
            erro
        )


# ============================================================
# APLICATIVO
# ============================================================

class ControllerApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        # ----------------------------------------------------
        # JANELA
        # ----------------------------------------------------

        self.title("Controller")

        self.geometry("900x680")

        self.minsize(
            800,
            600
        )

        # ----------------------------------------------------
        # VARIÁVEIS
        # ----------------------------------------------------

        self.arduino = None

        self.conectado = False

        self.config = carregar_config()

        self.aplicativos = encontrar_aplicativos()

        self.botoes = {}

        # ----------------------------------------------------
        # INTERFACE
        # ----------------------------------------------------

        self.criar_interface()

        self.atualizar_portas()

        self.atualizar_botoes()


    # ========================================================
    # INTERFACE PRINCIPAL
    # ========================================================

    def criar_interface(self):

        # ----------------------------------------------------
        # CABEÇALHO
        # ----------------------------------------------------

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(25, 10)
        )

        titulo = ctk.CTkLabel(
            header,
            text="CONTROLLER",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        )

        titulo.pack(
            anchor="w"
        )

        subtitulo = ctk.CTkLabel(
            header,
            text="USB Control Center",
            text_color="#888888"
        )

        subtitulo.pack(
            anchor="w"
        )


        # ----------------------------------------------------
        # CONEXÃO
        # ----------------------------------------------------

        conexao = ctk.CTkFrame(
            self,
            corner_radius=14
        )

        conexao.pack(
            fill="x",
            padx=30,
            pady=10
        )

        self.status_label = ctk.CTkLabel(
            conexao,
            text="● Desconectado",
            text_color="#ff5c5c",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            )
        )

        self.status_label.pack(
            side="left",
            padx=20,
            pady=15
        )

        self.porta_combo = ctk.CTkComboBox(
            conexao,
            width=130,
            values=["Nenhuma"]
        )

        self.porta_combo.pack(
            side="right",
            padx=(5, 10)
        )

        self.atualizar_btn = ctk.CTkButton(
            conexao,
            text="Atualizar",
            width=100,
            command=self.atualizar_portas
        )

        self.atualizar_btn.pack(
            side="right"
        )

        self.conectar_btn = ctk.CTkButton(
            conexao,
            text="Conectar",
            width=110,
            command=self.conectar
        )

        self.conectar_btn.pack(
            side="right",
            padx=10
        )


        # ----------------------------------------------------
        # TÍTULO DOS CONTROLES
        # ----------------------------------------------------

        controles = ctk.CTkLabel(
            self,
            text="CONTROLES",
            font=ctk.CTkFont(
                size=15,
                weight="bold"
            )
        )

        controles.pack(
            anchor="w",
            padx=35,
            pady=(20, 5)
        )


        # ----------------------------------------------------
        # ÁREA DOS BOTÕES
        # ----------------------------------------------------

        self.botoes_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.botoes_frame.pack(
            expand=True,
            fill="both",
            padx=30,
            pady=5
        )

        for linha in range(2):

            self.botoes_frame.grid_rowconfigure(
                linha,
                weight=1
            )

        for coluna in range(2):

            self.botoes_frame.grid_columnconfigure(
                coluna,
                weight=1
            )

        for numero in range(1, 5):

            self.criar_botao(numero)


        # ----------------------------------------------------
        # RODAPÉ
        # ----------------------------------------------------

        footer = ctk.CTkLabel(
            self,
            text="Clique para executar  •  Botão direito para configurar",
            text_color="#777777"
        )

        footer.pack(
            pady=(5, 20)
        )


    # ========================================================
    # CRIAR BOTÃO
    # ========================================================

    def criar_botao(self, numero):

        linha = (numero - 1) // 2

        coluna = (numero - 1) % 2

        chave = f"A5:{numero}"

        botao = ctk.CTkButton(
            self.botoes_frame,

            text=f"{numero:02d}",

            font=ctk.CTkFont(
                size=20,
                weight="bold"
            ),

            corner_radius=18,

            fg_color="#1c1c1c",

            hover_color="#292929",

            border_width=1,

            border_color="#363636",

            command=lambda c=chave:
            self.executar_botao(c)
        )

        botao.grid(
            row=linha,
            column=coluna,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        botao.bind(
            "<Button-3>",
            lambda evento, c=chave:
            self.editar_botao(c)
        )

        self.botoes[chave] = botao


    # ========================================================
    # ATUALIZAR BOTÕES
    # ========================================================

    def atualizar_botoes(self):

        for chave, botao in self.botoes.items():

            numero = chave.split(":")[1]

            dados = self.config.get(
                chave,
                {}
            )

            nome = dados.get(
                "nome",
                "Não configurado"
            )

            tipo = dados.get(
                "tipo",
                ""
            )

            if tipo:

                tipo_exibicao = tipo.capitalize()

            else:

                tipo_exibicao = ""

            botao.configure(
                text=(
                    f"{int(numero):02d}\n\n"
                    f"{nome}\n"
                    f"{tipo_exibicao}"
                )
            )


    # ========================================================
    # ATUALIZAR PORTAS
    # ========================================================

    def atualizar_portas(self):

        portas = []

        for porta in serial.tools.list_ports.comports():

            portas.append(
                porta.device
            )

        if portas:

            self.porta_combo.configure(
                values=portas
            )

            self.porta_combo.set(
                portas[0]
            )

        else:

            self.porta_combo.configure(
                values=["Nenhuma"]
            )

            self.porta_combo.set(
                "Nenhuma"
            )


    # ========================================================
    # CONECTAR
    # ========================================================

    def conectar(self):

        if self.conectado:

            self.desconectar()

            return

        porta = self.porta_combo.get()

        if porta == "Nenhuma":

            return

        try:

            self.arduino = serial.Serial(
                porta,
                115200,
                timeout=1
            )

            self.conectado = True

            self.status_label.configure(
                text="● Conectado",
                text_color="#4ade80"
            )

            self.conectar_btn.configure(
                text="Desconectar"
            )

            thread = threading.Thread(
                target=self.escutar_arduino,
                daemon=True
            )

            thread.start()

        except Exception as erro:

            print(
                "Erro ao conectar:",
                erro
            )


    # ========================================================
    # DESCONECTAR
    # ========================================================

    def desconectar(self):

        self.conectado = False

        if self.arduino:

            try:

                self.arduino.close()

            except Exception:

                pass

        self.arduino = None

        self.status_label.configure(
            text="● Desconectado",
            text_color="#ff5c5c"
        )

        self.conectar_btn.configure(
            text="Conectar"
        )


    # ========================================================
    # ESCUTAR ARDUINO
    # ========================================================

    def escutar_arduino(self):

        while self.conectado:

            try:

                comando = (
                    self.arduino
                    .readline()
                    .decode(
                        "utf-8",
                        errors="ignore"
                    )
                    .strip()
                )

                if comando:

                    self.after(
                        0,
                        self.receber_comando,
                        comando
                    )

            except Exception:

                break


    # ========================================================
    # RECEBER COMANDO
    # ========================================================

    def receber_comando(
        self,
        comando
    ):

        print(
            "Arduino:",
            comando
        )

        if comando in self.config:

            self.executar_botao(
                comando
            )


    # ========================================================
    # EXECUTAR BOTÃO
    # ========================================================

    def executar_botao(
        self,
        chave
    ):

        dados = self.config.get(
            chave
        )

        if not dados:

            return

        executar_acao(
            dados
        )


    # ========================================================
    # EDITAR BOTÃO
    # ========================================================

    def editar_botao(
        self,
        chave
    ):

        dados = self.config.get(
            chave,
            {}
        )

        numero = chave.split(":")[1]

        janela = ctk.CTkToplevel(
            self
        )

        janela.title(
            f"Configurar botão {numero}"
        )

        janela.geometry(
            "520x500"
        )

        janela.resizable(
            False,
            False
        )

        janela.grab_set()


        # ----------------------------------------------------
        # TÍTULO
        # ----------------------------------------------------

        ctk.CTkLabel(
            janela,
            text=f"CONFIGURAR BOTÃO {int(numero):02d}",
            font=ctk.CTkFont(
                size=22,
                weight="bold"
            )
        ).pack(
            anchor="w",
            padx=30,
            pady=(25, 5)
        )

        ctk.CTkLabel(
            janela,
            text="Configure a ação deste botão.",
            text_color="#888888"
        ).pack(
            anchor="w",
            padx=30,
            pady=(0, 15)
        )


        # ----------------------------------------------------
        # NOME
        # ----------------------------------------------------

        ctk.CTkLabel(
            janela,
            text="Nome",
            font=ctk.CTkFont(
                size=13,
                weight="bold"
            )
        ).pack(
            anchor="w",
            padx=30,
            pady=(5, 5)
        )

        nome = ctk.CTkEntry(
            janela,
            width=460,
            height=38,
            placeholder_text="Ex.: Google Chrome"
        )

        nome.pack(
            padx=30
        )

        nome.insert(
            0,
            dados.get(
                "nome",
                ""
            )
        )


        # ----------------------------------------------------
        # TIPO
        # ----------------------------------------------------

        ctk.CTkLabel(
            janela,
            text="Ação",
            font=ctk.CTkFont(
                size=13,
                weight="bold"
            )
        ).pack(
            anchor="w",
            padx=30,
            pady=(18, 5)
        )

        tipo = ctk.CTkComboBox(
            janela,
            width=460,
            height=38,
            values=[
                "programa",
                "site",
                "pasta"
            ]
        )

        tipo.pack(
            padx=30
        )

        tipo.set(
            dados.get(
                "tipo",
                "programa"
            )
        )


        # ----------------------------------------------------
        # DESTINO
        # ----------------------------------------------------

        ctk.CTkLabel(
            janela,
            text="Destino",
            font=ctk.CTkFont(
                size=13,
                weight="bold"
            )
        ).pack(
            anchor="w",
            padx=30,
            pady=(18, 5)
        )

        destino = ctk.CTkEntry(
            janela,
            width=460,
            height=38,
            placeholder_text="Destino"
        )

        destino.pack(
            padx=30
        )

        destino.insert(
            0,
            dados.get(
                "destino",
                ""
            )
        )


        # ----------------------------------------------------
        # SELECIONAR APLICATIVO
        # ----------------------------------------------------

        selecionar_btn = ctk.CTkButton(
            janela,
            text="Selecionar aplicativo",
            width=210,
            height=36
        )

        selecionar_btn.pack(
            pady=(12, 5)
        )


        def abrir_seletor():

            self.selecionar_aplicativo(
                nome,
                tipo,
                destino
            )


        selecionar_btn.configure(
            command=abrir_seletor
        )


        # ----------------------------------------------------
        # BOTÕES
        # ----------------------------------------------------

        area_botoes = ctk.CTkFrame(
            janela,
            fg_color="transparent"
        )

        area_botoes.pack(
            fill="x",
            padx=30,
            pady=(20, 20)
        )


        # ----------------------------------------------------
        # LIMPAR
        # ----------------------------------------------------

        def limpar():

            self.config.pop(
                chave,
                None
            )

            salvar_config(
                self.config
            )

            self.atualizar_botoes()

            janela.destroy()


        limpar_btn = ctk.CTkButton(
            area_botoes,
            text="Limpar",
            width=130,
            height=40,
            fg_color="#2a2a2a",
            hover_color="#3a3a3a",
            command=limpar
        )

        limpar_btn.pack(
            side="left"
        )


        # ----------------------------------------------------
        # SALVAR
        # ----------------------------------------------------

        def salvar():

            nome_valor = nome.get().strip()

            tipo_valor = tipo.get()

            destino_valor = destino.get().strip()

            if not nome_valor:

                nome_valor = f"Botão {numero}"

            self.config[chave] = {

                "nome": nome_valor,

                "tipo": tipo_valor,

                "destino": destino_valor

            }

            salvar_config(
                self.config
            )

            self.atualizar_botoes()

            janela.destroy()


        salvar_btn = ctk.CTkButton(
            area_botoes,
            text="✓  Salvar",
            width=180,
            height=40,
            command=salvar
        )

        salvar_btn.pack(
            side="right"
        )


    # ========================================================
    # SELECIONAR APLICATIVO
    # ========================================================

    def selecionar_aplicativo(
        self,
        campo_nome,
        campo_tipo,
        campo_destino
    ):

        janela = ctk.CTkToplevel(
            self
        )

        janela.title(
            "Selecionar aplicativo"
        )

        janela.geometry(
            "500x540"
        )

        janela.resizable(
            False,
            False
        )

        janela.grab_set()


        ctk.CTkLabel(
            janela,
            text="SELECIONAR APLICATIVO",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        ).pack(
            pady=(25, 5)
        )

        ctk.CTkLabel(
            janela,
            text="Escolha um aplicativo do Windows.",
            text_color="#888888"
        ).pack(
            pady=(0, 15)
        )


        pesquisa = ctk.CTkEntry(
            janela,
            width=430,
            height=38,
            placeholder_text="Pesquisar aplicativo..."
        )

        pesquisa.pack(
            pady=5
        )


        lista = ctk.CTkScrollableFrame(
            janela,
            width=430,
            height=330
        )

        lista.pack(
            pady=15
        )


        botoes_app = []

        nomes = list(
            self.aplicativos.keys()
        )


        def atualizar_lista(event=None):

            for widget in botoes_app:

                widget.destroy()

            botoes_app.clear()

            texto = pesquisa.get().lower()

            for aplicativo in nomes:

                if texto not in aplicativo.lower():

                    continue

                caminho = self.aplicativos[
                    aplicativo
                ]


                def escolher(
                    nome_app=aplicativo,
                    caminho_app=caminho
                ):

                    campo_nome.delete(
                        0,
                        "end"
                    )

                    campo_nome.insert(
                        0,
                        nome_app
                    )

                    campo_tipo.set(
                        "programa"
                    )

                    campo_destino.delete(
                        0,
                        "end"
                    )

                    campo_destino.insert(
                        0,
                        caminho_app
                    )

                    janela.destroy()


                botao = ctk.CTkButton(
                    lista,
                    text=aplicativo,
                    anchor="w",
                    height=36,
                    fg_color="transparent",
                    hover_color="#2a2a2a",
                    command=escolher
                )

                botao.pack(
                    fill="x",
                    pady=2
                )

                botoes_app.append(
                    botao
                )


        pesquisa.bind(
            "<KeyRelease>",
            atualizar_lista
        )

        atualizar_lista()


    # ========================================================
    # FECHAR APLICATIVO
    # ========================================================

    def fechar(self):

        self.desconectar()

        self.destroy()


# ============================================================
# INICIALIZAÇÃO
# ============================================================

ctk.set_appearance_mode(
    "dark"
)

ctk.set_default_color_theme(
    "dark-blue"
)


app = ControllerApp()


app.protocol(
    "WM_DELETE_WINDOW",
    app.fechar
)


app.mainloop()