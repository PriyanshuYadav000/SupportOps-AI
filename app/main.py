from fastapi import FastAPI

app = FastAPI(
    title="SupportOps AI",
    description="AI-powered customer support assistant",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "supportops-ai",
        "version": "0.1.0",
    }
