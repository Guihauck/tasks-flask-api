import pytest
import requests

#CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks = list()

def test_create_task():
  new_task_data = {
    "title": "Nova tarefa",
    "description": "Descrição da nova tarefa"
  }

  response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
  assert response.status_code == 200
  response_json = response.json()
  assert "message" in response_json
  assert "id" in response_json
  tasks.append(response_json['id'])

def test_read_get_task():
  response = requests.get(f"{BASE_URL}/tasks")
  assert response.status_code == 200
  response_json = response.json()
  assert "tasks" in response_json
  assert "total_tasks" in response_json

def test_read_get_tasks():
  if tasks:
    task_id = tasks[0]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert task_id == response_json['id']

def test_tasks_update():
  if tasks:
    task_id = tasks[0]
    payload = {
      "completed": True,
      "description": "A tarefa atualizada pelo teste automatizado.",
      "title": "Tarefa atualizada pelo teste"
    }
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
    response.status_code == 200
    response_json = response.json()
    assert "message" in response_json

# Nova requisição a tarefa específica.
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['title'] == payload['title']
    assert response_json['description'] == payload['description']
    assert response_json['completed'] == payload['completed']

def task_task_delete():
  if tasks:
    task_id = tasks[0]
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    response.status_code == 200
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 404
