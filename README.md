# Python Cloud Functions - Sanic | EdgeOne Pages

A demonstration website showcasing how to deploy high-performance async Sanic applications as serverless functions on EdgeOne Pages.

## 🚀 Features

- **Sanic Framework**: One of the fastest Python async web frameworks
- **Native Async/Await**: Built from the ground up for asynchronous programming
- **Streaming Support**: Built-in response streaming capabilities
- **WebSocket Support**: Native WebSocket handling
- **Type-validated Routes**: Path parameter type validation

## 🛠️ Tech Stack

### Frontend
- **Next.js 15** - React full-stack framework
- **React 19** - User interface library
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS 4** - Utility-first CSS framework

### Backend
- **Sanic** - Async Python web framework
- **Cloud Functions** - EdgeOne Pages serverless functions

## 📁 Project Structure

```
python-sanic-template/
├── src/                    # Next.js frontend
├── cloud-functions/        # Python cloud functions
│   ├── api/
│   │   └── [[default]].py # Sanic application
│   └── requirements.txt   # Python dependencies
├── public/                # Static assets
└── package.json          # Project configuration
```

## 🚀 Quick Start

### Requirements

- Node.js 18+ 
- Python 3.9+
- EdgeOne CLI

### Install Dependencies

```bash
npm install
```

### Development Mode

```bash
edgeone pages dev
```

Visit [http://localhost:8088](http://localhost:8088) to view the application.

## 🎯 API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /api/ | Root endpoint |
| GET | /api/health | Health check |
| GET | /api/info | Function information |
| GET | /api/time | Current server time |
| GET/POST | /api/echo | Echo request info |
| POST | /api/json | Handle JSON body |
| GET | /api/users/{user_id} | Get user by ID |
| POST | /api/users | Create new user |
| GET | /api/search | Search with query params |

## 📚 Documentation

- **Sanic Documentation**: [https://sanic.dev](https://sanic.dev)
- **EdgeOne Pages Docs**: [https://pages.edgeone.ai/document/cloud-functions/python](https://pages.edgeone.ai/document/cloud-functions/python)

## Deploy

[![Deploy with EdgeOne Pages](https://cdnstatic.tencentcs.com/edgeone/pages/deploy.svg)](https://edgeone.ai/pages/new?from=github&template=python-sanic-template)

## 📄 License

This project is licensed under the MIT License.
