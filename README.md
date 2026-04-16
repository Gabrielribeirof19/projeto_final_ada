## 📸 Demonstração da Aplicação

Esta seção apresenta capturas de tela da aplicação em funcionamento, mostrando o fluxo principal do sistema.

As imagens criadas com sucesso atraves do docker desktop:
<p align="center">
  <img src="docs/images/images-working.png" width="700">
</p>

---

## 🖥️ Aplicação Web

Tela inicial da aplicação para cadastro e avaliação de filmes.

<p align="center">
  <img src="docs/images/tela-home.png" width="700">
</p>

Nesta tela o usuário pode visualizar os filmes cadastrados e suas respectivas avaliações.

---

---

## 🐳 Containers em execução

A aplicação é executada utilizando containers com Docker.

<p align="center">
  <img src="docs/images/docker-containers.png" width="700">
</p>

Os serviços são orquestrados utilizando **Docker Compose**, contendo:

* Aplicação Web
* Banco de dados PostgreSQL

---

## ⚙️ Pipeline CI/CD

O projeto possui uma pipeline automática utilizando GitHub Actions.

<p align="center">
  <img src="docs/images/github-actions.png" width="700">
</p>

A pipeline executa automaticamente quando ocorre um **push no repositório**, realizando:

* checkout do código
* instalação das dependências
* build da imagem Docker
* execução da aplicação

---

## PIPELINE DE ETL RODANDO

O projeto possui uma pipeline automática utilizando GitHub Actions.

<p align="center">
  <img src="docs/images/github-actions-etl.png" width="700">
</p>

### link dos artefacts gerados:
https://github.com/Gabrielribeirof19/projeto_final_ada/actions/runs/24532952034/artifacts/6483215750

### Image do docker Hub
https://hub.docker.com/repository/docker/gabriel461/filmes-app

### CD Funcionando
<img width="1366" height="348" alt="image" src="https://github.com/user-attachments/assets/b25c9760-0688-40c0-ad47-46e5b33ffbc9" />


