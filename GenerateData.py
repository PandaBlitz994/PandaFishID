import kagglehub

# Download latest version
path = kagglehub.dataset_download("markdaniellampa/fish-dataset")

print("Path to dataset files:", path)