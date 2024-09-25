# @Time :2024/9/25 22:33
# @Author :codeking



file_size_mb = 101  # 目标文件大小（MB）
file_name = "large_file2.txt"

with open(file_name, "wb") as f:
    f.write(b"x" * (file_size_mb * 1024 * 1024))  # 写入150MB的字节
