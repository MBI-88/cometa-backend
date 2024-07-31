from fastapi import FastAPI
from app.controllers.input.controllers import router


app = FastAPI(
         title="Api cometa",
        description="Api for test",
        version="1.0"
    )
app.include_router(router, prefix="/api")



if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
   
   