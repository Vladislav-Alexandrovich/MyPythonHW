from api_YouGile import YouGile

from credentials import (url, login, password, companyId, new_project,
                         empty_title, testing_title, edit_title,
                         edited_title, deleted_status, user, wrong_user)

api = YouGile(url, login, password, companyId)


def test_post_project_positive():

    projects_before = api.get_project_list()
    len_before = len(projects_before)

    result = api.post_project(new_project, user)
    assert result.status_code == 201

    response_data = result.json()
    new_id = response_data['id']

    projects_after = api.get_project_list()
    len_after = len(projects_after)

    assert len_after - len_before == 1
    assert projects_after[-1]['title'] == new_project
    assert projects_after[-1]['id'] == new_id

    api.put_edit_project(new_id, True, new_project, user)


def test_post_project_negative():
    projects_before = api.get_project_list()
    len_before = len(projects_before)

    result = api.post_project(empty_title, user)

    projects_after = api.get_project_list()
    len_after = len(projects_after)

    assert result.status_code == 400
    assert len_after - len_before == 0


def test_get_project_by_id_positive():
    result = api.post_project(testing_title, user)
    assert result.status_code == 201

    project_id = result.json()['id']
    new_project = api.get_project_by_id(project_id)

    api.put_edit_project(project_id, True, testing_title, user)

    assert new_project.status_code == 200
    assert new_project.json()['title'] == testing_title
    assert new_project.json()['users'] == user


def test_get_project_by_id_negative():

    new_project = api.get_project_by_id("777")

    assert new_project.status_code == 404


def test_put_edit_project_positive():
    result = api.post_project(edit_title, user)
    assert result.status_code == 201
    project_id = result.json()['id']

    edited = api.put_edit_project(project_id, deleted_status,
                                  edited_title, user)

    api.put_edit_project(project_id, True, edited_title, user)

    assert edited.status_code == 200
    project_title = api.get_project_by_id(project_id).json()['title']
    assert project_title == edited_title


def test_put_edit_project_negative():
    result = api.post_project(edit_title, user)
    project_id = result.json()['id']

    edited = api.put_edit_project(project_id, deleted_status,
                                  edited_title, wrong_user)

    api.put_edit_project(project_id, True, edited_title, user)

    assert edited.status_code == 400
