'''
代码编写
假设你登录了一个虚拟环境，可以执行两种命令：

goto <bucket_name> - 移动到指定的存储桶 bucket_name。

create <filename> - 在当前存储桶中创建一个名为 filename 的新文件。

如果当前存储桶中已存在同名文件，则此命令不执行任何操作。

你的任务是处理所有给定的命令，并返回最后包含文件数量最多的存储桶的名称。题目保证文件数量最多的存储桶只有一个（没有平局）。

注意：

保证第一个命令是 goto。

保证至少有一个 create 命令。
'''

from collections import defaultdict
def solution(commands):
    filesystem = defaultdict(set)
    current_bucket = ""
    for cmd in commands:
        parts = cmd.split()
        command_type = parts[0]
        if command_type == 'goto':
            current_bucket = parts[1]
        elif command_type == "create":
            filename = parts[1]
            filesystem[current_bucket].add(filename)
    
    max_file = -1
    result_bucket = ""
    for bucket_name, files_set in filesystem.items():
        num_files = len(files_set)
        if num_files > max_file:
            max_file = num_files
            result_bucket = bucket_name
    
    return result_bucket