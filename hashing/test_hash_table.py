import pytest
from hash_table import Hashtable, BLANK



# tests

def test_creation_of_hashtable():
    assert Hashtable(size=100)

def test_show_capacity():
    assert len(Hashtable(size=100)) == 100, "bad capacity"

def test_should_create_empty_value_stores():
    assert Hashtable(size=3).values == [BLANK,BLANK,BLANK]

def test_should_insert_key_value_pais():
    hashtable = Hashtable(size=100)
    hashtable["hola"] = "hello"
    hashtable[98.6] = 37
    hashtable[False] = True

    assert "hello" in hashtable.values
    assert 37 in hashtable.values
    assert True in hashtable.values

    assert len(hashtable) == 100

def test_should_not_contain_none_value_when_created():
    assert None not in Hashtable(size=100).values

def test_should_insert_none_value():
    hashtable = Hashtable(size=100)
    hashtable["key"] = None
    assert None in hashtable.values


@pytest.fixture
def hash_table():
    sample_data = Hashtable(size=100)
    sample_data["hola"] = "Hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data

def test_should_find_value_by_key(hash_table):
    assert hash_table["hola"] == "hello"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True

#def test_should_raise_




test_creation_of_hashtable()
test_show_capacity()
test_should_create_empty_value_stores()
test_should_insert_key_value_pais()
test_should_not_contain_none_value_when_created()
test_should_insert_none_value()
test_should_find_value_by_key() # error is spat here. carry on from __getitem__ part