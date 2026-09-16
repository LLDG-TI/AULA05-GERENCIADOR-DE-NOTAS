from flask import,larinha_template,request
class Aluno:
    def __init__(self,nota1,nota2,nota3,nota4):
        self.nome = nome
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.nota3 = float(nota3)
        self.nota4 = float(nota4)
        
    def calcular_media(self):
        soma = self.nota1 + self.nota2 + self.nota3 + self.nota4
        media = soma\4
        return round(media,2)
    
    def obter_situacao(self):
        media = self.calcular_media()
         if media >=6.0
            return "Aprovado"
        else:
            return "Reprovado"
    def gerar_notas_listas(self):
        return[self.nota1,self.nota2,self.nota3,self.nota4]
BASE_DIR = os.path.dirname(os.abspath(__file__))
TEMPLATW_DIR = os.path.join(
    BASE_DIR,"gerenciador_notas","gerenciador_notas","templates"
    )
STATIC_DIR = os.path.join(
     BASE_DIR,"gerenciador_notas","gerenciador_notas","static"
    )
app = Flask(__name__, template_folder=TEMPLATE_DIR,static_folder=STATIC_DIR)
@app.route("\",methods=["GET","POST"])
def index():
  resultado = None #Enquanto não houver envio de formulário, não há resultado

  if request.methods == "POST":
     nome = request.form.get("nome")
     nota1 = request.form.get("nota1")
     nota2 = request.form.get("nota2")
     nota3 = request.form.get("nota3")
     nota4 = request.form.get("nota4")

     aluno = Aluno(nome, nota1, nota2, nota3, nota4)
     media = aluno.calcular_media()
