from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(4,5)==9
    assert add(-5,4)==-1

def test_sub():    
    assert sub(5,4)==1
    assert sub(9,-3)==12
    assert sub(6,9)==-3