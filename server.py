from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from app import app as flask_app
import uvicorn

def run():
    app = Starlette(
        routes=[
            Route('/', lambda _: JSONResponse({'message': 'Hello, World!'})),
            Route('/api/echo', lambda request: JSONResponse(request.json())),
            Route('/', flask_app)
        ]
    )
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))

if __name__ == '__main__':
    run()
