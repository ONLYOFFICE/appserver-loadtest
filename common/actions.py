from common.utils import ActionException

def authentication(client, auth_data):
    response = client.post("/authentication", json=auth_data)

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {authentication.__name__}")

    client.headers.update({"Authorization": response.json()["response"]["token"]})

def create_file_in_my(client):
    file_id = 0

    response = client.post("/files/@my/file", json={"title": "TestFile.docx"})

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {create_file_in_my.__name__}")

    file_id = response.json()["response"]["id"]

    return file_id

def delete_file(client, file_id):
    response = client.delete(f"/files/file/{str(file_id)}", json={"deleteAfter": False, "immediately": True}, 
    name="/api/2.0/files/file/fileId")

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {delete_file.__name__}")

    return response.json()


def file_information(client, file_id):
    response = client.get(f"/files/file/{str(file_id)}", name="/api/2.0/files/file/fileId")

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {file_information.__name__}")

    return response.json()

def favorite_add(client, file_ids):
    response = client.post("/files/favorites", json={"fileIds": file_ids})

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {favorite_add.__name__}")

    return response.json()

def favorite_delete(client, file_ids):
    response = client.delete("/files/favorites", json={"fileIds": file_ids})

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {favorite_delete.__name__}")

    return response.json()

def delete_files_and_folders(client, file_ids, folder_ids):
    response = client.put("/files/fileops/delete", json={"folderIds": folder_ids, "fileIds": file_ids, 
    "deleteAfter": False, "immediately": True})

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {delete_files_and_folders.__name__}")
    
    return response.json()

def update_file_stream(client, file_id, stream):
    response = client.put(f"/files/{str(file_id)}/update", files={"file": stream}, json={"file": "N/A"}, 
    name="/api/2.0/files/fileId/update")

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {update_file_stream.__name__}")
    
    return response.json()

def section_my(client, elements_count):
    response = client.get(f"/files/@my?count={str(elements_count)}")

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {section_my.__name__}")
    
    return response.json()

def section_shared(client, elements_count):
    response = client.get(f"/files/@share?count={str(elements_count)}")

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {section_shared.__name__}")
    
    return response.json()

def create_folder(client, folder_id):
    created_folder_id = 0

    response = client.post(f"/files/folder/{str(folder_id)}", json={"title": "TestFolder"}, 
    name="/api/2.0/files/folder/folderId")

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {create_folder.__name__}")

    created_folder_id = response.json()["response"]["id"]

    return created_folder_id

def delete_folder(client, folder_id):
    response = client.delete(f"/files/folder/{str(folder_id)}", json={"deleteAfter": False, "immediately": True}, 
    name="/api/2.0/files/folder/folderId")

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {delete_folder.__name__}")

    return response.json()

def folder_by_id(client, folder_id, elements_count):
    response = client.get(f"/files/{str(folder_id)}?count={str(elements_count)}", name="/api/2.0/files/folderId")

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {folder_by_id.__name__}")

    return response.json()

def rename_folder(client, folder_id):
    response = client.put(f"/files/folder/{str(folder_id)}", json={"title": "NewTitle.docx"}, name="/api/2.0/files/folderId")

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {rename_folder.__name__}")

    return response.json()

def move_to_folder(client, dest_folder_id, folder_ids, file_ids):
    response = client.put("/files/fileops/move", json={"destFolderId": dest_folder_id, "folderIds": folder_ids, 
    "fileIds": file_ids, "conflictResolveType": 1, "deleteAfter": False})

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {move_to_folder.__name__}")

    return response.json()

def editing_open(client, file_id):
    response = client.get(f"/files/file/{str(file_id)}/openedit", name="/api/2.0/files/file/fileId/openedit")

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {editing_open.__name__}")

    return response.json()

def editing_start(client, file_id):
    response = client.post(f"/files/file/{str(file_id)}/startedit", json={"editingAlone": True, "doc": "null"}, 
    name="/api/2.0/file/fileId/startedit")

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {editing_start.__name__}")

    return response.json()

def editing_track(client, file_id, is_finish):
    response = client.get(f"/files/file/{str(file_id)}/trackeditfile?isFinish={is_finish}", 
    name="/api/2.0/file/fileId/trackeditfile")

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {editing_track.__name__}")

    return response.json()

def editing_save(client, file_id, stream):
    response = client.put(f"/files/file/{str(file_id)}/saveediting", files={"stream": stream},
    json={"fileExtension": "docx", "downloadUri": "null", "stream": "N/A", "doc": "null", "forcesave": True}, 
    name="/api/2.0/files/file/fileId/saveediting")

    if response.status_code != 200:
        raise ActionException(f"Failed. Action: {editing_save.__name__}")

    return response.json()