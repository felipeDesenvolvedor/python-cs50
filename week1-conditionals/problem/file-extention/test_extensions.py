from extensions import get_extention

def test_get_extention():
    assert get_extention("cat.gif") == "image/gif"
    assert get_extention("cat.jpg") == "image/jpeg"
    assert get_extention("cat.jpeg") == "image/jpeg"
    assert get_extention("cat") == "application/octet-stream"
    assert get_extention("happy.jpg") == "image/jpeg"
    assert get_extention("document.pdf") == "application/pdf"