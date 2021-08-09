from common.utils import ActionException
from locust.user.task import task
from locust import SequentialTaskSet
from common.actions import create_file_in_my, create_folder, delete_folder, editing_open, editing_save, editing_start, favorite_delete, delete_file, file_information, favorite_add, delete_files_and_folders, folder_by_id, move_to_folder, rename_folder, section_shared, update_file_stream, section_my

try:
    stream = open("data/stream_template.docx", "rb")
except IOError:
    print("stream_template.docx not found")


class CreateReadUpdateDeleteFileTaskSet(SequentialTaskSet):
    file_id = 0

    @task
    def create_file(self):
        try:
            self.file_id = create_file_in_my(self.client)
        except ActionException:
            self.interrupt()

    @task
    def get_file_info(self):
        file_information(self.client, self.file_id)

    @task
    def update_file(self):
        update_file_stream(self.client, self.file_id, stream)
        stream.seek(0)
    
    @task
    def delete_file(self):
        delete_file(self.client, self.file_id)

    @task
    def stop(self):
        self.interrupt()

class FavoritesTaskSet(SequentialTaskSet):
    file_id = 0

    @task
    def create_files(self):
        try:
            self.file_id = create_file_in_my(self.client)
        except ActionException:
            self.interrupt()
    
    @task
    def favorites_add(self):
        try:
            favorite_add(self.client, [self.file_id])
        except:
            self.interrupt()

    @task
    def favorites_delete(self):
        favorite_delete(self.client, [self.file_id])

    @task
    def delete_files(self):
        delete_files_and_folders(self.client, [self.file_id], [])

    @task
    def stop(self):
        self.interrupt()

class GetFolderMyTaskSet(SequentialTaskSet):
    
    @task
    def get_folder_my(self):
        section_my(self.client, 100)

    @task
    def stop(self):
        self.interrupt()

class CreateReadUpdateDeleteFolderTaskSet(SequentialTaskSet):
    folder_my_id = 0
    folder_id = 0
    file_id = 0

    @task
    def get_folder_my_id(self):
        try:
            response = section_my(self.client, 20)
        except ActionException:
            self.interrupt()

        self.folder_my_id = response["response"]["files"][0]["folderId"]
    
    @task
    def create_folder_in_my(self):
        try:
            self.folder_id = create_folder(self.client, self.folder_my_id)
        except ActionException:
            self.interrupt()

    @task
    def get_folder(self):
        folder_by_id(self.client, self.folder_id, 100)

    @task
    def update_folder(self):
        rename_folder(self.client, self.folder_id)

        try:
            self.file_id = create_file_in_my(self.client)
        except:
            self.interrupt()

        move_to_folder(self.client, self.folder_id, [], [self.file_id])


    @task
    def delete_folder(self):
        delete_folder(self.client, self.folder_id)

    @task
    def stop(self):
        self.interrupt()

class GetFolderShareTaskSet(SequentialTaskSet):
    
    @task
    def get_folder_share(self):
        section_shared(self.client, 1000)

    @task
    def stop(self):
        self.interrupt()

class EditFileTaskSet(SequentialTaskSet):
    file_id = 0

    @task
    def create_file(self):
        try:
            self.file_id = create_file_in_my(self.client)
        except ActionException:
            self.interrupt()
    
    @task
    def open_edit(self):
        try:
            editing_open(self.client, self.file_id)
        except ActionException:
            self.interrupt()

    @task
    def start_edit(self):
        editing_start(self.client, self.file_id)
    
    @task
    def save_edit(self):
        editing_save(self.client, self.file_id, stream)
        stream.seek(0)
    
    @task
    def delete_file(self):
        delete_file(self.client, self.file_id)
    
    @task
    def stop(self):
        self.interrupt()