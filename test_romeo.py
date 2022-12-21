import romeo

def test_output(capfd, monkeypatch):
    input = ['romeo.txt']

    expected_output = "['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']"
    
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    romeo.original_sorted_word_printer()
    
    out, err = capfd.readouterr()

    assert expected_output in out
