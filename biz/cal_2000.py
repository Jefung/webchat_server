
def find_closest_sublist(input_str, target):
    # 将输入字符串转换为浮点数列表
    input_str = input_str.replace(' ', ',')
    input_str = input_str.replace(',', ',')
    numbers = [float(x) for x in input_str.split(',')]
    n = len(numbers)
    closest_sum = float('inf')
    closest_sublist = []

    def backtrack(start, current_sublist):
        nonlocal closest_sum, closest_sublist
        current_sum = sum(current_sublist)
        # 计算当前子列表和与目标值的差值绝对值
        diff = abs(current_sum - target)
        if diff < abs(closest_sum - target):
            closest_sum = current_sum
            closest_sublist = current_sublist.copy()

        for i in range(start, n):
            current_sublist.append(numbers[i])
            backtrack(i + 1, current_sublist)
            current_sublist.pop()

    backtrack(0, [])
    return closest_sublist

# 示例调用
input_str = "x,2.3,3.4,4.5"
target = 1.2
result = find_closest_sublist(input_str, target)
print(result)