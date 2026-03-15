def test_get_activities_returns_dict(reload_app):
    # Arrange
    app = reload_app()

    # Act
    activities = app.get_activities()

    # Assert
    assert isinstance(activities, dict)
    assert "Chess Club" in activities
