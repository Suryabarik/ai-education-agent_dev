
from fastapi import FastAPI
from schemas.input_schema import ContentInput
from services.refinement import run_pipeline

app = FastAPI(title="AI Education Agent")

@app.post("/generate-content")
def generate_content(payload: ContentInput):
    result = run_pipeline(payload.grade, payload.topic)
    return result
