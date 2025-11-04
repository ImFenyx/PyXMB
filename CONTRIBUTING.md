# Contribuindo para PyXMB

Obrigado por considerar contribuir com PyXMB! Este documento fornece diretrizes para contribuir com o projeto.

## Como Contribuir

### Reportando Bugs

Se você encontrar um bug, por favor abra uma issue incluindo:

- Descrição clara do problema
- Passos para reproduzir
- Comportamento esperado vs. comportamento atual
- Versão do Python e sistema operacional
- Logs de erro, se aplicável

### Sugerindo Melhorias

Sugestões de melhorias são bem-vindas! Abra uma issue descrevendo:

- Qual melhoria você gostaria de ver
- Por que essa melhoria seria útil
- Como você imagina que funcionaria

### Pull Requests

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Faça commit das suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

### Diretrizes de Código

- Siga o PEP 8 para estilo de código Python
- Adicione docstrings para novas funções e classes
- Mantenha a compatibilidade com Python 3.8+
- Teste suas mudanças antes de submeter

### Estrutura do Projeto

```
PyXMB/
├── pyxmb/              # Código principal
│   ├── main.py         # Aplicação e loop principal
│   ├── config.py       # Gerenciamento de configuração
│   ├── renderer.py     # Renderização da interface
│   ├── input_handler.py # Controle de entrada
│   └── launcher.py     # Lançador de aplicações
├── requirements.txt    # Dependências
├── setup.py           # Configuração do pacote
├── test_pyxmb.py      # Testes
└── demo.py            # Script de demonstração
```

### Áreas que Precisam de Ajuda

- Ícones personalizados para categorias
- Temas adicionais
- Suporte para mais tipos de itens
- Melhorias na animação
- Testes adicionais
- Tradução para outros idiomas
- Documentação

## Código de Conduta

- Seja respeitoso e construtivo
- Aceite críticas construtivas
- Foque no que é melhor para a comunidade

## Dúvidas?

Se tiver dúvidas, sinta-se à vontade para abrir uma issue ou entrar em contato.

Obrigado por contribuir! 🎉
