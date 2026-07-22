def add(a,b):
    return a+b
def test_addition():
    assert add(2,2) == 5
def test_nagetive():
    assert add(-1,1)==0
def test_addition_zero():
    assert add(0,0)==0