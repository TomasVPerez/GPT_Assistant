import openai
import os
import sys
import datetime

now = datetime.datetime.now()
dia_hora = now.strftime("%d/%m/%Y - %H:%M:%S")
prompt = ""
carpeta_log = os.path.expanduser("~/Proyectos/GPT/") #Cambiar carpeta Proyectos/GPT/ por la carpeta donde tengamos el script.

with open(f"{carpeta_log}/API_KEY.txt", "r") as file:
   API_KEY = file.read().strip() 

openai.api_key = API_KEY

def guardar_log(prompt, respuesta):
    with open(carpeta_log + "log.txt", "a") as file:
        if prompt ==  "salir":
            file.write(f"\n{'*' * 45}Conversacion finalizada ({dia_hora}){'*' * 45}\n")
            file.write("\n")
            sys.exit(0)
        else:
            file.write(f"{os.environ.get('USER')}: {prompt}\nGPT: {respuesta}\n")
        
while True:
    input_usuario = input(">")
    prompt = input_usuario
        # memoria_contexto.append({"role": "user", "content": prompt})
    response = openai.Completion.create(
            # model="gpt-3.5-turbo",
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.2,
        max_tokens=150,
        n=1,
        stop=None,
            # messages=memoria_contexto,
            # stream=True
    )
    respuesta = response.choices[0].text.strip()
    guardar_log(prompt, respuesta)
        # respuesta = response['choices'][0]
    print(respuesta)
        # memoria_contexto.append(respuesta)

