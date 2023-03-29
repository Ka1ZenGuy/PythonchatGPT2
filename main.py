import openai
import config

openai.api_key = config.api_key

# Contexto para darle al asistente
messages = [{"role": "system", "content": "Eres un Cocinero de talla Mundial"}]

while True:
    content = input("¿Sobre qué quieres hablar? ")

    if content == "nada":
    break

    messages.append({"role": "user", "content": content})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages= messages)
    response_content = response.choices.message.content

    messages.append({"role": "assistant" , "content": response_content})
    
print(response_content)
