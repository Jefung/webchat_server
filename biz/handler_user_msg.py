from biz.cal_2000 import find_closest_sublist_200

cmd_func = {
    '求总数接近2000': find_closest_sublist_200,
}
def handler_user_msg(msg) -> str:
    # 命令解析
    msg = msg.strip()
    msg_list = msg.split(' ')
    if len(msg_list) == 0:
        return '需要输入命令'
    cmd = msg_list[0]
    args = ' '.join(msg_list[1:])
    try:
        if cmd in cmd_func:
            result, err_msg = cmd_func[cmd](args)
            if err_msg != '':
                return f'执行失败:{err_msg}'
            return result
        return f'命令({cmd})不存在'
    except Exception as e:
        return f'执行失败:{e}'
if __name__ == '__main__':
    print(handler_user_msg('求总数接近2000 1,2.3,3.4,4.5'))