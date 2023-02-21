import pytest
from dundie.core import load
from .constants import PEOPLE_FILE


def setup_module():
    print()
    print("roda antes dos testes desse módulo\n")


def teardown_module():
    print()
    print("roda após dos testes desse módulo\n")


@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("isso é sujeira")
    yield
    file_.remove()


@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test load function"""

    request.addfinalizer(lambda: print("Terminou"))

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == "J"
