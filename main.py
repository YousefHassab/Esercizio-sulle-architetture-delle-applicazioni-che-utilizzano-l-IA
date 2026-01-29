from core.planner import Planner

def main():
    # Scegli False per Ollama locale, True se hai configurato OpenAI
    orchestrator = Planner(use_cloud=False) 
    
    domanda = "Dobbiamo sviluppare un'app mobile per monitorare i dati spettroscopici dei laboratori. Chi dovremmo mettere nel team per risparmiare tempo e soldi?"
    
    print(f"--- RICHIESTA PROGETTO ---")
    print(domanda)
    
    risposta = orchestrator.process_request(domanda)
    
    print(f"\n--- PROPOSTA TEAM DALL'AI ---")
    print(risposta)

if __name__ == "__main__":
    main()
