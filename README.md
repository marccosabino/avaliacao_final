# Sistema de Recomendação com FastAPI e Docker

Este projeto implementa um **sistema de recomendação** utilizando **FastAPI** para a construção da API e **Docker** para a containerização da aplicação. O objetivo é oferecer uma aplicação completa que permita registrar usuários, itens, avaliações e gerar recomendações personalizadas.

---

## 🚀 Funcionalidades

A API oferece os seguintes recursos:

- **Adicionar usuários**
- **Adicionar itens (ex: filmes)**
- **Registrar avaliações (ratings)**
- **Gerar recomendações personalizadas**
- Documentação automática via Swagger

---

## 🧠 Modelo de Recomendação

O sistema utiliza um modelo baseado em **filtragem colaborativa**, capaz de:

- Considerar avaliações de diferentes usuários
- Identificar similaridades entre itens
- Calcular um score de recomendação
- Retornar uma lista ordenada de itens recomendados

Tecnologias utilizadas:

- `Python`
- `FastAPI`
- `Pandas`
- `CSV`
- `Scikit-learn`
- `NumPy`
- `Uvicorn`
- `zipfile`
- `Pydantic`
- `MovieLens`
- `Docker`
- Lógica personalizada no arquivo `recommender.py`

---

## 📁 Estrutura do Projeto

```
avaliacao_final/
│
├── app/
│   ├── main.py
│   ├── recommender.py
│   ├── storage.py
│   ├── schemas.py
│
├── tests/
│   ├── test_api.py
│
├── requirements.txt
├── Dockerfile
└── README.md
```


---

## 🐳 Executando com Docker

### 🔨 1. Build da imagem
No diretório raiz do projeto:

```bash
docker build -t recomendador .
```

## ▶️ 2. Rodar o container
```
docker run -p 8000:8000 recomendador
```

## 🌐 3. Acessar o Swagger
Abra no navegador:
```
http://localhost:8000/docs
```


## 🖥️ Executando Localmente (sem Docker)
1. Criar ambiente virtual (opcional)
```
python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows
```
2. Instalar dependências
```
pip install -r requirements.txt
```
3. Rodar o servidor FastAPI
```
uvicorn app.main:app --reload
```
## 📌 Endpoints da API
### POST /users
Cria um novo usuário.

### POST /items
Registra um novo item.

### PUT /ratings
Adiciona ou atualiza a avaliação de um usuário para um item.

### GET /recommendations/{user_id}
Retorna recomendações personalizadas para o usuário informado.

## 🧪 Testes
Os testes estão no diretório tests/.

Para rodar:
```
pytest
```
## 📄 Decisões de Projeto
- A API foi construída utilizando **FastAPI**, pela leveza e documentação automática.
- O armazenamento utiliza estrutura **em memória**, facilitando testes.
- O modelo de recomendação utiliza **filtragem colaborativa simples**.
- O uso de **Docker** padroniza o ambiente e facilita a execução.

## 👨‍🏫 Exigências Atendidas
✔ Modelo de recomendação implementado

✔ API completa com FastAPI

✔ Containerização com Docker

✔ Documentação automática (Swagger)

✔ Testes automatizados

✔ README completo

## 🏁 Conclusão
Este sistema apresenta uma solução completa de recomendação, totalmente funcional, documentada e containerizada — atendendo a todos os requisitos propostos na atividade.
