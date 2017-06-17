"""
The program returns permutations of a string.
"""

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return sequence
    else:
        list_of_permutations = []
        for i in range(len(sequence)):
            seq = sequence[0:i] + sequence[i+1:len(sequence)]
            for element in get_permutations(seq):#recursion call
                for j in range(len(element)):
                    permutation = ''
                    permutation += element[0:j]
                    permutation += sequence[i]
                    permutation += element[j:len(element)]
                    if permutation not in list_of_permutations:
                        list_of_permutations.append(permutation)
        list_of_permutations.sort()               
        return list_of_permutations

if __name__ == '__main__':
    EXAMPLE_INPUT = 'abc'
    print('Input:          ', EXAMPLE_INPUT)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:  ', get_permutations(EXAMPLE_INPUT))
    print(' ')
    EXAMPLE_INPUT = '12'
    print('Input:          ', EXAMPLE_INPUT)
    print('Expected Output:', ['12', '21'])
    print('Actual Output:  ', get_permutations(EXAMPLE_INPUT))
    print(' ')
    EXAMPLE_INPUT = '@#e'
    print('Input:          ', EXAMPLE_INPUT)
    print('Expected Output:', ['#@e', '#e@', '@#e', '@e#', 'e#@', 'e@#'])
    print('Actual Output:  ', get_permutations(EXAMPLE_INPUT))
    print(' ')


