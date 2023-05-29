from fastapi import FastAPI
import db
import models

app=FastAPI()

@app.get("/")
def root():
    return {"message":"Its Alive"}

@app.get("/all")
def get_all():
    data = db.all()
    return {"data":data}

@app.post("/create")
def create(data:models.Todo):
    id = db.create(data)
    return {"inserted":True,"inserted_id":id}

@app.get("/get/{name}") ## now name is passed in Path parameter and if we remove {name} - it will be query parameter
def get_one(name:str):
    data  =db.get_one(name)
    return {"data":data}

@app.delete("/delete")
def delete(name:str):
    data = db.delete(name)
    return {"deleted":True, "deleted_count":data}

@app.put("/update")
def update(name:str,data:models.Todo):
    data = models.Todo(name=data.name,description=data.description)
    data = db.update(name,data)

