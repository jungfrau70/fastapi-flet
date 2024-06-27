from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas, database
from data import generate_ohlc_data
from utils import calculate_ema

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/signup", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user(db, username=user.username)
    if not db_user or not crud.pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}

@app.get("/ohlc", response_model=schemas.OHLCResponse)
def get_ohlc():
    df = generate_ohlc_data()
    ohlc_data = df.to_dict(orient='records')
    return {"data": ohlc_data}

@app.get("/ema")
def get_ema(period: int):
    df = generate_ohlc_data()
    ema = calculate_ema(df, period)
    return ema.to_list()
