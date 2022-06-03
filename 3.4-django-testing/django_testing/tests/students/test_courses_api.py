import pytest
from rest_framework.test import APIClient
from students.models import *
from model_bakery import baker


base_url = '/api/v1/courses/'


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


# проверка получения 1го курса
@pytest.mark.django_db
def test_get_course(client, course_factory, student_factory):

    students = student_factory(_quantity=10)
    courses = course_factory(_quantity=2, students=students)
    url = base_url + str(courses[0].id) + '/'
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert data['id'] == courses[0].id


# проверка получения списка курсов
@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get(base_url)
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, d in enumerate(data):
        assert d['id'] == courses[i].id


# проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_get_course_filter_id(client, course_factory):
    courses = course_factory(_quantity=10)
    url = base_url + '?id=' + str(courses[0].id)
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert data[0]['id'] == courses[0].id


# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_get_course_filter_name(client, course_factory):
    courses = course_factory(_quantity=10)
    url = base_url + '?name=' + courses[0].name
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == courses[0].name


# тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    response = client.post(base_url, data={'name': 'Python_course'}, format='json')
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


# тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=10)
    url = base_url + str(courses[0].id) + '/'
    response = client.patch(url, data={'name': 'Java_course'}, format='json')
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == 'Java_course'


# тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=10)
    count = Course.objects.count()
    url = base_url + str(courses[0].id) + '/'
    response = client.delete(url)
    assert response.status_code == 204
    assert Course.objects.count() == count - 1


# тест ограничения числа студентов на курсе
@pytest.mark.parametrize('number, answer', [(20, 'Допустимо'), (21, 'Перебор'), (19, 'Допустимо')])
def test_validating_students_number(settings, number, answer):
    if number <= settings.MAX_STUDENTS_PER_COURSE:
        assert answer == 'Допустимо'
    else:
        assert answer == 'Перебор'

