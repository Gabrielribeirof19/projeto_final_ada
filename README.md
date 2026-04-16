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

## 🎬 Cadastro de Filmes

Formulário utilizado para cadastrar um novo filme e atribuir uma nota.

<p align="center">
  <img src="docs/images/cadastrar-filme.png" width="700">
</p>

O sistema recebe o nome do filme e a nota atribuída pelo usuário.

---

## ⭐ Lista de Filmes Avaliados

Após o cadastro, os filmes são armazenados no banco de dados e exibidos na lista.

<p align="center">
  <img src="docs/images/lista-filmes.png" width="700">
</p>

Cada item da lista mostra:

* Nome do filme
* Nota atribuída

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

## 📂 Estrutura das imagens no repositório

```
docs/
 └── images/
      ├── tela-home.png
      ├── cadastrar-filme.png
      ├── lista-filmes.png
      ├── docker-containers.png
      └── github-actions.png
```
