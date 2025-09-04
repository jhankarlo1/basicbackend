from fastapi import FastAPI

app = FastAPI()

patients = []  # temporary in-memory storage

@app.get("/")
def read_root():
    return {"message": "App Backend Running"}

@app.post("/patients")
def add_patient(name: str):
    patient = {"patient id": len(patients)+1, "patient name": name, "status": "pre-operation"}
    patients.append(patient)
    return patient

@app.get("/patients")
def get_patients():
    return patients
