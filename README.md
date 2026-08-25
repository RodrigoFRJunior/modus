# 🚀 Modus

> Um controlador de atalhos físicos para computador, desenvolvido com Arduino UNO e Python.

---

## 📌 Informações do projeto

| Informação | Detalhes |
| --- | --- |
| 📊 Status | Finalizado |
| 🧩 Categoria | Sistemas embarcados / Automação |
| 💻 Tecnologia principal | C++ e Python |
| 📅 Início | 14/08/2026 |
| 📅 Fim | 25/08/2026 |
| 🔗 Repositório | https://github.com/RodrigoFRJunior/modus.git |

---

## 📖 1. Sobre o projeto

### O que é?

O **Modus** é um controlador de atalhos físicos desenvolvido utilizando um **Arduino UNO** conectado a um computador por USB.

Através de botões físicos, o usuário pode executar diferentes ações no computador, como abrir aplicativos, sites e pastas.

O Arduino identifica o botão pressionado e envia a informação através da comunicação serial. Um aplicativo desenvolvido em Python recebe essa informação e executa a ação correspondente no Windows.

### 🎯 Objetivo

Mais do que criar um controlador de atalhos, o Modus é um projeto de estudo e prototipação focado na integração entre **hardware e software**.

O projeto também faz parte dos meus estudos e experimentos nas áreas de **Sistemas Embarcados, Automação, IoT e desenvolvimento de software**.

Durante o desenvolvimento, optei por utilizar o **Arduino UNO**, mesmo sendo uma placa bastante simples e com algumas limitações, justamente para explorar o quanto é possível construir utilizando uma plataforma acessível e de fácil disponibilidade.

### 💡 Problema que o projeto resolve

O projeto foi criado para facilitar o meu dia a dia na hora de encontrar e abrir rapidamente sites, planilhas, documentos, pastas e aplicativos específicos durante o horário de trabalho.

Em vez de procurar manualmente cada recurso no computador, uma ação pode ser executada através de um botão físico.

### 👥 Público / usuários

O projeto pode ser utilizado por qualquer pessoa que queira dinamizar o acesso a:

- Aplicativos
- Sites
- Pastas
- Documentos
- Atalhos e outras ações do computador

---

## ✨ 2. Funcionalidades

- Abrir aplicativos ✅ 2026-08-14
- Abrir sites ✅ 2026-08-14
- Abrir pastas ✅ 2026-08-14
- Configurar individualmente cada botão ✅ 2026-08-14
- Selecionar aplicativos instalados no Windows ✅ 2026-08-14
- Salvar configurações em arquivo JSON ✅ 2026-08-16
- Executar ações através dos botões físicos ✅ 2026-08-14
- Executar ações através da interface gráfica ✅ 2026-08-18
- Comunicação Arduino ↔ Python via USB/Serial ✅ 2026-08-14
- Utilizar diferentes ações sem alterar o código do Arduino ✅ 2026-08-16
- Possibilidade de expansão para novas funções 🔄

---

## 🏗️ 3. Arquitetura

### Visão geral

O Modus utiliza o Arduino UNO como controlador físico e um aplicativo desenvolvido em Python como intermediário entre o hardware e o sistema operacional.

O Arduino identifica o botão pressionado e envia um comando através da comunicação serial.

O aplicativo Python interpreta esse comando, consulta a configuração correspondente e solicita ao Windows que execute a ação configurada.

### 📐 Diagrama

```text
┌───────────────┐
│ Botão físico  │
└───────┬───────┘
        │
        ▼
┌────────────────┐
│  Arduino UNO   │
│     C++        │
└───────┬────────┘
        │
        │ USB / Serial
        ▼
┌────────────────┐
│ Aplicação      │
│ Python         │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│    Windows     │
└───────┬────────┘
        │
        ▼
┌─────────────────────────┐
│ Ação configurada        │
│                         │
│ • Aplicativo            │
│ • Site                  │
│ • Pasta                 │
└─────────────────────────┘
```

### 🔄 Fluxo de funcionamento

1. Usuário pressiona um botão físico.
2. Arduino identifica o botão.
3. Arduino envia o comando pela porta serial.
4. Aplicação Python recebe o comando.
5. Python identifica qual botão foi pressionado.
6. O programa consulta a configuração do botão.
7. O Windows executa a ação configurada.

Exemplo:

```text
Botão 1
   ↓
Arduino
   ↓
"A5:1"
   ↓
Python
   ↓
Configuração do botão 1
   ↓
Google Chrome
```

---

## 💻 4. Tecnologias utilizadas

| Tecnologia | Versão | Utilização |
| --- | --- | --- |
| Arduino UNO | - | Controlador físico |
| C++ | Arduino | Programação do microcontrolador |
| Python | 3.13.15 | Aplicação desktop |
| CustomTkinter | - | Interface gráfica |
| PySerial | - | Comunicação serial |
| JSON | - | Armazenamento das configurações |
| Windows | - | Sistema operacional alvo |

