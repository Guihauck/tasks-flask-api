# CRUD: Create, Read, Update and Delete - > Criar, Ler, Atualizar, Deletar.
from flask import Flask, request, jsonify
from model.tasks import Task

app = Flask(__name__) 

tasks = list()
tasks_id_control = 1

@app.route("/tasks", methods=['POST']) # Traçando rota método POST.
def create_task():
  global tasks_id_control
  data = request.get_json()
  new_tasks = Task(id=tasks_id_control, title=data['title'], description=data.get("description"))
  tasks_id_control += 1
  tasks.append(new_tasks)
  print(tasks, data)
  return jsonify({"Mensagem": "Nova Tarefa Criada"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = []
    for task in tasks:
       task_list.append(task.to_dict()) # Adicionado o formato dicionário.
    output = {
          "tasks": task_list,
          "total_tasks": len(task_list) # Contagem dos elementos na lista.
        }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  for t in tasks:
   if t.id == id:
      return jsonify(t.to_dict())
   
  return jsonify({"message": "Não foi possível carregar a atividade."}), 404

@app.route("/tasks/<int:id>", methods=['PUT'])
def update_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t
    
  if task == None:
    return jsonify({"message:" "Tarefa não existe para este identificador."}), 404
  
  data = request.get_json()
  task.title = data['title']
  task.description = data['description']
  task.completed = data['completed']

  return jsonify({"message": "Tarefa atualizada com sucesso."})

if __name__ == "__main__":
  app.run(debug=True) #Habilitação de logs.  