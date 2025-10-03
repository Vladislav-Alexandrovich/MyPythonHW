import requests

class YouGile:
    def __init__(self, url, login=None, password=None, companyId=None):
        self.url = url

    # response_data = resp.json()
    # if 'key' not in response_data:
    #     raise KeyError(f"'key' not found in response. Available keys:
    #                    {list(response_data.keys())}")
    #     return response_data['key']

        self.url = url
        self.token = self.get_token(login, password, companyId)

    def get_token(self, login, password, companyId):
        payload = {
            "login": login,
            "password": password,
            "companyId": companyId
        }
        resp = requests.post(self.url + 'auth/keys/get', json=payload)

        response_data = resp.json()
        return response_data[0]['key']

    def get_project_list(self):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(self.url + 'projects', headers=headers)
        return resp.json()['content']

    def post_project(self, title, users):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        project = {
            "title": title,
            "users": users
        }
        resp = requests.post(self.url + 'projects',
                             headers=headers, json=project)
        return resp

    def get_project_by_id(self, project_id):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(self.url + f'projects/{project_id}',
                            headers=headers)
        return resp

    def put_edit_project(self, project_id, new_deleted, new_title, new_users):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        project = {
            "deleted": new_deleted,
            "title": new_title,
            "users": new_users
        }
        resp = requests.put(self.url + f'projects/{project_id}',
                            headers=headers, json=project)
        return resp
