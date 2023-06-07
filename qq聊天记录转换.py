import re

#你的聊天记录位置
with open('data/my_qq_data/全部消息记录.txt', 'r', encoding='utf-8') as f:
    content = f.read()

#删除行==================
for line in content.splitlines():
    if line.strip() == '================================================================':
        content = content.replace(line, '')
    if "消息分组" in line:
        content = content.replace(line, '')
    if "消息对象" in line:
        content = content.replace(line, '')

pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} .+?\n.+?(?=\n\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}|\Z)'
messages = re.findall(pattern, content, re.DOTALL)
data_messages = []
for msg in messages:
    # 使用\n分割字符串一次
    msg = msg.split('\n', 1)
    # 将分割后的字符串再次分割
    data1 = msg[0].split(' ', 2)[-1]
    data2 = msg[1].replace('\n', '')
    # 过滤掉图片、语音、文件、视频、表情
    if '[图片]' in data2 or '[语音]' in data2 or '[文件]' in data2 or '[视频]' in data2 or '[表情]' in data2 or '' == data2:
        continue
    #进一步处理字符串
    if '(' in data1:
        data1 = data1.split('(', 1)[0]
    if '<' in data1:
        data1 = data1.split('<', 1)[0]
    #组合成字典
    data = {'name': data1, 'message': data2}
    data_messages.append(data)

#填写你的昵称名字
my_name = ''
old_msg = data_messages[0]
new_data = []
for msg in data_messages:
    if msg['name'] == my_name and old_msg['name'] != my_name:
        final_msg = {'instruction': old_msg['message'],"output":msg['message']}
        new_data.append(final_msg)
    old_msg = msg

#输出的json文件
import json
with open('data/my_qq_data/tp.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)
