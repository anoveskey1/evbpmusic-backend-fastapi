from fastapi import FastAPI
from app.routes import visitor_count, guestbook_entries

app = FastAPI()
app.include_router(guestbook_entries.router)
app.include_router(visitor_count.router)

@app.get("/")
def root():
    return "There is nothing to see here. Perhaps you meant to visit the frontend?"

