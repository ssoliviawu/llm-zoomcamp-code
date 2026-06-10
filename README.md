这是https://github.com/DataTalksClub/llm-zoomcamp的课程笔记总结

1. 构建环境    
在磁盘里新建一个空白文件夹并进行初始配置   
mkdir llm-zoomcamp-code    
cd llm-zoomcamp-code    
uv init    
这样就创建了一个 pyproject.toml 以及一个基本的项目结构。    

2. 安装依赖   
uv add requests minsearch openai jupyter python-dotenv   

3. 设置API密钥    
在文件夹里新建一个.env 文件并添加到 .gitignore 中，以确保绝不会意外地提交你的密钥。    
注意Windows 默认 隐藏已知文件扩展名, 确保添加的文件为.env 而不是.env.txt .    
直接打开.gitignore文件，贴上以下两行即可。    
#Environment variables   
.env   
练习使用的是Agnes的Text模型，目前是免费的。   

4. 先看notebook step-by-step.ipynb可以得到分步流程    
   notebook- oop.py是跟ingest.py及rag_helper.py搭配使用的   

   
