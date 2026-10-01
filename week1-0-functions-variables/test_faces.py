from faces import get_message

def test_faces():
    assert get_message("Hello :)") == "Hello 😂"
    assert get_message("Goodbye :(") == "Goodbye ☹️"
    assert get_message(":fogo") == "🔥"
    assert get_message("Hello :) Goodbye :(") == "Hello 😂 Goodbye ☹️"