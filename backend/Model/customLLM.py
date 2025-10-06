import json
import chromadb
import os

class CustomLLM:
    _client = chromadb.Client()
    _collection = None

    @classmethod
    def _load_collection(cls):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "info.json")

        if cls._collection is None:
            cls._collection = cls._client.get_or_create_collection("perfil_usuario")


            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            documento = json.dumps(data, ensure_ascii=False)


            if len(cls._collection.get()["ids"]) == 0:
                cls._collection.add(documents=[documento], ids=["usuario"])

        return cls._collection

    @classmethod
    def context(cls, pregunta: str) -> str:
        collection = cls._load_collection()

        contexto = collection.query(query_texts=[pregunta], n_results=3)
        documentos = contexto["documents"][0]

        return ". ".join(documentos)
