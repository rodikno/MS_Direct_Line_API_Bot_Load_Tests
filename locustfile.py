from locust import HttpLocust, TaskSet, task
from locust import events


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        print('Load test started')

    @task(1)
    def index(self):
        expected_content = b'{"original_message": "Hello I\'m a bit confused", "messages": ["[QnA bot] says:\\nCould you rephrase or clarify your question for better understanding?"], "length": "1"}'
        with self.client.post("/ask_bot", {"message": "Hello I'm a bit confused"}) as response:
            print(response.content)
            print(response.status_code)
            if response.content != expected_content:
                print(str(response.content))


class NLPAPIUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
