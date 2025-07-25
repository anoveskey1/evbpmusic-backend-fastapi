from fastapi import APIRouter

router = APIRouter()

visitor_count = 0

@router.get("/api/visitor-count")
def get_visitor_count():
    global visitor_count
    visitor_count += 1
    return { "count": visitor_count }