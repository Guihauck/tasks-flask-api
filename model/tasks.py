class Task:
  def __init__(self, id, title, description, completed=False):
    self.id = id
    self.title = title
    self.description = description
    self.completed = completed # Definição dos atributos utilizando self.

  def to_dict(self): # Método que retorna um dicionário com os atributos
    return {
      "id": self.id,
      "title": self.title,
      "description": self.description,
      "completed": self.completed
    }
    