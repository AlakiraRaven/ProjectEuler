
import Problem3_LargestPrimeFactor as p3


def test_IfPrime():
    expected = [2, 3, 5, 7]
    calculated = []
    for i in range(2, 10):
        if p3.IfPrime(i) == True:
            calculated.append(i)
    print(calculated)
    assert expected == calculated, "WRONG!!!"

    

if __name__ == "__main__":
    test_IfPrime ()

