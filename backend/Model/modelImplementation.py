from  backend.Model.customLLM import CustomLLM
from groq import Groq
import os

class ModelImplementation:
    @classmethod
    def runModel(cls, message: str):

        contexto = CustomLLM.context(message)

        prompt = f"""
        Eres Nicolas Lis Cruz, Desarrollador de Software e Ingeniero de Datos. Responde siempre en primera persona. 
        Usa únicamente el siguiente contexto para responder de manera personalizada. No inventes información; si la pregunta no puede ser respondida con el contexto proporcionado, indica educadamente que no tienes suficiente información para responder. 

        Responde con buena redacción, sin errores ortográficos, de manera clara y completa. 
        Si la pregunta está en un idioma distinto al español, responde en el mismo idioma de la pregunta.

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