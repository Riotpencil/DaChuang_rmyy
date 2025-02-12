from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
# 执行 PCA 降维
pca = PCA(n_components=2)  # 降到二维
pca_result = pca.fit_transform(filtered_mmp_data.T)  # 转置后每一行为一个样品

# 使用最佳 K 值的最终聚类结果
final_labels = results["final_labels"]

# 可视化 PCA 结果
plt.figure(figsize=(8, 6))
for cluster in sorted(pca_df["Cluster"].unique()):
    cluster_data = pca_df[pca_df["Cluster"] == cluster]
    plt.scatter(cluster_data["PC1"], cluster_data["PC2"], label=f"Cluster {cluster}", alpha=0.7)

# 添加标题和标签
plt.title("PCA Visualization of Consensus Clustering")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
plt.grid(alpha=0.5)
plt.show()