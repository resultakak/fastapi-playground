# FastAPI Playground

## Use

```bash
uvicorn main:app --reload
```

## API

```bash
GET /ping HTTP/1.1
Host: 127.0.0.1:8000
```

```json
{
  "message": "pong"
}
```

## Structure

```bash
.
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
└── main.py
```

## Links

- [Swagger UI - http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

- [openapi.json - http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)
