from sklearn.metrics import accuracy_score
import numpy as np

from imagededup.methods import PHash, AHash, DHash, WHash

from annotations import annotation

def similar_result(hasher, annotation, max_distance_threshold=1):
    results = []
    for i in range(1, 178):
        res = [0] * 12
        try:
            encodings = hasher.encode_images(image_dir=f'testset/{i}')
            duplicates = hasher.find_duplicates(encoding_map=encodings, max_distance_threshold=max_distance_threshold)
            if 'query.jpg' in duplicates:
                for i in duplicates['query.jpg']:
                    res[int(i.split('.')[0])] = 1
        except:
            pass
        results.append(res)

    return accuracy_score(np.array(annotation).flatten(), np.array(results).flatten())

final = {}
for i in [PHash, AHash, DHash, WHash]:
    for max_distance in [1, 2]:
        final[f"{i.__name__}_{max_distance}"] = similar_result(i(verbose=False), annotation, max_distance)

print(final)
