# Sistema de Recomendação com FastAPI e Docker

Este projeto implementa um **sistema de recomendação** utilizando **FastAPI** para a construção da API e **Docker** para a containerização da aplicação.  
O objetivo é oferecer uma aplicação completa que permita registrar usuários, itens, avaliações e gerar recomendações personalizadas.

---

## 🚀 Funcionalidades

A API oferece os seguintes recursos:

- **Adicionar usuários**  
- **Adicionar itens (ex: filmes)**  
- **Registrar avaliações (ratings)**  
- **Gerar recomendações personalizadas** com base no modelo implementado  
- Documentação automática via Swagger  

---

## 🧠 Modelo de Recomendação

O sistema utiliza um modelo baseado em **filtragem colaborativa**, capaz de:

- Considerar avaliações de diferentes usuários  
- Identificar similaridades entre itens  
- Calcular um score de recomendação  
- Retornar uma lista ordenada de itens recomendados  

Utiliza bibliotecas como:

- `numpy`  
- `pandas`  
- Lógica personalizada dentro da classe `Recommender`

---

## 📁 Estrutura do Projeto

