from app.services.job_service import JobService


class JobController:

    def get_all_jobs():
        return JobService.get_all_jobs()

    def get_job(id):
        return JobService.get_job(id)

    def save_job(data):
        return JobService.save_job(data)

    def update_job(id, data):
        return JobService.update_job(id, data)

    def delete_job(id):
        return JobService.delete_job(id)