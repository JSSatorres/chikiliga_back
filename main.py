
from fastapi import FastAPI
import uvicorn
import os
from api.routes import router


app = FastAPI()

app.include_router(router)

# port = int(os.getenv("PORT", 10000)) 

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    
    
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=port)    