from flask import Flask, request
from pypdf import PdfReader
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)


@app.route("/")
def index():
    return "<div><h1>Prueba Tecnica Rocketbot</h1><p>Lectura de PDF yEnvio de email con Python</p></div>"


@app.route("/sendmail", methods=["POST"])
def receive_file():
    archivo = request.files["archivo"]
    email = request.form["email"]
    texto_a_enviar = read_file(archivo)
    sendEmail(email, texto_a_enviar)

    return {
        "success": True,
        "message": "The email has been successfully sent to " + email,
    }


def read_file(archivo):
    leer_archivo = PdfReader(archivo)
    numero_de_paginas = len(leer_archivo.pages)
    pagina1 = leer_archivo.pages[0]
    texto = pagina1.extract_text().split("\n")
    primeras_30_lineas = texto[:30]
    return primeras_30_lineas


def sendEmail(email, lista):
    linea = " ".join(lista)
    cuerpo_mensaje = linea.replace(" . ", ".\n")

    # Configurar el servidor SMTP
    servidor_smtp = "smtp.gmail.com"
    puerto_smtp = 587
    # Configurar el inicio de sesión SMTP
    nombre_usuario = "bernatattoo@gmail.com"
    contrasena = "wolf xiei bydj helq"

    # Crear una conexión SMTP
    with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:

        servidor.starttls()
        # Iniciar sesión en el servidor SMTP
        servidor.login(nombre_usuario, contrasena)

        mensaje = MIMEMultipart()
        mensaje["Subject"] = "Prueba Tecnica Rocketbot..."
        mensaje.attach(MIMEText(cuerpo_mensaje))

        # Enviar el mensaje
        servidor.sendmail(nombre_usuario, email, mensaje.as_string())


if __name__ == "__main__":
    app.run()
