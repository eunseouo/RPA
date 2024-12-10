from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
 
@app.get("/item")
def read_item(item_id: int, name: str = None, age: int = 0):
    return {"item_id": item_id, "name": name, "age": age}


@app.post("/plus")
async def plus_form(num1: int = Form(...), num2: int = Form(...),num3: int = Form(...), num4: int = Form(...)):
    result = num1 + num2
    result2 = num3 + num4
    return {"msg": f"{num1} + {num2} = {result} | {num3} + {num4} = {result2}"}
  

app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")
