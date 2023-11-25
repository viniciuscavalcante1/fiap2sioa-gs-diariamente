"""
Módulo para execução do FastAPI.

Para iniciar o aplicativo, execute este módulo diretamente. Exemplo:
    ```
    uvicorn server.app:app --host 0.0.0.0 --port 8000 --reload
    ```

"""
import uvicorn

if __name__ == "__main__":
    # Inicia o servidor Uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)