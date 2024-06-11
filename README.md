# Prueba Tecnica Rocketbot

## Python

## Requirements:

- Develop a RESTful API using Node or Python
- The API should include the following functionalities:
  - Receive a PDF file.
  - Extract the first 30 lines of the PDF.
  - Send an email with the extracted content to the provided email address.

### Entorno Virtual e instalacion de librerias

- Crear el entorno virtual
- instalar las librerias necesarias

### Levantar el proyecto

    $ pip install -r requirements.txt

    $ flask --app app run

### Endpoint POST

http://127.0.0.1:5000/sendmail
http://localhost:5000/sendmail

### Observaciones

tanto la cuenta de email, como la contraseña de aplicacion por el momento estan funcional para pruebas, fueron creadas solo para este ejercicio.
