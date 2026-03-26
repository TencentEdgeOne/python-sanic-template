"""
Python Cloud Function - Sanic Framework
A high-performance async serverless function using Sanic web framework.
"""
from sanic import Sanic
from sanic.response import json as sanic_json
from sanic.exceptions import NotFound, SanicException
import time
import datetime

app = Sanic("SanicCloudFunction")


@app.get("/")
async def index(request):
    """Root endpoint."""
    return sanic_json({
        "message": "Hello from Sanic Cloud Function!",
        "framework": "Sanic",
        "timestamp": time.time()
    })


@app.get("/health")
async def health(request):
    """Health check endpoint."""
    return sanic_json({
        "status": "healthy",
        "timestamp": time.time(),
        "type": "sanic_function"
    })


@app.get("/info")
async def info(request):
    """Function information endpoint."""
    return sanic_json({
        "name": "Sanic Cloud Function",
        "framework": "Sanic",
        "description": "A high-performance async serverless function using Sanic web framework",
        "features": [
            "Async/await native",
            "High performance",
            "Built-in streaming",
            "WebSocket support",
            "Class-based views"
        ]
    })


@app.get("/time")
async def get_time(request):
    """Return current server time."""
    now = datetime.datetime.now()
    return sanic_json({
        "timestamp": time.time(),
        "iso": now.isoformat(),
        "formatted": now.strftime("%Y-%m-%d %H:%M:%S"),
    })


@app.route("/echo", methods=["GET", "POST"])
async def echo(request):
    """Echo request information."""
    body = request.body.decode('utf-8') if request.body else None
    return sanic_json({
        "method": request.method,
        "query": dict(request.args),
        "headers_count": len(dict(request.headers)),
        "body": body[:500] if body else None,
        "timestamp": time.time()
    })


@app.post("/json")
async def handle_json(request):
    """Handle JSON request body."""
    try:
        data = request.json or {}
    except Exception:
        return sanic_json({"error": "Invalid JSON body"}, status=400)
    
    return sanic_json({
        "message": "JSON received and parsed",
        "received": data,
        "keys": list(data.keys()) if isinstance(data, dict) else [],
        "size": len(request.body) if request.body else 0
    })


@app.get("/users/<user_id:int>")
async def get_user(request, user_id: int):
    """Get user by ID with type-validated path parameter."""
    if user_id < 0:
        return sanic_json({"error": "Invalid user ID"}, status=400)
    
    return sanic_json({
        "user_id": user_id,
        "username": f"user_{user_id}",
        "email": f"user{user_id}@example.com",
        "source": "sanic_function"
    })


@app.post("/users")
async def create_user(request):
    """Create a new user."""
    try:
        data = request.json or {}
    except Exception:
        return sanic_json({"error": "Invalid JSON body"}, status=400)
    
    if 'username' not in data:
        return sanic_json({"error": "Username is required"}, status=400)
    
    return sanic_json({
        "message": "User created",
        "user": {
            "id": 12345,
            "username": data['username'],
            "email": data.get('email', ''),
        }
    }, status=201)


@app.get("/search")
async def search(request):
    """Search functionality with query parameters."""
    q = request.args.get('q', '')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))
    
    if not q:
        return sanic_json({"error": "Query parameter 'q' is required"}, status=400)
    
    results = [
        {"id": i, "name": f"Result {i}", "score": round(0.95 - i * 0.08, 2)}
        for i in range(offset, offset + min(limit, 10))
    ]
    
    return sanic_json({
        "query": q,
        "limit": limit,
        "offset": offset,
        "count": len(results),
        "results": results
    })


# Exception handlers
@app.exception(NotFound)
async def not_found_handler(request, exception):
    return sanic_json({"error": "Not Found"}, status=404)


@app.exception(SanicException)
async def server_error_handler(request, exception):
    return sanic_json({"error": str(exception)}, status=exception.status_code)