---

## 📦 5. Dependências

| Dependência | Versão | Função |
| --- | --- | --- |
| Python | 3.13.15 | Execução da aplicação |
| CustomTkinter | - | Interface gráfica |
| PySerial | - | Comunicação com Arduino |
| Arduino IDE | - | Compilação e envio do código para o Arduino |

Instalação:

```bash
python -m pip install customtkinter pyserial
```

---

## ⚙️ 6. Instalação e configuração

### Requisitos

- Arduino UNO
- Cabo USB
- 4 botões
- Protoboard
- Jumpers
- Computador com Windows
- Python 3 instalado
- Arduino IDE

### Instalação

Clone o repositório:

```bash
git clone https://github.com/RodrigoFRJunior/modus.git
```

Entre na pasta:

```bash
cd modus
```

Instale as dependências:

```bash
python -m pip install customtkinter pyserial
```

Abra o código do Arduino na Arduino IDE e envie o programa para o Arduino UNO.

Depois, execute a aplicação Python.

### Configuração

A aplicação utiliza um arquivo `config.json` para armazenar as configurações dos botões.

Exemplo:

```json
{
    "A5:1": {
        "nome": "Google",
        "tipo": "site",
        "destino": "https://www.google.com"
    },
    "A5:2": {
        "nome": "WordPad",
        "tipo": "programa",
        "destino": "write.exe"
    }
}
```

As configurações também podem ser alteradas através da interface gráfica.

---

## ▶️ 7. Como executar

### Arduino

1. Conecte o Arduino UNO ao computador.
2. Abra o projeto na Arduino IDE.
3. Selecione a placa Arduino UNO.
4. Selecione a porta COM correspondente.
5. Faça o upload do código.

### Aplicação

Execute:

```bash
python controller_moderno.py
```

Selecione a porta COM do Arduino e clique em **Conectar**.

### 🖥️ Resultado esperado

Após a conexão, a aplicação deverá indicar que o Arduino está conectado.

Ao pressionar um botão físico, a ação configurada para aquele botão será executada no computador.

Também é possível testar as ações diretamente pela interface gráfica.

---

## 🔌 8. Hardware / Eletrônica

### Componentes

| Componente | Quantidade | Função |
| --- | --- | --- |
| Arduino UNO | 1 | Controlador principal |
| Push Button | 4 | Entrada dos comandos |
| Protoboard | 1 | Montagem do circuito |
| Jumpers | - | Conexões elétricas |
| Cabo USB | 1 | Alimentação e comunicação com o computador |

### Ligações

| Componente | Pino Arduino | Função |
| --- | --- | --- |
| Botão 1 | Entrada digital | Comando A5:1 |
| Botão 2 | Entrada digital | Comando A5:2 |
| Botão 3 | Entrada digital | Comando A5:3 |
| Botão 4 | Entrada digital | Comando A5:4 |

> Os pinos utilizados podem ser alterados conforme a montagem e a versão do código.

### 📐 Circuito

> Adicione aqui o esquema elétrico ou circuito do Modus.

---

## 🧪 9. Testes

| Teste | Resultado esperado | Resultado obtido | Status |
| --- | --- | --- | --- |
| Pressionar botão 1 | Arduino identificar o comando | Funcionando | 🟢 |
| Pressionar botão 2 | Arduino identificar o comando | Funcionando | 🟢 |
| Pressionar botão 3 | Arduino identificar o comando | Funcionando | 🟢 |
| Pressionar botão 4 | Arduino identificar o comando | Funcionando | 🟢 |
| Comunicação USB/Serial | Python receber os comandos | Funcionando | 🟢 |
| Abrir aplicativo | Aplicativo iniciar | Funcionando | 🟢 |
| Abrir site | Navegador acessar o endereço | Funcionando | 🟢 |
| Abrir pasta | Windows abrir a pasta | Funcionando | 🟢 |
| Configuração dos botões | Alterar função sem editar Arduino | Funcionando | 🟢 |
| Interface gráfica | Controlar o Modus pelo computador | Funcionando | 🟢 |
| Seletor de aplicativos | Listar aplicativos instalados | Funcionando | 🟢 |

---

## 🐛 10. Problemas e soluções

### Problema 1

**Problema:**

O Arduino parecia reiniciar sempre que um botão era pressionado.

**Causa:**

O cabo estava conectado inicialmente em uma porta que não correspondia à conexão utilizada para comunicação com o Arduino.

**Solução:**

A conexão USB foi corrigida.

**Resultado:**

Comunicação restabelecida.

---

### Problema 2

**Problema:**

O Python não era reconhecido pelo Windows.

**Causa:**

O Python não estava disponível corretamente através do PATH/alias de execução.

**Solução:**

A instalação/configuração do Python foi corrigida.

**Resultado:**

Python 3.13.15 funcionando normalmente através do terminal.

---

### Problema 3

**Problema:**

O Python parecia não receber os comandos do Arduino.

**Causa:**

