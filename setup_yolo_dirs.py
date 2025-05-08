import os
import yaml

# 생성할 경로
base_dir = "datasets"
sub_dirs = [
    "images/train",
    "images/val",
    "labels/train",
    "labels/val"
]

# 디렉토리 생성
for sub in sub_dirs:
    path = os.path.join(base_dir, sub)
    os.makedirs(path, exist_ok=True)
    print(f"Created: {path}")

# data.yaml 내용
data_yaml = {
    "path": base_dir,
    "train": "images/train",
    "val": "images/val",
    "names": {
        0: "ground_parking",
        1: "underground_parking",
        2: "disabled_parking",
        3: "no_parking",
        4: "women_parking"
    }
}

# data.yaml 저장
with open("data.yaml", "w") as f:
    yaml.dump(data_yaml, f)
    print("Created: data.yaml")
