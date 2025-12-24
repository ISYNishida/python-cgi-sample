from data_store import save_message, load_messages

def test_save_and_load():
    save_message("nishida", "hello")
    data = load_messages()
    assert "nishida" in data

