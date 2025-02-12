# UCEC ITGB
## 已经完成

`ITG.py`
    
- 读取 `exp.csv` ，筛选目标基因家族的表达数据
- 去除掉不在 `clincal.csv` 中的样本
- 保存为 `ITG_exp.csv`


`cluster.py`

- 读取 `ITG_exp.csv` ，对表达数据进行聚类分析
- 打印 "best_k" 的值
- 画出不同 k 值的聚类图（需要手动保存）
- 保存聚类结果为 `ITG_cluster.csv` (k = 2, label = 0 || 1)


`PCA.py`


## 待完成

## 想法
### 癌症预测
- 通过聚类分析，将样本分为不同的类别，根据朴素贝叶斯分类器，预测患者是否患癌或者预测癌症的类型