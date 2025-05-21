from fastapi import APIRouter
from openai import OpenAI, completions
from interfaces.chatinterfaces import ChatCompletionResponse, InputMessage

router = APIRouter()

import os
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url='https://openrouter.ai/api/v1')
##client = OpenAI(api_key='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',
                ##base_url='https://openrouter.ai/api/v1')

@router.post("/ai-chat")
def aiChat(data: InputMessage):
    data = data.model_dump()
    print("message: " + data["message"])
    message = "Por favor responde de manera concreta, clara y siempre en castellano"

    try:
        completion: ChatCompletionResponse = client.chat.completions.create(
            model="google/gemma-3-1b-it:free",
            messages=[
                {"role": "system", "content": "Eres un asistente que siempre responde en castellano, de forma clara y breve"},
                {"role": "user", "content": f"{message}. Responde a esta pregunta: {data['message']}"}
            ]
        )
        response_text = completion.choices[0].message.content
        print("response: " + response_text)
        return {"response": response_text}

    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}

@router.post("/ai-chat2")
def aiChat2(data: InputMessage):  # nombre único
    data = data.model_dump()
    print("message: " + data["message"])
    message = "Por favor responde de manera concreta, clara y siempre en castellano"

    try:
        completion: ChatCompletionResponse = client.chat.completions.create(
            model="deepseek/deepseek-prover-v2:free",
            messages=[
                {"role": "system", "content": "Eres un asistente que siempre responde en castellano, de forma clara y breve"},
                {"role": "user", "content": f"{message}. Responde a esta pregunta: {data['message']}"}
            ]
        )
        response_text = completion.choices[0].message.content
        print("response: " + response_text)
        return {"response": response_text}

    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}
