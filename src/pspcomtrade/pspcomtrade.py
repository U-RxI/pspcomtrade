from typing import Iterable

def find_idx(array : Iterable, value : float) -> int:
    """
    Function to find the equivalent index to a specific time in a array representing time

    Parameters
    ----------
    array : Iterable
        Array like object representing time
    value : float

    Returns
    -------
    int : nearest index to the given time value

    Example
    -------
    >>> find_idx([0, 0.1, 0.2, 0.3, 0.4], 3)
    3
    >>> find_idx([0, 0.1, 0.2, 0.3, 0.4], 0.12)
    1
    """
    n = [abs(i-value) for i in array]
    idx = n.index(min(n))
    return idx


# To do
# test for singal with 1 in the beginning and/or end
def binaryplot(ax, name, stream, time, changed_only=True):
    flag = False
    for i in range(len(time)):
        if stream[i] and (not flag):
            start = time[i]
            flag = True
        elif not stream[i] and flag:
            flag = False
            end = time[i - 1]
            ax.barh(name, end - start, left=start, color='b')
        else:
            continue

    if not all(stream) and not changed_only:
        ax.barh(name, time[-1], left=0, alpha=0)  # invisible bar