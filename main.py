"""Main Entry point for the FastAPI app."""
import uvicorn


def main():
    """Run the FastAPI app using Uvicorn."""
    uvicorn.run("app:app", port=8050, reload=True)


if __name__ == "__main__":
    main()
