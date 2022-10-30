# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list. remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


def subsets(elements):
    if not elements:
        return [[]]
    x = subsets(elements[1:])
    return x + [[elements[0]] + y for y in x]


# wrapper function
def subsets_of_given_size(elements, n):
    return [x for x in subsets(elements) if len(x) == n]


if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    n = 3
    print(subsets_of_given_size(numbers, n))

# Driver program to test above function
data = list('SQUARE')
i = 0
for p in permutation(data):
    i = i + 1
    print(p)

print(i)


def driver(word):
    # Driver program to test above function
    data = list(word)
    i = 0
    for p in permutation(data):
        i = i + 1
        print(p)

    print(i)


# 6 Words C(6, 6)
driver('SQUARE')

# 5 Words C(6, 5)
driver('SQUAR')
driver('SQUAE')
driver('SQURE')
driver('SQARE')
driver('SUARE')
driver('QUARE')

# 4 Words C(6, 4)
driver('UARE')
driver('QARE')
driver('QURE')
driver('QUAE')
driver('QUAR')
driver('SARE')
driver('SURE')
driver('SUAE')
driver('SUAR')
driver('SQRE')
driver('SQAE')
driver('SQAR')
driver('SQUE')
driver('SQUR')
driver('SQUA')

# 3 Words C(6, 3)
driver('ARE')
driver('URE')
driver('UAE')
driver('UAR')
driver('QRE')
driver('QAE')
driver('QAR')
driver('QUE')
driver('QUR')
driver('QUA')
driver('SRE')
driver('SAE')
driver('SAR')
driver('SUE')
driver('SUR')
driver('SUA')
driver('SQE')
driver('SQR')
driver('SQA')
driver('SQU')

# 2 Words C(6, 2)
driver('RE')
driver('AE')
driver('AR')
driver('UE')
driver('UR')
driver('UA')
driver('QE')
driver('QR')
driver('QA')
driver('QU')
driver('SE')
driver('SR')
driver('SA')
driver('SU')
driver('SQ')

# 1 Words C(6, 1)
driver('S')
driver('Q')
driver('U')
driver('A')
driver('R')
driver('E')

numbers = ['S', 'Q', 'U', 'A', 'R', 'E']
n = 2
print(subsets_of_given_size(numbers, n))