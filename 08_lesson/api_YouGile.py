import requests


class YouGile:
    def __init__(self, url, login, password, company):
        self.url = url
        self.token = self.get_token(login, password, company)

    def get_token(self, login, password, company):
        payload = {
            "login": login,
            "password": password,
            "companyId": company
        }
        resp = requests.post(self.url + 'auth/keys', json=payload)

        response = resp.json()['key']
        return response

    def get_project_list(self):
        key = self.token
        headers = {
            'Authorization': 'Bearer + key'
        }
        resp = requests.get(self.url + 'projects', headers=headers)
        return resp.json()['content']

    def post_project(self, title, users):
        key = self.token
        headers = {
            'Authorization': 'Bearer + key',
            'Content-Type': 'application/json'
        }
        project = {
            "title": title,
            "users": users
        }
        resp = requests.post(self.url + 'projects', headers=headers, json=project)
        return resp

    def get_project_by_id(self, project_id):
        key = self.token
        headers = {
            'Authorization': 'Bearer + key'
        }
        resp = requests.get(self.url + 'projects/{project_id}', headers=headers)
        return resp

    def put_edit_project(self, project_id, new_deleted, new_title, new_users):
        key = self.token
        headers = {
            'Authorization': 'Bearer + key',
            'Content-Type': 'application/json'
        }
        project = {
            "deleted": new_deleted,
            "title": new_title,
            "users": new_users
        }
        resp = requests.put(self.url + 'projects/{project_id}', headers=headers, json=project)
        return resp