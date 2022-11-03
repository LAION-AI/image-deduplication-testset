import numpy as np
from imagededup.methods import AHash, DHash, PHash, WHash
from sklearn.metrics import accuracy_score

from annotations import annotation


def similar_result(hasher, annotation, max_distance_threshold=1):
    results = []
    for i in range(1, 178):
        res = [0] * 12
        try:
            encodings = hasher.encode_images(image_dir=f"testset/{i}")
            duplicates = hasher.find_duplicates(encoding_map=encodings)
            if "query.jpg" in duplicates:
                for i in duplicates["query.jpg"]:
                    res[int(i.split(".")[0])] = 1
        except:
            pass
        results.append(res)

    return (
        results,
        accuracy_score(np.array(annotation).flatten(), np.array(results).flatten()),
    )


final = {}
final_acc = {}
for i in [PHash, AHash, DHash, WHash]:
    # for max_distance in [1, 2, 4]:
    res, acc = similar_result(i(verbose=False), annotation)
    final[f"{i.__name__}"] = res
    final_acc[f"{i.__name__}"] = acc

print(final_acc)

for i in [PHash, AHash, DHash, WHash]:
    for j in [PHash, AHash, DHash, WHash]:
        if i != j:
            print(
                f"{i.__name__} + {j.__name__}",
                accuracy_score(
                    np.array(annotation).flatten(),
                    np.array(
                        np.array(final[f"{i.__name__}"])
                        | np.array(final[f"{j.__name__}"])
                    ).flatten(),
                )
            )
