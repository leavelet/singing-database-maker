wordnlp类使用前置条件：
安装xmnlp包（安装方法：pip install xmnlp）
xmnlp版本0.5.0以上
允许文件编码格式：utf-8

wordnlp包含方法：
setting_nlpmodel（filepos）   设置分词模型路径（默认路径是与wordnlp.py同级文件夹下的xmnlp-onnx-models文件夹）(需要保证每一行后段需要断词中文字符之前没有中文字符出现)
文件每一行格式举例：convention29360-35100 小学篱笆旁的蒲公英
word_processing(filename)   将文件内的内容切分词语，转换为列表输出（不包含每一行前段字符）
output_file(filename)  给定输出文件名称，将分词结果输出到文件中（包含每一行前段字符）（每个词之间有空格）（需要先使用word_processing方法）
输出文件格式举例：convention29360-35100 小学 篱笆 旁 的 蒲公英 
processandoutput(infilename,outfilename) 给定输入输出文件名称，将分词结果输出到输出文件，同时返回值为存储分词结果的列表（包含每一行前段字符）