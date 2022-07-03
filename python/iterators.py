"""
We can iterate over an iterable(list, tuple, set, dict) using an iterator

Python's for loop retrieves the iterator for the iterable using iter(iterable) -> iterable.__iter__()

SNIPPET

    for i in sq:
        do something with i

WORKING

    iter(sq) will be called which in turns call sq.__iter__()
    sq.__iter__() should return an object (say itr) that implements its.__next__()
    Now we repeatedly call next(itr) which in turn calls itr.__next__()
    itr.__next__() EITHER returns some value, and it is called again. This requires itr to maintain state.
    OR, it raises StopIteration error, which indicates the for loop to stop.

"""

from typing import Any, List, Optional, Sequence, overload
from loguru import logger as lg

    
class ListIterator:
    """
    Iterated over first <limit> items in the <ls>
    """
    def __init__(self, ls: List, limit: int) -> None:
        self._ls = ls
        self._limit = limit
        self._next_ls_index = 0

    def __iter__(self) -> Any:
        return self

    def __next__(self) -> Any:
        if self._next_ls_index == self._limit:
            raise StopIteration
        else:
            i = self._next_ls_index
            self._next_ls_index += 1
            return self._ls[i]


class StateIterator:
    def __init__(self, states: List[str], limit: Optional[int] = None) -> None:
        """
        Returns only <limit> number of items on iteration
        if limit is not provided, return all of them
        """
        self._states = sorted(states)
        self._limit = limit or len(self._states)
        self._next_state_offset = 0

    def __next__(self) -> str:
        if self._next_state_offset == self._limit:
            raise StopIteration
        i = self._next_state_offset
        self._next_state_offset += 1
        return self._states[i]

class Country:
    """
    A country object has a country name and names of the states
    When it is iterated upon, it should return First-n states lexicographical order
    """
    DEFAULT_STATE_LISTING_COUNT = 3
    def __init__(self, name: str, states: List[str], default_state_listing_count: Optional[int] = None):
        """
        states is a list, not necessarily in order
        """
        self._name = name
        self._states = states
        self._default_state_listing_count = default_state_listing_count or \
            self.DEFAULT_STATE_LISTING_COUNT
    
    def __iter__(self):
        return StateIterator(self._states, self._default_state_listing_count)


def main():
    # manual iteration using default iterator from sequence
    # below code is same as doing -> for i in ls: lg.info(i)
    lg.info('manual iteration')
    ls = ['a', 'b', 'c', 'd']
    iterator = iter(ls)     # ls.__iter__()
    iteration_over = False

    while not iteration_over:
        try:
            next_item = next(iterator)  # iterator.__next__()
            lg.info(next_item)
        except StopIteration as e:
            # when no items left in the iterable(sequence), StopIteration exception is raised
            iteration_over = True
    lg.info('-'*50)

    # manual iteration using a custom iterator for a sequence
    lg.info('manual iteration using a custom iterator for a sequence')
    ls = ['a', 'b', 'c', 'd']
    for i in ListIterator(ls, 4):
        lg.info(i)
    lg.info('-'*50)
    
    # Custom iterable object using custom iterator
    lg.info('Custom iterable object using custom iterator')
    # country = Country('India', ['UP', 'MP', 'MH', 'RJ', 'DL'])
    country = Country('India', ['UP', 'MP', 'MH', 'RJ', 'DL'], default_state_listing_count=None)
    for i in country:
        lg.info(i)
    lg.info('-'*50)
    
main()