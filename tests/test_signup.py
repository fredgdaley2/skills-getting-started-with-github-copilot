import pytest


def test_signup_adds_participant(reload_app):
    # Arrange
    app = reload_app()
    activity = "Chess Club"
    email = "test.user@example.com"
    assert email not in app.activities[activity]["participants"]

    # Act
    res = app.signup_for_activity(activity, email)

    # Assert
    assert email in app.activities[activity]["participants"]
    assert res["message"] == f"Signed up {email} for {activity}"


def test_unregister_removes_participant(reload_app):
    # Arrange
    app = reload_app()
    activity = "Chess Club"
    existing = "michael@mergington.edu"
    assert existing in app.activities[activity]["participants"]

    # Act
    res = app.unregister_from_activity(activity, existing)

    # Assert
    assert existing not in app.activities[activity]["participants"]
    assert "Removed" in res["message"]


def test_signup_duplicate_raises(reload_app):
    # Arrange
    app = reload_app()
    activity = "Chess Club"
    existing = "daniel@mergington.edu"
    assert existing in app.activities[activity]["participants"]

    # Act / Assert
    with pytest.raises(app.HTTPException):
        app.signup_for_activity(activity, existing)
