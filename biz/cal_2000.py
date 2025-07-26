def find_closest_sublist_200(input_str) -> (str,str):
    return find_closest_sublist(input_str,2000)

def find_closest_sublist(input_str, target) -> (str,str):
    # 将输入字符串转换为浮点数列表
    input_str = input_str.replace(' ', ',')
    input_str = input_str.replace(',', ',')
    try:
        numbers = [float(x) for x in input_str.split(',')]
    except ValueError:
        return '', "输入字符串包含非数字字符"
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

    return f"最接近{target}的总和为{sum(closest_sublist)}, 其子列表为 {','.join(str(x) for x in closest_sublist)}",''

# 示例调用
input_str = "1,2.3,3.4,4.5"
target = 1.2
result = find_closest_sublist(input_str, target)
print(result)