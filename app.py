# CRUD: Create, Read, Update and Delete - > Criar, Ler, Atualizar, Deletar
from flask import Flask, request, jsonify
from model.tasks import Task

app = Flask(__name__) 

tasks = list()
tasks_id_control = 1

@app.route("/tasks", methods=['POST']) # Traçando rota método POST
def create_task():
  global tasks_id_control
  data = request.get_json()
  new_tasks = Task(id=tasks_id_control, title=data['title'], description=data.get("description"))
  tasks_id_control += 1
  tasks.append(new_tasks)
  print(tasks, data)
  return jsonify({"Mensagem": "Nova Tarefa Criada"})

@app.route("/tasks", methods=['GET'])
def get_task():
    task_list = []
    for task in tasks:
       task_list.append(task.to_dict()) # Adicionado o formato dicionário.
    output = {
          "tasks": task_list,
          "total_tasks": 0
        }
    return jsonify(output)

if __name__ == "__main__":
  app.run(debug=True) #Habilitação de logs. 