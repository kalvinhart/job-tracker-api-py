from app.services.job_service import JobService


class JobController:

    def get_all_jobs():
        return JobService.get_all_jobs()

    def get_job(id):
        return JobService.get_job(id)

    def saveJob(data):
        return JobService.save_job(data)

    def updateJob(job):
        pass

    def deleteJob(id):
        pass