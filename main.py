from fastapi import FastAPI
app=FastAPI()
@app.get("/calculator")
def numbers(a:int,b:int):
    result1=a+b
    result2=a-b
    result3=a*b
    result4=a/b
    return {"a": a, "b": b, "addition": result1, "subtraction": result2, "multiplication": result3, "division": result4}
