import utils


def test_arewebro_not_bros():
    """ test negative scenario """
    assert utils.are_we_bro("Fabien", "Dark Vador") is False


def test_arewebro_empty():
    """ test empty strings """
    assert utils.are_we_bro("", "") is False


def test_arewebro_empty_friend():
    assert utils.are_we_bro("Fabien", "") is False


def test_arewebro_caps():
    """ test case """
    assert utils.are_we_bro("Fabien", "PIERRE") is False


def test_arewebro_bros():
    """ test positive scenario """
    assert utils.are_we_bro("Fabien", "Pierre") is True
