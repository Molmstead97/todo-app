from fastapi import FastAPI, Depends, HTTPException
import models 
import schemas
import crud

from database import SessionLocal, engine

from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

todos: list[schemas.Todo] = []

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_model=list[schemas.Todo])
async def get_todos(db: Session = Depends(get_db)) -> list[schemas.Todo]:
    return crud.get_todos(db)

@app.post("/", response_model=schemas.Todo)
async def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)) -> schemas.Todo:
    return crud.create_todo(db=db, todo=todo)