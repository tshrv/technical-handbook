"""
Problem: Generate all possible combinations of n pairs of open and closed paranthesis
"""

from typing import List
from loguru import logger as lg


def generate_paranthesis(n: int) -> List[str]:
    """
    input:
        n: int
    output:
        Generate all possible combinations of n pairs of open and closed paranthesis
    """
    # see open paranthesis
    pairs = gen_pars(n, '', 0, 0)
    return pairs

def gen_pars(n: int, string: str, open: int, closed: int):
    if open + closed == 2*n:
        return [string] if string else []

    # open - open <= n
    # close - closed <= open
    open_pairs = []
    closed_pairs = []

    if open < n:
        # can go for open
        pairs = gen_pars(n, string+'(', open+1, closed)
        open_pairs.extend(pairs)

    if closed < open:
        # can go for close
        pairs = gen_pars(n, string+')', open, closed+1)
        closed_pairs.extend(pairs)

    return [*open_pairs, *closed_pairs]

    
def main():
    test_cases = [
        (0, set()),
        (1, {'()'}),
        (2, {'()()', '(())'}),
        (3, {'()()()', '()(())', '(())()', '((()))', '(()())'}),
    ]
    for input, expected_output in test_cases:
        actual_output = set(generate_paranthesis(input))
        assert actual_output == expected_output, f'Test case {input} FAILED -> {actual_output}, expected -> {expected_output}'
        lg.info(f'Test case {input} PASSED -> {expected_output}')

    lg.info(generate_paranthesis(4))

if __name__ == '__main__':
    main()