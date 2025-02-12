from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
import numpy as np
import pandas as pd

def consensus_clustering(data, max_k=5, n_iterations=100, sample_fraction=0.8):
    """
    实现共识聚类
    Args:
        data (pd.DataFrame): 输入基因表达数据，行是基因，列是样品
        max_k (int): 最大聚类数 K
        n_iterations (int): 重复子采样和聚类的次数
        sample_fraction (float): 每次采样的样品比例

    Returns:
        dict: 包括共识矩阵、最佳 K 值和最终分组结果
    """
    n_samples = data.shape[1]
    consensus_matrices = {k: np.zeros((n_samples, n_samples)) for k in range(2, max_k + 1)}

    # 对每个 K 值执行多次采样和聚类
    for k in range(2, max_k + 1):
        for iter in range(n_iterations):
            # 随机采样样品
            sampled_indices = np.random.choice(n_samples, int(sample_fraction * n_samples), replace=False)
            sampled_data = data.iloc[:, sampled_indices]

            # 执行 KMeans 聚类
            kmeans = KMeans(n_clusters=k, random_state=None)
            labels = kmeans.fit_predict(sampled_data.T)  # 转置后每一行为一个样品

            # 更新共识矩阵
            for i, idx_i in enumerate(sampled_indices):
                for j, idx_j in enumerate(sampled_indices):
                    if labels[i] == labels[j]:
                        consensus_matrices[k][idx_i, idx_j] += 1

        # 归一化共识矩阵
        consensus_matrices[k] /= n_iterations

    # 选择最佳 K 值
    avg_consensus = {k: np.mean(consensus_matrices[k]) for k in consensus_matrices}
    best_k = max(avg_consensus, key=avg_consensus.get)

    # 使用最佳 K 值对原始数据进行 KMeans 聚类
    final_kmeans = KMeans(n_clusters=best_k, random_state=None)
    final_labels = final_kmeans.fit_predict(data.T)  # 转置后每一行为一个样品

    return {
        "consensus_matrices": consensus_matrices,
        "best_k": best_k,
        "final_labels": final_labels  # 返回最终分组结果
    }

def plot(results):
    fig, axes = plt.subplots(2, 2, figsize=(16, 16))  # 创建 2x2 子图布局
    clustermap_figures = []

    # 生成带有树状图的热图并保存为图像
    for idx, (k, matrix) in enumerate(results['consensus_matrices'].items()):
        clustermap = sns.clustermap(matrix, cmap="viridis", metric="euclidean", method="average")
        clustermap_figures.append((clustermap, k))  # 保存 clustermap 和 k 值
        plt.close(clustermap.fig)  # 关闭 clustermap 的原始图以避免重复显示

    # 将 clustermap 图像拼接到一个图中
    for idx, (clustermap, k) in enumerate(clustermap_figures):
        ax = axes[idx // 2, idx % 2]  # 确定子图位置
        ax.imshow(clustermap.fig.canvas.buffer_rgba())  # 添加图像
        ax.axis('off')  # 隐藏坐标轴
        ax.set_title(f"Consensus Matrix for k={k}", fontsize=14)  # 在子图上添加标题

    plt.tight_layout()
    plt.show()

def main():
    # 读取数据
    ITG = pd.read_csv('ITG.csv', index_col=0, sep=';')

    # consensus clustering
    result = consensus_clustering(ITG, max_k=5, n_iterations=1000)
    print("best_k:", result["best_k"])
    plot(result)
    df_labels = pd.DataFrame({"Sample": ITG.columns, "Cluster": result["final_labels"]})
    df_labels.to_csv("final_clusters.csv", index=False)

if __name__ == "__main__":
    main()