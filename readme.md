这只是个把qq聊天记录导出并提取成一问一答的训练资料的python脚本

![QQ截图20230428140840](https://user-images.githubusercontent.com/132042689/235070575-3a2652d9-a4d4-48fb-a2b3-e210a33eee53.png)

![QQ截图20230428140852](https://user-images.githubusercontent.com/132042689/235070581-9509cf6e-4573-4a28-84da-7a1f81ef99cf.png)


需要把你的qq聊天记录导出为txt文件,并将文件拷贝到目录里，且将文件名改为test1.txt（或者改脚本内的名字），随后按照脚本内的注释调整参数运行。

最后你的记录会导出到train.json以及dev.json内，继续执行微调就行。

关于效果

我测试了使用5252416行txt聊天记录（按空格格式）导入脚本，最后输出50309行实际可用的训练集，

![QQ截图20230428142557](https://user-images.githubusercontent.com/132042689/235071304-947d88f5-f67a-4b82-9146-e1dc2085118b.png)

应用官方提供的ptuning未调后，效果如图：

![IMG_6988](https://user-images.githubusercontent.com/132042689/235071566-31be4332-3af3-400a-acbf-514e76747962.PNG)

![IMG_6989](https://user-images.githubusercontent.com/132042689/235071599-7c3149e2-bb36-4b6f-ba2d-0a28f1b0ea8d.PNG)

只能说还凑合吧，但确实挺有意思。