O Monitor Serial da Arduino IDE estava utilizando a mesma porta serial.

**Solução:**

O Monitor Serial foi fechado antes de executar o programa Python.

**Resultado:**

A aplicação Python passou a receber os comandos normalmente.

---

## 📈 11. Evolução do projeto

| Data | Alteração | Resultado |
| --- | --- | --- |
| 14/08/2026 | Início do projeto | 🟢 |
| 15/08/2026 | Primeiros testes com Arduino | 🟢 |
| 20/08/2026 | Comunicação Arduino + Python | 🟢 |
| 21/08/2026 | Execução de aplicativos e sites | 🟢 |
| 22/08/2026 | Criação da interface gráfica | 🟢 |
| 23/08/2026 | Configuração individual dos botões | 🟢 |
| 24/08/2026 | Seletor de aplicativos | 🟢 |
| 25/08/2026 | Finalização e documentação | 🟢 |

---

## 🧠 12. O que aprendi

Durante o desenvolvimento do Modus, foram trabalhados conceitos de:

- Comunicação serial entre Arduino e computador.
- Integração entre hardware e software.
- Programação em C++ para Arduino.
- Desenvolvimento de aplicações desktop em Python.
- Desenvolvimento de interfaces gráficas.
- Manipulação de arquivos JSON.
- Automação de tarefas no Windows.
- Identificação de portas COM.
- Configuração dinâmica de funções.
- Organização e documentação de projetos.

Um dos principais aprendizados foi perceber que mesmo utilizando um **Arduino UNO**, uma placa bastante acessível e com recursos limitados, é possível criar uma solução funcional quando o microcontrolador trabalha em conjunto com um software no computador.

---

## 🚀 13. Melhorias futuras

- [ ] Criar versão com mais botões
- [ ] Adicionar atalhos de teclado personalizados
- [ ] Criar sistema de perfis
- [ ] Adicionar ícones personalizados aos botões
- [ ] Melhorar a interface gráfica
- [ ] Criar inicialização automática com o Windows
- [ ] Criar versão específica para streaming
- [ ] Integrar com OBS Studio
- [ ] Avaliar comunicação sem fio
- [ ] Criar uma versão utilizando outros microcontroladores

---

## 📚 15. Referências

### Documentação

- Documentação oficial do Arduino: https://docs.arduino.cc/.
- Documentação do Python: https://docs.python.org/3.13/.
- Documentação do CustomTkinter: https://customtkinter-tomschimansky-com.translate.goog/documentation/?._x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc.
- Documentação do PySerial: https://pyserial.readthedocs.io/en/latest/.

### Artigos / Tutoriais

- Pesquisas e estudos realizados durante o desenvolvimento.

https://embarcados.com.br/arduino-comunicacao-serial/

https://docs.arduino.cc/language-reference/pt/fun%C3%A7%C3%B5es/communication/serial/


### Vídeos

- Conteúdos utilizados como apoio durante os testes e desenvolvimento.

JuliaLabs, Stream Deck DIY: Projeto Completo do Zero 🛠️
- https://www.youtube.com/watch?v=X_ZKeOIq-ek&t=19s

### Outros projetos

- Projetos de controladores físicos e interfaces de automação utilizados como referência conceitual.

Stream Deck da elgato: https://www.elgato.com/lm/pt/p/stream-deck-mini
---

## 📎 16. Arquivos do projeto

- 💻 Código Arduino: `/codigo_modus.py`
- 🐍 Aplicação Python: `/software`
- 🔌 Circuito: `/hardware`
- 📐 Modelagem 3D: `/3d`
- 🖼️ Imagens: `/assets`
- 📄 Documentação: `/docs`

---

## ✅ 17. Checklist final

- [x] Projeto descrito
- [x] Objetivo definido
- [x] Funcionalidades documentadas
- [x] Arquitetura registrada
- [x] Tecnologias registradas
- [x] Dependências registradas
- [x] Instalação documentada
- [x] Execução documentada
- [x] Testes registrados
- [x] Problemas e soluções registrados
- [ ] Imagens adicionadas
- [x] Melhorias futuras registradas
- [x] Referências adicionadas
- [ ] Código/arquivos anexados
- [x] Documentação revisada

---

## 💭 Observações

O Modus foi desenvolvido inicialmente como um projeto experimental para explorar a comunicação entre um microcontrolador e um computador.

A proposta é continuar utilizando o projeto como base para novos experimentos envolvendo **sistemas embarcados, automação, IoT e integração hardware/software**.

A escolha do Arduino UNO foi intencional: por ser uma placa de baixo custo, fácil acesso e presente em muitos ambientes educacionais, o projeto pode ser reproduzido e adaptado com facilidade.

O projeto também servirá como base para uma futura versão voltada ao controle de **lives e transmissões**, incluindo possíveis integrações com o OBS Studio.

---

## ⭐ Projeto

**Modus — Hardware simples. Software flexível.**

Desenvolvido por **Rodrigo Felipe**.
