import pytest
import calculate
import UI


def test_operator_compare_prime_test():
    assert calculate.operator_compare('*', '+') == 1
    assert calculate.operator_compare('+', '+') == 0
    assert calculate.operator_compare('+', '*') == -1

def test_string_to_signals():
    # [1, 2, 3] 传入为空字符串，输出为空list
    assert calculate.string_to_signals(" ") == [' ']
    # [1, 2, 4, 5, 2, 3] 传入为一个运算符，输出为包含单个元素的list
    assert calculate.string_to_signals("+") == ['+']
    # [1, 2, 4, 6, 8, 9, 2, 3] 传入为一个数字，输出为包含单个元素的list
    assert calculate.string_to_signals("1") == [1]
    # [1,2,4,6,7,9,2,4,5,2,3] 传入为一个数字加一个运算符，输出为包含两个元素的list
    assert calculate.string_to_signals("1+") == [1, '+']
    # [1,2,4,6,8,9,2,4,6,7,9,2,4,6,8,9,2,3] 传入为一个数字加一个运算符再加一个数字，输出为包含一个计算式的list
    assert calculate.string_to_signals("1+1") == [1, '+', 1]
    # [1,2,4,6,8,9,10,2,3] 这个测试用例无法执行，因为start本身开始就是-1，无法到达节点8，本次测试用例使用空代替
    assert calculate.string_to_signals(" ") == [' ']
    # [1,2,4,5,2,4,6,7,9,10,2,3] 传入为一个运算符加一个数字，输出为包含两个元素的list
    assert calculate.string_to_signals("+1") == ['+', 1]
    # [1,2,4,6,8,9,10,2,4,5,2,3] 这个测试用例也无法执行，因为start本身开始就是-1，无法经过start != -1的链路，无法到达节点8，本次测试用例使用空代替
    assert calculate.string_to_signals("+1") == ['+', 1]
    # [1,2,4,6,7,9,2,4,6,8,9,2,4,5,2,4,5,2,3] 传入为两个数字加两个运算符，输出为包含三个元素的list
    assert calculate.string_to_signals("11++") == [11, '+', '+']
    # [1,2,4,6,7,9,10,2,4,6,8,9,10,2,4,6,7,9,2,3] 传入为三个数字，输出为一个三位数
    assert calculate.string_to_signals("102") == [102]

def test_suffix_calculate():
    # [1,2,5] 本测试用例无法执行，由于传入为空字符串，而函数逻辑又是将字符串中元素压入栈中，len(stack) = 0，所以碰到函数中的assert则会抛出错误
    assert calculate.suffix_calculate([0]) == 0
    # [1,2,4,7] 传入为非运算符非数字，则会抛出错误"the suffix is illegal"
    with pytest.raises(Exception) as errCode:
        calculate.suffix_calculate(['?'])
    assert str(errCode.value) == "the suffix is illegal"
    # [1,2,3,2,3,2,5] 本测试用例无法执行，传入的为两个数字，其中不包含运算符，则len(stack) = 0，所以碰到函数中的assert则会抛出错误
    assert calculate.suffix_calculate([0]) == 0
    # [1,2,3,2,4,7] 传入的为一个数字一个非运算符非数字，则会抛出错误"the suffix is illegal"
    with pytest.raises(Exception) as errCode:
        calculate.suffix_calculate([1, '?'])
    assert str(errCode.value) == "the suffix is illegal"
    # [1,2,4,6,8,2,4,6,9] 传入的为两个运算符，则会抛出错误"input numbers illegal"
    with pytest.raises(Exception) as errCode:
        calculate.suffix_calculate(['+', '-'])
    assert str(errCode.value) == "input numbers illegal"
    # [1,2,4,6,8,2,4,6,8,2,5] 本测试用例无法执行，传入的为两个运算符，则无法做到len(stack) >= operator_nums，所以无法连续两次从6到8
    assert calculate.suffix_calculate([0]) == 0
    # [1,2,3,2,4,7] 传入的为一个运算符一个非运算符非数字，则会抛出错误"input numbers illegal"
    with pytest.raises(Exception) as errCode:
        calculate.suffix_calculate(['+', '?'])
    assert str(errCode.value) == "input numbers illegal"
    # [1,2,4,6,9] 传入的为单个运算符，则会抛出错误"input numbers illegal"
    with pytest.raises(Exception) as errCode:
        calculate.suffix_calculate(['+'])
    assert str(errCode.value) == "input numbers illegal"
    # [1,2,3,2,4,6,8,2,3,2,5] 传入的为两个数字，一个运算符，输出为计算结果
    assert calculate.suffix_calculate([1, 1, '+']) == 2
    # [1,2,3,2,4,6,9] 传入的为一个数字，一个运算符，则会抛出错误"input numbers illegal"
    with pytest.raises(Exception) as errCode:
        calculate.suffix_calculate([2, '+'])
    assert str(errCode.value) == "input numbers illegal"

def test_input_character():
    # 点击按钮C，清空屏幕
    assert calculate.input_character("C", "") == 'C'
    # 屏幕不为空时，点击按钮=，计算结果
    assert calculate.input_character("=", "1+2") == '='
    # 屏幕不为空时，点击按钮Del，删除上一步的输入
    assert calculate.input_character("Del", "1+23") == 'del'
    # 点击其他按钮，输入内容
    assert calculate.input_character("2", "1+") == 'input'





