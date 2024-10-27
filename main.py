from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(
    request: Request,
    operation: str = Form(...),
    num1: float = Form(...),
    num2: float = Form(...),
):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        result = "Invalid operation"
    
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

