import pandas as pd
import util
import cluster

# # 相关基因：整合素信号传导和粘附
# related_genes = [
#     'FAK',        # Focal Adhesion Kinase, 参与整合素信号传导
#     'Talin',      # 连接整合素与细胞骨架的蛋白
#     'Vinculin',   # 参与整合素与肌动蛋白网络的连接
#     'Paxillin',   # 参与整合素介导的信号转导
#     'Src',        # Src 激酶，参与整合素介导的信号传导
#     'Vav1',       # 参与整合素调节的 Rho 家族小GTP酶
#     'PI3K',       # 磷脂酰肌醇3激酶，参与整合素介导的信号通路
#     'RhoA',       # Rho GTP酶，参与细胞迁移和粘附
#     'Rap1',       # GTP酶，调节整合素活性
#     'Integrin Linked Kinase (ILK)',  # 整合素连接激酶，介导整合素信号
#     'CDH1',       # E-钙黏附蛋白，介导细胞间的粘附作用
#     'CDH2',       # N-钙黏附蛋白，参与细胞间粘附
#     'CD44',       # 细胞表面糖胺聚糖受体，参与细胞迁移和粘附
#     'VE-Cadherin (CDH5)', # 血管内皮钙黏附蛋白，调节血管生成
#     'Zyxin',      # 参与细胞粘附和整合素介导的信号
#     'Actin',      # 肌动蛋白，与整合素共同调节细胞骨架
#     'TGF-beta',   # 转化生长因子β，调节细胞粘附、迁移等
# ]

def main():
    # target genes
    ITG_genes = ['ITGA1', 'ITGA2', 'ITGA3', 'ITGA4', 'ITGA5', 'ITGA6', 'ITGA7', 'ITGA8', 'ITGA9', 'ITGA10', 'ITGA11',
            'ITGB1', 'ITGB2', 'ITGB3', 'ITGB4', 'ITGB5', 'ITGB6', 'ITGB7',
            'ITGB8']
    extra_genes = ['FAK', 'Talin', 'Vinculin', 'Paxillin', 'Src', 'Vav1', 'PI3K', 'RhoA', 'Rap1',
                   'ILK', 'CDH1', 'CDH2', 'CD44', 'CDH5',
                   'Zyxin', 'Actin', 'TGF-beta']
    #util.exist(ITG_genes, exp)
    #util.exist(extra_genes, exp)

    # read csv datas
    exp = util.get_data("exp")  # shape: (59427, 585)
    clinical = util.get_data("clincal")  # shape: (488, 5)


    ITG = util.pick_col(ITG_genes, exp) # shape: (19, 585)
    ITG = util.pick_row(clinical.index, ITG) # shape: (19, 488)

    print("shape: ", ITG.shape)
    ITG.to_csv("ITG.csv", index=True, sep=";")



if __name__ == "__main__":
    main()

