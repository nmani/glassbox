import pytest
from gbfullsession_model import GBFullSession

def test_gbfullsession_model():
    # Test valid input
    session = GBFullSession(
        session_id="1234",
        resultCode=1,
        clientIPs=["192.168.0.1"],
        serverIPs=["192.168.0.2"],
        userAgent="Mozilla/5.0",
        userNames="John Doe",
        appIds=[1, 2, 3],
        sessionTags="tag1",
        sessionCurrentDimensions={"dimension1": "value1"},
        avgDownloadTime=100,
        avgResponseSize=1024,
        sessionStartTimeTS="2022-01-01T00:00:00Z",
        sessionEndTimeTS="2022-01-01T01:00:00Z",
        numOfPages=5,
        queryId="abcd"
    )
    assert session.session_id == "1234"
    assert session.resultCode == 1
    assert session.clientIPs == ["192.168.0.1"]
    assert session.serverIPs == ["192.168.0.2"]
    assert session.userAgent == "Mozilla/5.0"
    assert session.userNames == "John Doe"
    assert session.appIds == [1, 2, 3]
    assert session.sessionTags == "tag1"
    assert session.sessionCurrentDimensions == {"dimension1": "value1"}
    assert session.avgDownloadTime == 100
    assert session.avgResponseSize == 1024
    assert session.sessionStartTimeTS == "2022-01-01T00:00:00Z"
    assert session.sessionEndTimeTS == "2022-01-01T01:00:00Z"
    assert session.numOfPages == 5
    assert session.queryId == "abcd"

    # Test invalid input
    with pytest.raises(ValueError):
        GBFullSession(
            session_id="1234",
            resultCode=0,
            clientIPs=["192.168.0.1"],
            serverIPs=["192.168.0.2"],
            userAgent="Mozilla/5.0",
            userNames="John Doe",
            appIds=[1, 2, 3],
            sessionTags="tag1",
            sessionCurrentDimensions={"dimension1": "value1"},
            avgDownloadTime=100,
            avgResponseSize=1024,
            sessionStartTimeTS="2022-01-01T00:00:00Z",
            sessionEndTimeTS="2022-01-01T01:00:00Z",
            numOfPages=-5,  # Invalid value
            queryId="abcd"
        )

if __name__ == "__main__":
    pytest.main([__file__])