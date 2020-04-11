
# Chinese Relation Extraction Based on Deep Learning for Forestry Knowledge Graph Construction
Use FastText to deal with forestry entities, and then use Bi-directional GRU with Word and Sentence Dual Attentions for End-to End Relation Extraction
## Requrements

* Python (>=3.5)
* TensorFlow (>=r1.0)
* Scikit-learn (>=0.18)
* fastText
* numpy=1.16.2
## Usage
### * Training:
1. Prepare data in forestry_data/ , including relation types (relation2id.txt), training data (train.txt), testing data (test.txt) and Chinese word vectors (vec.txt).
2. Organize data into npy files, which will be save at data/
```
#python initial.py
```
3. Training, models will be save at model/
```
#python train_GRU.py
```
### * Inference

**If you have trained a new model, please remember to change the pathname in main_for_evaluation() and main() in test_GRU.py with your own model name.**

```
#python3 test_GRU.py
```

Program will ask for data input in the format of "name1 name2 sentence".

We have pre-trained model in /model. To test the pre-trained model, simply initialize the data and run test_GRU.py:

```
#python3 initial.py
#python3 test_GRU.py
```
## Explanation
* forestry_data file contains
---including relation types (relation2id.txt)
---testing data (test.txt)
---training data (train.txt)
---Chinese word vectors (vector.txt)## **predict_label file generates entity vectors by FastText**