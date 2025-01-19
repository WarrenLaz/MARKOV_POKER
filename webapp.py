from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    string_ = "helloworld"
    html_content = f"""
    <!DOCTYPE html>
    <html> 
    <head>
        <title>FastAPI App</title>
    </head>
    <body>
        <h1>{string_}</h1>
        <p>Welcome to your FastAPI app.</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
