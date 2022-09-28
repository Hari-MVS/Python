""" import unittest

class Test_demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('class method execution')
    def setUp(self):
        print('setup executed')
    def test_hari(self):
        print('test executed')
    def test_venkat(self):
        print('venkat executed')
    def tearDown(self):
        print('teardown executed')
    @classmethod
    def tearDownClass(cls):
        print('teardown class executed')
unittest.main() """

def inser(a):
    le = len(a)
    for i in range(1,le):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j] :
            a[j+1] = a[j]
            j += -1
        a[[j+1]] = key


def insertsort(L):
    for i in range(1,len(L)):
        small = L[i]
        M = range(-1, i)
        M.reverse()
        for j in M:
            if j>=0 and small<L[j]:
                L[j+1]=L[j]
            else:
                break
        L[j+1] = small
    return L

# insert sort
arr = [5, 4, 3, 2, 1]
for i in range(1, len(arr)):
    j = i - 1
    key = arr[i]
    for j in range(j, -2, -1):
        if j < 0 or key >= arr[j]:
            break
        else:
            arr[j + 1] = arr[j]

    arr[j + 1] = key