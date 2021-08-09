from common.filestasksets import CreateReadUpdateDeleteFileTaskSet, EditFileTaskSet, FavoritesTaskSet, GetFolderMyTaskSet, CreateReadUpdateDeleteFolderTaskSet, GetFolderShareTaskSet
from common.actions import authentication
from locust import HttpUser, between, events

users_names = []

@events.test_start.add_listener
def on_test_start(**kwargs):
    users_names.clear()
    for i in range(1, 50001):
        users_names.append(f"testuser{str(i)}@onlyoffice.com")

try:
    stream = open("data/stream_template.docx", "rb")
except IOError:
    print("stream_template.docx not found")

class OnlyOfficeUser(HttpUser):
    wait_time = between(4, 6)
    tasks = { CreateReadUpdateDeleteFileTaskSet: 2, 
        CreateReadUpdateDeleteFolderTaskSet: 1, 
        GetFolderShareTaskSet: 1, 
        GetFolderMyTaskSet: 3, 
        FavoritesTaskSet: 1, 
        EditFileTaskSet: 2}

    def on_start(self):
        authentication(self.client, {"password": "testuser", "userName":users_names.pop()})