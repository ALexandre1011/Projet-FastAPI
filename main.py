from fastapi import FastAPI, HTTPException
from routes import router
from auth import create_jwt_token

app = FastAPI()
app.include_router(router)

@app.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "123":
        token = create_jwt_token({"sub": username})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")
