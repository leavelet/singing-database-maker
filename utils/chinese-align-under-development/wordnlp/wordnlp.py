import xmnlp
# xmnlp.set_model("E:/mynlp_model/xmnlp-onnx-models")
# 动态链接模型位置
# 使用/而不是\
# 实际使用需要修改模型位置
xmnlp.set_model("xmnlp-onnx-models")
class wordnlp:
    def setting_nlpmodel(filepos):  # 设置模型路径
        xmnlp.set_model(filepos)
    def word_processing(filename):
        mydatanlp=[]
        wordnlp.filedata=[]
        with open(filename, "r",encoding = "utf-8") as f:  # 读取文件
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                pos=0
                for i in range(0,len(line)):
                    if(u'\u4e00' <= line[i] <= u'\u9fa5'):
                        pos=i
                        break
                Unprocesseddata=line[i:len(line)] # 提取字符
                wordnlp.filedata.append([line[:i],xmnlp.seg(Unprocesseddata)])
                mydatanlp.append(xmnlp.seg(Unprocesseddata))  # 分词
        return mydatanlp
    def output_file(filename):
        with open(filename,'w',encoding="utf-8") as f:  # 写文件
            for i in range(0,len(wordnlp.filedata)):
                f.write(wordnlp.filedata[i][0])
                for j in range(0,len(wordnlp.filedata[i][1])):
                    f.write(wordnlp.filedata[i][1][j])
                    f.write(' ')
                f.write('\n')
    def processAndOutput(infilename,outfilename):  # 同时输出列表和文件
        wordnlp.word_processing(infilename)
        wordnlp.output_file(outfilename)
        return wordnlp.filedata
