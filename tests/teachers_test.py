def test_get_assignments_teacher_1(client, h_teacher_1):
    response = client.get(
        '/teacher/assignments',
        headers=h_teacher_1
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['teacher_id'] == 1


def test_get_assignments_teacher_2(client, h_teacher_2):
    response = client.get(
        '/teacher/assignments',
        headers=h_teacher_2
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['teacher_id'] == 2
        assert assignment['state'] in ['SUBMITTED', 'GRADED', 'DRAFT']


def test_grade_assignment_cross(client, h_teacher_2):
    """
    failure case: assignment 1 was submitted to teacher 1 and not teacher 2
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_2,
        json={
            "id": 1,
            "grade": "A"
        }
    )

    assert response.status_code == 400
    data = response.json

    assert data['error'] == 'FyleError'


def test_grade_assignment_bad_grade(client, h_teacher_1):
    """
    failure case: API should allow only grades available in enum
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": 1,
            "grade": "AB"
        }
    )

    assert response.status_code == 400
    data = response.json

    assert data['error'] == 'ValidationError'


def test_grade_assignment_bad_assignment(client, h_teacher_1):
    """
    failure case: If an assignment does not exists check and throw 404
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": 100000,
            "grade": "A"
        }
    )

    assert response.status_code == 404
    data = response.json

    assert data['error'] == 'FyleError'


def test_grade_assignment_draft_assignment(client, h_teacher_1):
    """
    failure case: only a submitted assignment can be graded
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1
        , json={
            "id": 2,
            "grade": "A"
        }
    )

    assert response.status_code == 400
    data = response.json

    assert data['error'] == 'FyleError'

# Grading API test
# Test: Teacher grades an assignment successfully

def test_grade_assignment_not_submitted(client, h_teacher_1):
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            'id': 3,  # The assignment ID that is in DRAFT state
            'grade': 'A'
        }
    )

    assert response.status_code == 400
    error_response = response.json
    assert error_response['error'] == 'FyleError'


# Test: Teacher tries to grade an assignment that does not belong to them
def test_grade_assignment_wrong_teacher(client, h_teacher_1):
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            'id': 2,  # The assignment ID that is assigned to a different teacher
            'grade': 'A'
        }
    )

    assert response.status_code == 400
    error_response = response.json
    assert error_response['error'] == 'FyleError'


# Test: Teacher tries to grade a non-existent assignment
def test_grade_assignment_not_found(client, h_teacher_1):
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            'id': 9999,  # Non-existent assignment ID
            'grade': 'A'
        }
    )

    assert response.status_code == 404
    error_response = response.json
    assert error_response['error'] == 'FyleError'


# Test: Invalid grade value
def test_grade_assignment_invalid_grade(client, h_teacher_1):
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            'id': 2,
            'grade': 'Z'  # Invalid grade value
        }
    )

    assert response.status_code == 400
    error_response = response.json
    assert error_response['error'] == 'ValidationError'