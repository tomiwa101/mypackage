def top_n (items, n):
    """Return the top n item in an array, in desc order.

    Args:
        items (array): list or array-like object ()
        n (int): num of items to return

    Egs:
        >>> top_n([8,3,2,6,5], 3)
        [8,6,5]    
    """

    items.sort(reverse=True)
    return items[:n]