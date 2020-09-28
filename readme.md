## 制作数据集
### 工具
- `via-2.0.9`
- `labelme`
### 过程
1. 使用labelme正常标注
2. 划分数据集，train:0.8, val:0.2
3. 运行data_dataset_coco/labelme2coco.py 生成单个json文件
4. 导入到via，重新via格式标注文件
5. via标注文件添加name属性

## 训练和识别
`*参考mrcnn-blog.doc*`