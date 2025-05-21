from openai import OpenAI

client = OpenAI(api_key='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',
                 base_url='https://openrouter.ai/api/v1')
message = input("Cuál es tu pregunta: ")
prompt = (
    "Por favor responde de manera clara y sin símbolos innecesarios."
    "Evita usar otros idiomas que no sean el castellano y escribe y una respuesta concisa." \
    f"Pregunta del usuario: {message}"
)

completion = client.chat.completions.create(
    model = 
 "cognitivecomputations/dolphin3.0-r1-mistral-24b:free",    messages = [
        {
            "role":"user",
            "content":prompt
        }
    ]
)
print(completion.choices[0].message.content)
