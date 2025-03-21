# CRUD API com Flask

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0-black?style=for-the-badge&logo=flask)
![JSON](https://img.shields.io/badge/JSON-Data-orange?style=for-the-badge&logo=json)

## Sobre o projeto
Este projeto consiste em uma API simples de CRUD (Create, Read, Update, Delete) utilizando Flask.

## Tecnologias Utilizadas
- ![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
- ![Flask](https://img.shields.io/badge/Flask-2.0-black?style=flat-square&logo=flask)
- ![JSON](https://img.shields.io/badge/JSON-Data-orange?style=flat-square&logo=json)

## Instalação
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/Guihauck/tasks-flask-api)
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Executando o projeto
```bash
python app.py
```

## Endpoints

### Criar uma nova tarefa
`POST /tasks`
```json
{
  "title": "Nova Tarefa",
  "description": "Descrição da tarefa"
}
```

### Listar todas as tarefas
`GET /tasks`

### Obter uma tarefa específica
`GET /tasks/{id}`

### Atualizar uma tarefa
`PUT /tasks/{id}`
```json
{
  "title": "Tarefa Atualizada",
  "description": "Descrição atualizada",
  "completed": true
}
```

### Deletar uma tarefa
`DELETE /tasks/{id}`

## Autor
Feito por [Guilherme Hauck][([https://github.com/seu-usuario](https://github.com/Guihauck)).](https://github.com/Guihauck)
