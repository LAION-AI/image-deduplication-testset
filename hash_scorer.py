import os
import pickle

import numpy as np
from imagededup.methods import CNN, AHash, DHash, PHash, WHash
from sklearn.metrics import accuracy_score, confusion_matrix

from annotations import annotation


def similar_result(hasher, annotation, max_distance):
    results = []
    gt_labels = []
    pred_dict = {}
    for i in range(1, 178):
        # Encoding
        encodings = hasher.encode_images(image_dir=f"testset/{i}")
        files = os.listdir(f"testset/{i}")
        if max_distance:
            duplicates = hasher.find_duplicates(
                encoding_map=encodings, min_similarity_threshold=max_distance
            )
        else:
            duplicates = hasher.find_duplicates(encoding_map=encodings,)

        # Predictions
        if "query.jpg" in duplicates:
            for j in range(12):
                if f"{j}.jpg" in files and os.path.getsize(f"testset/{i}/{j}.jpg"):
                    gt_labels.append(annotation[i - 1][j])
                    if f"{j}.jpg" in duplicates["query.jpg"]:
                        results.append(1)
                        pred_dict[f"testset/{i}/{j}.jpg"] = 1
                    else:
                        results.append(0)
                        pred_dict[f"testset/{i}/{j}.jpg"] = 0
                    # print(f"testset/{i}/{j}.jpg")
    return (
        confusion_matrix(np.array(gt_labels).flatten(), np.array(results).flatten()),
        accuracy_score(np.array(gt_labels).flatten(), np.array(results).flatten()),
        pred_dict,
    )


res_dict = {}

for i, max_distance in [
    (CNN, 0.9),
    (CNN, 0.91),
    (CNN, 0.92),
    (PHash, None),
    (AHash, None),
    (DHash, None),
    (WHash, None),
]:
    print(i.__name__)
    if max_distance:
        model_name = f"{i.__name__}_{max_distance}"
    else:
        model_name = f"{i.__name__}"
    conf_matrix, acc, pred_dict = similar_result(
        i(verbose=False), annotation, max_distance
    )

    res_dict[model_name] = {
        "pred_dict": pred_dict,
        "confusion_matrix": conf_matrix,
        "accuracy": acc
    }

for i, max_distance in [
    (CNN, 0.9),
    (CNN, 0.91),
    (CNN, 0.92),
    (PHash, None),
    (AHash, None),
    (DHash, None),
    (WHash, None),
]:
    if max_distance:
        model_name = f"{i.__name__}_{max_distance}"
    else:
        model_name = f"{i.__name__}"
    print(model_name)
    print(res_dict[model_name]["accuracy"])
    print(res_dict[model_name]["confusion_matrix"])

with open(f"res_dict.pkl", "wb") as f:
    pickle.dump(res_dict, f, pickle.HIGHEST_PROTOCOL)
f.close()

# print(f"Total images {np.sum(final[f'{i.__name__}'])}")
