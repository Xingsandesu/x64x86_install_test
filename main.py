import platform


def check_windows_bit_version():
    # 获取系统的位数信息
    bit_version = platform.architecture()[0]

    if bit_version == '32bit':
        input("Windows系统是32位的")
    elif bit_version == '64bit':
        input("Windows系统是64位的")
    else:
        input("无法确定Windows系统位数")


if __name__ == "__main__":
    check_windows_bit_version()
