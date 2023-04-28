import json
#file = open('test1.txt', 'r')#另一种写入方式，与下面搭配。
#formatted_lines = []
num = 0
n=0
tag1 = 0
tag2 = 0
sig1 = 0
sig2 = 0
count = 0
#print("a")#检测程序是否运行1
#t=open("train.json", "a")
#d=open("dev.json", "a")#另一种写入方式，与下面搭配。
with open('test1.txt', 'r',encoding="utf-8") as e :#这里要改成你聊天记录文件的文件名
    for l in e:
        count += 1
e.close()
print("你的聊天记录共",count,"行，现在开始执行\n\n\n\n")
with open('test1.txt', 'r',encoding="utf-8") as f :#这里要改成你聊天记录文件的文件名
    #print("b")#检测程序是否运行2
    for line in f :
        num += 1
        #print(num)
        parts = line.strip()
        if len(parts)>10:
            if parts[4]=="-"and parts[7]=="-"and parts[10]==" ":
                tag2 = num
        if '刘浩然' in line:#这里要改成你的qq昵称
            if tag2==num:
                tag1 = num
            #anwser = line.strip().split('')#另一种查找方式，效果不如现在的。
        if num == tag1+1 and num>1 :
            anwser = line.strip()
            #print("一")
            #print(anwser)
            if abs(sig1+1-sig2)<2 :
                sig1+=1
            #print(sig1)
        elif num == tag2+1 and num>1 :
            question = line.strip()
            #print("二")
            #print(question)
            if abs(sig1-sig2-1)<2 :
                sig2 +=1
            #print(sig2)
        if sig1==sig2 and sig1+sig2!=0:
            n+=1
            data = {
                "content":question,"summary":anwser
                }#这个是GLM的微调格式，如果遇到其他模型需要更换对应的格式和KEY！
            if n%3==0:#训练集的提取，不要轻易改动
                #print(data)#这是检验“训练集"json文件用的
                t = open("train.json", "a+",encoding='utf-8')
                json.dump(data,t,ensure_ascii=False)
                t.write('\n')
                #t.write(data)#其他写入备用
            if n%9==0:#验证集的提取，可以改动，比如现在设置为33.3%且验证集是从训练集中抽取。可以按照需求改成其他设置。
                #print(data)#这是检验“验证集”json文件用的
                d = open("dev.json", "a+",encoding='utf-8')
                json.dump(data,d,ensure_ascii=False)
                d.write('\n')
        print(num,"/",count)#进度检测，后面那个是你的txt总行数
#记得写关闭和备份，否则会导致源文件发生莫名其妙的故障
f.close()
