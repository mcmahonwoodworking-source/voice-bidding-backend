from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any, List
import os

from .models import CreateJobIn, StepHoursIn, MaterialIn, MaterialOut, NoteIn, JobOut, CompileOut
from . import storage
from .proposal import load_critical_paths, render_proposal, render_internal_summary

app = FastAPI(title="Voice Bidding Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE = os.path.dirname(os.path.dirname(__file__))
CRIT = load_critical_paths()

def get_label_and_rate(job_type: str, step_key: str):
    steps = CRIT[job_type]["steps"]
    for s in steps:
        if s["key"] == step_key:
            return s["label"], s["rate"]
    return step_key, 120

def calc_board_feet(thickness_quarters: int, width_in: float, length_ft: float) -> float:
    # BF = (T(in) * W(in) * L(ft)) / 12
    t_in = thickness_quarters / 4.0
    return (t_in * width_in * length_ft) / 12.0

# root
@app.get("/")
def root():
    return {"ok": True, "service": "voice-bidding-backend"}

# (leave the rest of your routes here unchanged)
