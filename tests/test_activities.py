from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    email = "student@example.com"

    if email not in activities[activity_name]["participants"]:
        activities[activity_name]["participants"].append(email)

    response = client.delete(
        f"/activities/{activity_name}/participants?email={email}"
    )

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in activities[activity_name]["participants"]
