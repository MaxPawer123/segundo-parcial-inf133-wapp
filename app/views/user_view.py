# render_template() es una función de Flask
# que renderiza un template de Jinja2.
from flask import render_template


# La función `usuarios` recibe una lista de
# usuarios y renderiza el template `usuarios.html`
def patient(users):
    return render_template("patient.html", users=users, title="Lista de pacientes")


# La función `registro` renderiza el
# template `registro.html`
def registro():
    return render_template("register.html", title="Registro de usuarios")


# La función `actualizar` recibe un usuario
# y renderiza el template 


# La función `login` renderiza el template `login.html`
def login():
    return render_template("login.html", title="Inicio de sesión")

