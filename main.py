from fastapi import FastAPI
import todos

app = FastAPI(
    title="TodoAPI",
    description="Une API REST simple pour gérer des todos — projet fil rouge formation Git & GitHub",
    version="0.1.0",
)

# Enregistrement des routers
app.include_router(todos.router)


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}