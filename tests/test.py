from mypackage import myModule

def test_top_n():
    """
    make sure top_n wokrs correctly
    """

    assert myModule.top_n([8,3,2,4,5,10], 3) == [10,8,5], 'incorrect'
    assert myModule.top_n([9,7,2,4,5,1], 2) == [9,7], 'incorrect'
    assert myModule.top_n([5,3,2,4,5,10], 5) == [10,5,5,4,3], 'incorrect'