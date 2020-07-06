from fastapi import FastAPI


from fastapi import FastAPI


app = FastAPI()


TAREFAS = []


@app.get("/tarefas")
def listar():
    return TAREFAS