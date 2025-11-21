from fastapi import FastAPI, HTTPException
import os
from .storage import Storage
from .recommender import Recommender
from .schemas import UserCreate, ItemCreate, RatingCreate


app = FastAPI(title="🎓 Recommender — FastAPI")


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')


storage = Storage(data_dir=DATA_DIR)
recomm = Recommender(storage)


@app.on_event("startup")
def startup_event():
    storage.ensure_data()
    recomm.load_data()


@app.get('/')
def root():
    return {"status": "ok"}


@app.post('/users', status_code=201)
def create_user(user: UserCreate):
    user_id = storage.add_user(user.dict())
    return {"user_id": user_id}


@app.post('/items', status_code=201)
def create_item(item: ItemCreate):
    item_id = storage.add_item(item.dict())
    return {"item_id": item_id}


@app.put('/ratings', status_code=200)
def add_or_update_rating(rating: RatingCreate):
    storage.add_rating(rating.user_id, rating.item_id, rating.rating)
    recomm.load_data()
    return {"status": "ok"}


@app.get('/recommendations/{user_id}')
def get_recommendations(user_id: int, n: int = 10):
    if not storage.user_exists(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    recs = recomm.recommend(user_id, n)
    return {"user_id": user_id, "recommendations": recs}