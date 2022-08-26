from app import app

@app.get("/")
def home():
    return "home route"

@app.get("/jobs")
def get_all_jobs():
    return "get all jobs"

@app.post("/jobs/new")
def save_job():
    return "job save"

@app.get("/job/<string:id>")
def get_job(id):
    return f"get job {id}"


@app.put("/job/<string:id>/edit")
def edit_job(id):
    return f"edit job {id}"

@app.delete("/job/<string:id>/delete")
def delete_job(id):
    return f"delete job {id}"