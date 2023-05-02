import pytest


# num1 = 4
# num2 = 17
# sum = num1 + num2
# print(sum)

# assert sum == 21, 'The summary of the numbers is wrong'

# @pytest.mark.parametrize('input, expected_out, desc',
#                          [
#                              (10, 20, 'positive numbers'),
#                              (0, 0, 'zero values'),
#                              (-5, -20, 'negative values'),
#                              (-5, -10, 'negative values'),
#                              (2, 6, 'failed values')
#                          ]
#                          )
@pytest.mark.parametrize('input, expected_out, desc',
                         [
                             ('Jackson', 7, 'Good Michael test'),
                             ('Gal', 4, 'Wrong Gal Test'),
                             ('', 0, 'zero value name test'),
                             ('Q', 1, 'Good one char name test'),
                             ('Alex21', 6, 'Good with number test')
                         ]
                         )
# def testMultiple(input, expected_out, desc):
#     print('start test for ', desc)
#     res = input * 2
#     assert res == expected_out, 'Assert found'

def testLength(input, expected_out, desc):
    print('start test for ', desc)
    result = len(input)
    assert result == expected_out, 'Assert found'
