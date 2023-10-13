from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import pandas

class LoginFormulario(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log in")

class RegistroFormulario(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Registrar")

#Conversion de la base de datos instrumentos a listas para renderizarla:

app = Flask(__name__)
app.secret_key = "clave-secreta"

@app.route("/")
def home():
    return render_template('index.html')


        

@app.route("/login", methods=["GET","POST"])
def login():
    formulario_login = LoginFormulario()
    if formulario_login.validate_on_submit():
        archivo = pandas.read_csv("Usuarios.csv")
        lista_de_usuarios = archivo["Usuario"].to_list()
        lista_de_contraseñas = archivo["Contraseña"].to_list()  
        datos = pandas.read_csv("Instrumentos.csv")
        lista_instrumentos = datos["Instrumentos"].to_list()
        lista_colores = datos["Color/es"].to_list()
        lista_stock = datos["Stock"].to_list()
        lista_disponible = datos["Disponible"].to_list()
        lista_de_listas = [lista_instrumentos,lista_colores,lista_stock,lista_disponible]
        if formulario_login.email.data in lista_de_usuarios and formulario_login.password.data in lista_de_contraseñas:
            nombre_de_bienvenida=formulario_login.email.data
            
                
            return render_template("index2.html", nombre=nombre_de_bienvenida,lista_de_data=lista_de_listas)

            
        else:
            return render_template("error.html")
            
    return render_template('login.html', form=formulario_login)

@app.route("/registro", methods=["GET","POST"])
def register():
    formulario_registro = RegistroFormulario()
    if formulario_registro.validate_on_submit():
        
        usuario = formulario_registro.email.data
        contraseña = formulario_registro.password.data
        bd = pandas.DataFrame({"Usuario":[usuario],
                               "Contraseña":[contraseña]
                       })  
        bd.to_csv("Usuarios.csv",mode="a", header=False)
        
      
        return render_template("exito.html")
            
    
    return render_template('registro.html', rform=formulario_registro)
            
    

if __name__ == '__main__':
    app.run(debug=True)
    
#https://wtforms.readthedocs.io/en/3.0.x/
#https://jinja.palletsprojects.com/en/3.1.x/
#https://flask.palletsprojects.com/en/2.3.x/