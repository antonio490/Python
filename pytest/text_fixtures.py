
@pytest.fixture()
def a_tuple():
    '''Return something more interesting'''
    return (1, 'foo', None, {'bar': 23})

def test_a_tuple(a_tuple):
    '''Demo the a_tuple fixture'''
    assert a_tuple[3]['bar'] == 32

