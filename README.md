# Desenvolvimento de Software para Dispositivos Móveis

[![Instituição](https://img.shields.io/badge/UniRV-Universidade%20de%20Rio%20Verde-006432.svg)](https://www.unirv.edu.br/)
[![Curso](https://img.shields.io/badge/Faculdade-Engenharia%20de%20Software-blue.svg)]()
[![Semestre](https://img.shields.io/badge/Semestre-2026%2F2-brightgreen.svg)]()
[![Linguagem](https://img.shields.io/badge/Linguagem-Kotlin%20%7C%20JavaScript-orange.svg)]()

Repositório oficial com o material didático, aulas, trabalhos práticos, servidores de testes e avaliações da disciplina de **Desenvolvimento de Software para Dispositivos Móveis**, ministrada na **Faculdade de Engenharia de Software** da **Universidade de Rio Verde (UniRV)**.

---

## 👨‍🏫 Informações Docentes

- **Professor:** Me. Sergio Souza Novak
- **Instituição:** Universidade de Rio Verde (UniRV)
- **Faculdade:** Engenharia de Software
- **Áreas de Atuação & Pesquisa:** Engenharia de Software, Ciência da Computação, Inteligência Artificial, Visão Computacional e IoT.

---

## 📌 Visão Geral da Disciplina

A disciplina abrange os conceitos essenciais e práticos para a construção de aplicações móveis modernas e robustas. O conteúdo programático orienta os alunos desde os fundamentos teóricos da arquitetura de hardware e sistemas operacionais móveis até o desenvolvimento prático utilizando **Kotlin** e a biblioteca moderna de UI **Android Jetpack / Jetpack Compose**, além de integração com APIs Backend.

### Principais Objetivos de Aprendizagem:
1. Compreender o funcionamento do hardware e arquitetura dos sistemas operacionais móveis (**Android** e **iOS**).
2. Dominar a linguagem de programação **Kotlin** e seus paradigmas.
3. Desenvolver interfaces declarativas e reativas utilizando **Android Jetpack Compose**.
4. Projetar e implementar aplicativos integrados a servidores Web e serviços de API REST.
5. Aplicar princípios de arquitetura de software, Clean Code e padrões de projeto em dispositivos móveis.

---

## 📁 Estrutura do Repositório

```text
DESENVOLVIMENTO DE SOFTWARE PARA DISPOSITIVOS MÓVEIS/
├── inicio/                       # Documentação inicial, plano de ensino e cronograma
│   ├── PLANO DE ENSINO - Modelo.docx
│   ├── CRONOGRAMA DE AULAS - Modelo.docx
│   └── capa.png
│
├── aulas/                        # Apresentações (LaTeX/Beamer) e listas de exercícios
│   ├── 1.Introdução/                                # Introdução à disciplina, POO e Clean Code
│   ├── 2. Noções de hardware de dispositivos móveis # Hardware, arquitetura Android/iOS
│   ├── 3. Introdução ao Kotlin/                      # Fundamentos e sintaxe do Kotlin
│   ├── 4.Criação do primeiro app Kotlin/            # Estrutura do app e ciclo de vida
│   └── 5.Primeiro Contato com Jet pack/             # Android Jetpack e UI Declarativa
│
├── projetos/                     # Serviços backend e projetos auxiliares
│   └── server/                   # Servidor Express.js mock para integração mobile (APIs REST)
│
├── enunciado trabalho da N2/     # Enunciados, especificações e protótipos de telas da N2
│   ├── enunciado.pdf / .tex
│   └── telas (HTML/PNG)
│
├── provas/                       # Provas, gabaritos, exercícios de revisão da N1
│   └── n1/                       # Arquivos de avaliação N1 e listas preparatórias
│
├── notas/                        # Planilhas de notas dos alunos (ignorado via .gitignore)
├── .gitignore                    # Regras de exclusão de arquivos no Git
└── README.md                     # Documentação geral do repositório
```

---

## 📚 Módulos e Conteúdo Programático

### 1. Introdução à Computação Móvel e Engenharia de Software
- Apresentação da disciplina e visão geral da trajetória profissional.
- Fundamentos de Orientação a Objetos, Clean Code e complexidade de algoritmos.
- Apresentação de listas introdutórias e alinhamento do plano de curso.

### 2. Hardware e Sistemas Operacionais Móveis
- **Hardware:** Processadores (arquiteturas ARM), gestão de memória RAM, armazenamento flash, sensores (GPS, acelerômetro, giroscópio) e gerenciamento de energia/bateria.
- **Sistemas Operacionais:** Arquitetura do Android (Linux Kernel, HAL, ART/Dalvik, Framework) vs. Arquitetura do iOS (Darwin, Core Services, Cocoa Touch).

### 3. Introdução à Linguagem Kotlin
- Sintaxe moderna, controle de nulos (*Null Safety*), inferência de tipos.
- Funções, lambdas, coleções, escopos (`let`, `apply`, `run`, `also`, `with`).
- Orientação a Objetos em Kotlin (data classes, sealed classes, interfaces, herança).

### 4. Criação do Primeiro Aplicativo Android
- Configuração do ambiente de desenvolvimento (**Android Studio** e SDK Android).
- Anatomia de um projeto Android (`AndroidManifest.xml`, `build.gradle.kts`, recursos `res/`).
- Ciclo de vida de *Activities* e componentes fundamentais.

### 5. Primeiro Contato com Android Jetpack & Compose
- Introdução ao paradigma de UI declarativa com **Jetpack Compose**.
- Componentes fundamentais (`Text`, `Button`, `Column`, `Row`, `LazyColumn`).
- Gerenciamento de Estado (`remember`, `mutableStateOf`, `StateHoisting`).

### 6. Projetos Backend & Integração (`projetos/server`)
- Servidor local construído em **Node.js + Express.js**.
- Fornece rotas JSON para testes de requisições HTTP (GET, POST, PUT, DELETE) para os aplicativos mobile desenvolvidos nas aulas.

### 7. Avaliações e Trabalhos Práticos
- **Provas N1:** Exercícios preparatórios, provas anteriores e revisões de conteúdo.
- **Trabalho N2:** Especificações completas com prototipagem de telas e requisitos de negócio para construção do aplicativo principal.

---

## 🛠️ Tecnologias e Ferramentas

| Categoria | Tecnologia / Ferramenta |
|---|---|
| **Linguagem Principal Mobile** | Kotlin |
| **Ambiente de Desenvolvimento** | Android Studio |
| **Interface de Usuário** | Android Jetpack Compose |
| **Backend Mock / API** | Node.js, Express.js, JSON |
| **Documentação & Aulas** | LaTeX (Beamer, TikZ) |
| **Controle de Versão** | Git / GitHub |

---

## 🚀 Como Executar os Projetos Locais

### Executando o Servidor Mock Backend (Node.js)

Para realizar testes de integração de rede a partir dos aplicativos mobile:

```bash
# Navegar até o diretório do servidor
cd projetos/server

# Instalar as dependências (caso não estejam instaladas)
npm install

# Iniciar o servidor de testes
npm start
# ou node server.js
```

### Compilando as Apresentações em LaTeX

Para visualizar ou editar os slides das aulas (`aulas/`):
1. Abra o arquivo `.tex` correspondente no **TeXstudio**, **VS Code** (com extensão LaTeX Workshop) ou **Overleaf**.
2. Utilize o compilador `pdfLaTeX` ou `LaTeXmk` para gerar o arquivo `.pdf`.

---

## 🔒 Privacidade e Segurança (`.gitignore`)

Por razões de privacidade e conformidade com a LGPD, a pasta `notas/` (contendo planilhas de notas e frequências) está incluída no arquivo `.gitignore` e **não é enviada para repositórios remotos**.

---

## 📄 Licença

Este material é de uso exclusivo didático e acadêmico no âmbito do curso de Engenharia de Software da **Universidade de Rio Verde (UniRV)**. Todos os direitos reservados aos respectivos autores.
# Disciplina-Desenvolvimento-Para-Dispositivos-Moveis
