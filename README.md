# Sistema de Login em Python (JSON)

Sistema simples de cadastro e login usando arquivos JSON para armazenar dados dos usuários.  
Ideal para estudos sobre CRUD, manipulação de arquivos e autenticação básica.

---

## Funcionalidades

- Criar nova conta  
- Fazer login  
- Armazenar dados no arquivo `usuarios.json`  
- Criar automaticamente o arquivo caso não exista  
- Código limpo e direto ao ponto  

---

## Tecnologias utilizadas

- Python 3  
- Biblioteca `json` (nativa)

---

## Como executar

```bash
git clone https://github.com/thxxuz/sistema-login-python
cd sistema-login-python
python main.py
```

---

## Estrutura do projeto

```
sistema-login-python/
│
├── main.py        -> código principal do sistema
├── funcoes.py     -> funções auxiliares
└── usuarios.json  -> onde os dados são armazenados
```

---

## Resetar o sistema

Para apagar todos os usuários cadastrados, basta deletar o arquivo:

```
usuarios.json
```

Ele será recriado automaticamente na próxima execução.

---

## Observações

Esse projeto é ótimo para quem está começando e quer entender:

- CRUD simples  
- Salvamento de dados sem usar banco de dados  
- Organização de código em módulos  
- Estrutura básica de autenticação


