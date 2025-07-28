from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "guestbook_entries.json"

@router.get("/api/guestbook-entries")
def get_guestbook_entries():
    with open(DATA_PATH, 'r') as file:
        data = json.load(file)

    if not data:
        return {
            "code": "DATA_UNAVAILABLE",
            "message": "No guestbook entries found."
            }
    else:
        return data