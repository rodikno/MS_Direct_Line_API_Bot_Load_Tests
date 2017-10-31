from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        self.client.post("/api/v1/auth", {"appID":"APP_ID", "password":"123"})

    @task(1)
    def index(self):
        self.client.get("/api/v1/language")


class NLPAPIUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000