from src.utils import are_we_bro
# have to import like this otherwise pytest plays dumb

def test_arewebro_not_bros():
    """ test negative scenario """
    assert are_we_bro("Fabien", "Dark Vador") is False


def test_arewebro_empty():
    """ test empty strings """
    assert are_we_bro("", "") is False


def test_arewebro_empty_friend():
    assert are_we_bro("Fabien", "") is False


def test_arewebro_caps():
    """ test case """
    assert are_we_bro("Fabien", "PIERRE") is False


def test_arewebro_bros():
    """ test positive scenario """
    assert are_we_bro("Fabien", "Pierre") is True
