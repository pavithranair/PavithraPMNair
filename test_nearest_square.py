import nearest_square

def test_answer():
    assert nearest_square.near_square(5) == 4
    assert nearest_square.near_square(-12) == 0
    assert nearest_square.near_square(9) == 9
    assert nearest_square.near_square(23) == 16
    
