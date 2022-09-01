from app.services.job_service import JobService


class JobController:

    def get_all_jobs(user_id):
        return JobService.get_all_jobs(user_id)

    def get_job(user_id, job_id):
        return JobService.get_job(user_id, job_id)

    def save_job(user_id, data):
        return JobService.save_job(user_id, data)

    def update_job(user_id, id, data):
        return JobService.update_job(user_id, id, data)

    def delete_job(user_id, id):
        return JobService.delete_job(user_id, id)