from flask import Flask
# Repasse da variável name tendo o valor main. Sendo executada de forma manual e não importada por outro arquivo.

app = Flask(__name__) 

# Criação de rota, criando comunicação de recebimento e devolução de informações com o método route.

@app.route("/")
def hello_world():
  return "Hello world!"

@app.route("/about")
def about():
  return "Página sobre!"

# Vai permitir que toda vez quando a rota '/' for acessada a função será executada.

# Validação da execução manual do servidor local.
if __name__ == "__main__":
  app.run(debug=True) #Habilitação de logs. 