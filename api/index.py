from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_methods=["POST", "GET", "OPTIONS"],
allow_headers=["Content-Type", "Authorization"],
expose_headers=["Access-Control-Allow-Origin"],
)

from pathlib import Path
import pandas as pd

CSV_FILE = Path(__file__).resolve().parent.parent / "q-fastapi.csv"
df = pd.read_csv(CSV_FILE)

@app.get("/api")
def get_students(class_: list[str] | None = Query(None, alias="class")):
    data = df

    if class_:
        data = df[df["class"].isin(class_)]

    return {
        "students": data.to_dict(orient="records")
    }
