# Introduction
> This project is a python script used to obtain the triples relationship in the forestry knowledge graph. Includes a crawler that crawls Wikidata data, a script that extracts all Chinese Wiki pages, and a script that aligns Wikidata triples data to Chinese Wiki page statements.
### Environment

python3, Scrapy(Necessary to crawl the corresponding data), neo4j(Alignment), MongoDB(Annotating data)

>Note: all crawlers below perform the following order at the root of each module
    `scrapy crawl XXX`

### Model&taggingDemo&toolkit

The tool used to label the training set. If the tag of **Statement** is correct, click the True button.
Otherwise, select a relationship or enter other relationships. 
If the current sentence cannot be determined, click the Change One button to Change a data description.
Note: **Statement** is the data in **/TrainDataBaseOnWiki/finalData train_data.txt**, we will convert it to json, and imported into the **MongoDB**.
Annotating data also exists in the **MongoDB** in another Collection. About the use of the **MongoDB** can refer to the official tutorial.
We used two Collections in **MongoDB**, one was train_data, that is, data without manual annotation;The other is test_data, which is manually annotated data.
##### How to use?

After starting neo4j,mongodb，go to the taggingdemo directory, launch the django service, and go to 127.0.0.1:8000/tagging.

### WikidataCrawler

**crawls down the relationships defined by wikidata**

All the relationships in wikidata are summarized on this page[(link)](https://www.wikidata.org/wiki/Wikidata:List_of_properties/Summary_table), WikidataCrawler crawls down all the relationships of the summary under the page and their corresponding Chinese names and stores them in json format

##### How to use?

Go to wikidataCrawler directory，launch `scrapy crawl relation`,you can climb to all the relationships defined in wikidata.You can get`relation.json` and `chrmention.json`。

* `relation.json`Content: relation id, relation category, subclass of the relation belongs, corresponding link, relation English representation 
* `chrmention.json`Content: relation id, relation Chinese representation (for the data that does not contain the Chinese representation, we will not do processing for the moment).

Merge the data `relation.json` and `chrmention.json`，launch `mergeChrmentionToRelation.ipynb`, get the match result in `result.json`，The match failure store in `fail.json` 

### wikientities

**Used to crawl entities, return json format**

Go to the wikientities directory, launch`scrapy crawl entity`, get `entity.json`

`entity.json` Search the returned json content on wikidata with the entity in predict_labels.txt as the search term.


> Since we are doing a knowledge graph of the forestry field, many words in predict_labels.txt are about forestry. 
>If you want to climb other entities, you can modify the data in predict_labels.txt by yourself.

### wikidataRelation introduction

##### Triples used to crawl entities and relationships between entities, returning triples


Wikidata is an open, domain-wide knowledge base that contains a large number of entities and their relationships. 

You can see that the wikidata entity page contains the description of the entity and other entities associated with the entity and their corresponding relationships.

WikidataRelation crawls the ternary relationship between the entity and the entity. For example, there is a relationship of `material used` between` synthetic rubber` and `oil`, so you can get the following triples in json format:

`{" entity1 ":" Synthetic rubber "," relation ":" material used "," entity2 ":" Petroleum "}`

##### How to use?

First run `preProcess.py` to get `readytoCrawl.json`. Then go to the `wikidataRelation` directory and run `scrapy crawl entityRelation`. You can get `entityRelation.json`.

`entityRelation.json` is based on using all entities in` entity.json` to get other entities and relationships related to these entities.

### wikidataProcessing 

##### Used to process the resulting triples relationship (entityRelation.json)

Process the obtained entityRelation.json into a csv and store it in the neo4j database. 

launch `relationDataProcessing.py`, can get the following files：
--`new_nodef.csv` (That is, the entities obtained from the wikidata entity page are not included in the `predict_label.txt`)
--`wikidata_relationf.csv`(Relationship between entities in `predict_label.txt`)
--`wikidata_relation2f.csv`(Relationship between entities and newly discovered entities in `predict_label.txt`)，

Import all `csv` in this directory into neo4j

### TrainDataBaseOnWiki

##### Used to align the triples obtained from the wikidata knowledge base onto the Chinese Wiki's corpus:

First, the csv in the `wikidataProcessing` directory must be imported into neo4j to run successfully. 
After running `extractTrainingData.py`, you can get` train_data.txt`, which contains:
(entity1pos entity1 entity2pos entity2 setence relation)

(Note: parallelTrainingData.py in this folder was added later to get the NA relationship data. You can refer to this code to get train_data.txt in parallel.)

There are many attribute relationships (Chinese) in the training set aligned from the Wiki expectation, and even some relationships are empty. Filter this part out and get ** filter_train_data_all.txt **

`` `shell
python filterRelation.py
`` `
Some python files may report errors due to file name changes, just modify the file name

### wikidataAnalyse

wikidataAnalyse: Get `staticResult.txt`, statistics the distribution of various relationships

extractEntityAttribute: Get entity attributes and store them in `attributes.csv`

getCorpus: Get interactive encyclopedia and store them in `hudongBaikeCorpus.txt`

