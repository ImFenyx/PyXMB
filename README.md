# PyXMB

Um launcher desktop em Python que emula a experiência de usuário da XMB (XrossMediaBar), inspirado no menu da PlayStation.

## Características

- **Interface Gráfica XMB**: Menu horizontal com categorias e sub-itens verticais
- **Navegação Fluida**: Efeitos de ondas animadas e transições suaves
- **Controle Múltiplo**: Suporte para teclado e gamepad
- **Configurável**: Sistema de configuração baseado em JSON
- **Lançador de Aplicações**: Execute jogos, visualizadores de imagens, players de música e mais

## Instalação

### Requisitos

- Python 3.8 ou superior
- Pygame 2.5.0 ou superior

### Instalação via pip

```bash
# Clone o repositório
git clone https://github.com/ImFenyx/PyXMB.git
cd PyXMB

# Instale as dependências
pip install -r requirements.txt

# Instale o pacote
pip install -e .
```

## Uso

### Executar PyXMB

```bash
# Executar com configuração padrão
pyxmb

# Executar com arquivo de configuração personalizado
pyxmb --config /caminho/para/config.json
```

Ou execute diretamente via Python:

```bash
python -m pyxmb.main
```

### Controles

#### Teclado

- **← / →** ou **A / D**: Navegar entre categorias (horizontal)
- **↑ / ↓** ou **W / S**: Navegar entre itens (vertical)
- **Enter** ou **Espaço**: Selecionar/Confirmar
- **ESC**: Voltar/Sair

#### Gamepad

- **D-Pad** ou **Analógico Esquerdo**: Navegação
- **Botão A/Cross**: Selecionar
- **Botão B/Circle**: Voltar

## Configuração

A configuração é armazenada em `~/.pyxmb/config.json`. Na primeira execução, um arquivo de configuração padrão é criado automaticamente.

### Estrutura da Configuração

```json
{
  "categories": [
    {
      "name": "Nome da Categoria",
      "icon": "identificador_icone",
      "items": [
        {
          "name": "Nome do Item",
          "type": "launcher",
          "command": "comando_para_executar"
        }
      ]
    }
  ],
  "theme": {
    "background_color": [0, 20, 40],
    "wave_color": [100, 150, 200],
    "text_color": [255, 255, 255],
    "selected_color": [255, 200, 100]
  }
}
```

### Categorias Padrão

1. **Configurações**: Sistema e informações
2. **Fotos**: Visualizador de imagens
3. **Músicas**: Player de música
4. **Vídeos**: Player de vídeo
5. **Jogos**: Lançador de jogos (ex: Steam)

### Tipos de Itens

- **launcher**: Executa um comando externo (aplicação)
- **action**: Executa uma ação interna (ex: "about", "system_info")

### Exemplo de Item

```json
{
  "name": "Steam",
  "type": "launcher",
  "command": "steam"
}
```

## Personalização

### Adicionar Nova Categoria

Edite `~/.pyxmb/config.json` e adicione uma nova categoria:

```json
{
  "name": "Minha Categoria",
  "icon": "custom",
  "items": [
    {
      "name": "Minha Aplicação",
      "type": "launcher",
      "command": "meu-comando"
    }
  ]
}
```

### Modificar Cores do Tema

Ajuste as cores RGB no objeto `theme`:

```json
"theme": {
  "background_color": [10, 10, 30],
  "wave_color": [50, 100, 200],
  "text_color": [255, 255, 255],
  "selected_color": [255, 150, 50]
}
```

## Desenvolvimento

### Estrutura do Projeto

```
PyXMB/
├── pyxmb/
│   ├── __init__.py
│   ├── main.py          # Aplicação principal e loop
│   ├── config.py        # Gerenciamento de configuração
│   ├── renderer.py      # Renderização da interface XMB
│   ├── input_handler.py # Controle de entrada (teclado/gamepad)
│   └── launcher.py      # Lançador de aplicações
├── requirements.txt
├── setup.py
└── README.md
```

### Executar em Modo de Desenvolvimento

```bash
# Instalar dependências de desenvolvimento
pip install -r requirements.txt

# Executar diretamente
python -m pyxmb.main
```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto é de código aberto. Veja o arquivo LICENSE para mais detalhes.

## Créditos

Inspirado pela interface XrossMediaBar (XMB) da Sony PlayStation.