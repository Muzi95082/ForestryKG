## Relation extraction

Chinese Forestry Knowledge Graph Relation Extraction

### data

Process the data set to get the json file needed for relation extraction

step:
* If there is no `filter_train_data_all_deduplication.txt` in the current folder, then go to the wikidataSpider directory and follow the method described in TrainDataBaseOnWiki / readme.md,


Get `filter_train_data_all_deduplication.txt` (It takes a long time to generate data, it is recommended to test with a public data set. Use a public data set, directly enter Algorithm from the ignore, and ignore all subsequent operations)
* Run `python dosomething.py filter_dataset` to get` filtered_data.txt`
* Run `python preprocessing.py rel2id` to get `rel2id.json`
* Run `python preprocessing.py dataset.json` to get `dataset.json`
* Run `python preprocessing.py word2vecjson` to get `word2vec.json`
* Run `python preprocessing.py entity2id` to get `entity2id.json`
* Run `python preprocessing.py dataset_split` to get `train_dataset.json` and `test_dataset.json`

The obtained rel2id.json, word2vec.json, entity2id.json, train_dataset.json, and test_dataset.json are the data required by the relationship extraction algorithm, and put them in the data / forestry directory of algorithm
Process the data set to get the json file needed for relation extraction
### algorithm

Algorithm part of relation extraction, implemented by FastText_BiGRu_ATT

##### data

Store the data required for relation extraction. If you only test the relation extraction algorithm, it is recommended to use public data such as nyt.


* `forestry_data` the forestry knowledge graph data
* `nyt_data` Public dataset, New York Times data
* `SemEval2010` Public dataset





