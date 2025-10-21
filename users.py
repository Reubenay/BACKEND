from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import uvicorn
import bcrypt

load_dotenv()

app = FastAPI(title="simple App", version="1.0.0")

class Simple(BaseModel):
    name: str = Field(...,  example="sam larry")
    email: str = Field(...,  example="@sample.com")
    password: str = Field(...,  example="sam123")

@app.post("/signup")
def signUp(input: Simple):
    try:
        query = text("""
                     INSERT INTO users (name, email, pasword)
                     VALUES(:name, :email, :password)

        """)


        
        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw(input.password.encode('utf-8'), salt)
        print(hashedPassword)

        db.execute(query, {"name": input.name, "email": input.email, "password": hashedPassword})
        db.commit()

        return{
            "message": "user created Successsfully",
            "data": {"name": input.name, "email": input.email}
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=e)