import os
import chromadb
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

class Planner:
    def __init__(self):
        # 1. Connessione al Vector DB (Invariata)
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_collection(name="human_capital")
        
        # 2. Inizializzazione Groq (Velocità estrema)
        self.llm = ChatGroq(
            model_name="llama-3.3-70b-versatile",
            temperature=0
        )
        print("[System] Connesso a Groq LPU - Velocità Massima Attivata")

    def process_request(self, user_input):
        print(f"\n[AI Planner] Groq sta analizzando il database...")
        
        # Recupero semantico dal DB
        results = self.collection.query(query_texts=[user_input], n_results=2)
        contesto = results['documents'][0][0]
        
        prompt = f"""
        Sei il Manager HR di una multinazionale. 
        Dato questo profilo dipendente: {contesto}
        Rispondi alla sfida dell'utente: {user_input}
        
        Sii sintetico, professionale e indica chiaramente il risparmio economico.
        """
        
        return self.llm.invoke(prompt).content
