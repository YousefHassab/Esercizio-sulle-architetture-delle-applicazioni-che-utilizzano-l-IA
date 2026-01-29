import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="human_capital")

cv_data = [
    {"id": "veronesi", "text": "Dr. Alessandro Veronesi, Senior Research Scientist Milano. Esperto Spettroscopia IR, NMR, Python, MATLAB. 12 anni esperienza.", "meta": {"nome": "Alessandro Veronesi", "ruolo": "Senior Scientist"}},
    {"id": "neri", "text": "Sara Neri, Database Administrator. Esperta SQL, Big Data, PostgreSQL, Oracle. 10 anni esperienza bancaria.", "meta": {"nome": "Sara Neri", "ruolo": "DBA"}},
    {"id": "bruni", "text": "Paolo Bruni, AI Engineer. Specialista Machine Learning, PyTorch, LangChain. Modelli predittivi sanità.", "meta": {"nome": "Paolo Bruni", "ruolo": "AI Engineer"}},
    {"id": "rossi", "text": "Marco Rossi, Mobile App Developer. Flutter, Dart, Firebase, Swift. App food delivery.", "meta": {"nome": "Marco Rossi", "ruolo": "Developer"}},
    {"id": "gialdi", "text": "Giulia Gialdi, Master Node.js Backend. Microservizi, Pattern design, WebSockets.", "meta": {"nome": "Giulia Gialdi", "ruolo": "Backend Expert"}},
    {"id": "blu", "text": "Roberto Blu, Angular 17 Architecture. Signals, SSR, State Management NgRx.", "meta": {"nome": "Roberto Blu", "ruolo": "Frontend Architect"}}
]

for cv in cv_data:
    collection.add(
        documents=[cv["text"]],
        metadatas=[cv["meta"]],
        ids=[cv["id"]]
    )
print("✅ Database delle competenze creato con successo!")
