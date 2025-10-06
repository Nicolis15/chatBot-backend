from  backend.Model.customLLM import CustomLLM
from groq import Groq
import os

class ModelImplementation:
    @classmethod
    def runModel(cls, message: str):

        contexto = CustomLLM.context(message)

        prompt = f"""
        Eres Nicolas Lis Cruz, Desarrollador de Software e Ingeniero de datos, responde en primera persona.
        Usa el siguiente contexto para responder de manera personalizada, hazlo con buena redaccion, sin errores de ortografia:

        Contexto:
        {contexto}

        Pregunta:
        {message}
        """


        client = Groq(api_key=os.environ.get("VITE_GROQ_API_KEY"))


        chat_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )

        return chat_completion.choices[0].message.content


