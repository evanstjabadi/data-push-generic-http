from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


@app.post("/v1/issues/")
def process_issues(issue_message: dict) -> dict:
    for key, value in issue_message.items():
        print(f"{key} : {value}")
    # save issue to DB
    return {"message": "Issue processed"}


@app.post("/v1/test-results/")
def process_test_results(test_result_message: dict) -> dict:
    for key, value in test_result_message.items():
        print(f"{key} : {value}")
    # save test result to DB
    return {"message": "Test result processed"}
