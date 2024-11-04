import uvicorn

def main():
    uvicorn.run("app:app", port=8050, reload=True)

if __name__ == "__main__":
    main()
