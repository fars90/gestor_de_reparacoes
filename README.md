# Sistema de Gestão de Assistência Técnica

Este projeto foi desenvolvido no âmbito da UFCD de Projeto de Programação e simula uma aplicação de **gestão de assistência técnica** para pequenas empresas, técnicos independentes ou lojas de reparações.

Permite o registo de clientes, equipamentos, gestão de estados de reparações, e exportação de relatórios. O objetivo é criar uma ferramenta útil, simples e adaptada ao dia a dia de um negócio técnico.

---

## Funcionalidades principais

- Registo de clientes e equipamentos
- Acompanhamento do estado das reparações
- Consultas e histórico por cliente ou estado
- Login para técnicos (controlo de acesso)
- Exportação de relatórios em ficheiro
- Armazenamento de dados persistente (SQLite ou JSON)

---

## Estrutura do Projeto

```
projeto/
├── main.py               # Ficheiro principal da aplicação
├── cliente.py            # Módulo de gestão de clientes
├── equipamento.py        # Módulo de gestão de equipamentos
├── tecnico.py            # Login e utilizadores
├── base_dados.py         # Ligação à base de dados (mySQL/JSON)
├── relatorios.py         # Geração de relatórios
├── README.md             # Este ficheiro
└── requirements.txt      # Bibliotecas necessárias (se aplicável)
```

---

## Como executar

1. **Pré-requisitos**:
   - Python 3.x
   - (Opcional) Instalar bibliotecas: `pip install -r requirements.txt`

2. **Executar a aplicação**:
   ```bash
   python main.py
   ```

---

## Autor

Projeto realizado por: **André Faria**  
Curso de Linguagens de Programação - Python, IEFP  
Ano letivo 2024/2025

---

## Licença

Este projeto é de uso académico. Todos os direitos reservados ao autor.


