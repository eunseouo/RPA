from fastapi import FastAPI, Form, File, UploadFile 
import shutil
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
import qrcode
from io import BytesIO

# FastAPI 객체 정의
app = FastAPI()

def loginDB(userId, userPassword):
    import sqlite3

    conn = sqlite3.connect('education.db')
    cursor = conn.cursor()
    
    query = 'SELECT * FROM user WHERE userId = ? AND userPassword = ?'
    cursor.execute(query, (userId, userPassword))
    result = cursor.fetchone()
    conn.close()
 
    if result:
        print("Login successful!")
        print("User Info:", result)  # 쿼리 결과 출력
        return True
    else:
        print("Login failed. Invalid username or password.")
        return False

@app.post("/login")
def login_form(userid: str = Form(...), userpassword: str = Form(...)):
    result = loginDB(userid, userpassword)
 
    if result == True:
        return {"msg": f"{userid}님 반갑습니다."}
    else:
        return {"msg": "로그인에 실패했습니다"}

from fastapi.staticfiles import StaticFiles
import qrcode.constants

@app.get("/files/{filename}")
async def get_file(filename: str):
    file_path = Path("static/uploads") / filename

    if file_path.is_file():
        return FileResponse(path=file_path, filename=filename)
    else:
        raise HTTPException(status_code=404, detail="File not found")


app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")
