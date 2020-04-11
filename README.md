# Forestry Knowledge Graph

## Introduction

> ### College of Information and Computer Engineering, Northeast Forestry University

## Directory Structure:

```
├── Forestry_View     // Just a demo of forstry knowledge system
│   ├── Model  
│   ├── demo 
│   ├── label_data 
│   │   └── handwork
│   ├── static    
│   │   ├── css
│   │   ├── js
│   │   └── open-iconic
│   ├── templates  
│   └── toolkit   // Tool Library
│   └── KNN_predict   
├── KNN_predict    // KNN algorithm predicts labels
├── Forestry_Tree     // Reptile crawling tree structure of forestry entity in interactive encyclopedia
├── Forestry_Triple    //  Crawling relationships in the wikidata
└── RelationExtraction    // Use FastText_BiGRU_ATT to extract relation from forestry knowledge
```

## Reusable resources

- `forestry_pedia.csv/forestry_pedia2.csv/forestry_pedia3.csv`: Structured csv file of the encyclopedia page of the forestry entity that has been crawled
- `labels.txt`：Manually labeled entity categories
- `predict_labels.txt`: The categories of entities predicted by the KNN algorithm
- `/Forestry_Triple/wikidataProcessing/wikidata_relation.csv`
- `attributes.csv`: Entity attributes

## Project configuration

**0.Environment**

Install python3 and Neo4j
 
Install dependencies
 
--sudo pip3 install -r requirement.txt

**1.Import data into neo4j**

```
LOAD CSV WITH HEADERS  FROM "file:///forestry_pedia.csv" AS line  
CREATE (p:HudongItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList})  

LOAD CSV WITH HEADERS  FROM "file:///forestry_pedia3.csv" AS line  
CREATE (p:HudongItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList}) 

LOAD CSV WITH HEADERS  FROM "file:///forestry_pedia2.csv" AS line  
CREATE (p:HudongItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList})  
```
```
// Create index
CREATE CONSTRAINT ON (c:HudongItem)
ASSERT c.title IS UNIQUE
```

The meaning of the above two steps is to import `forestry_pedia.csv` into neo4j as a node, and then add UNIQUE (unique constraint / index) to the title attribute
Go to `/wikidataSpider/wikidataProcessing`, put `new_node.csv, wikidata_relation.csv, wikidata_relation2.csv` into the import folder of neo4j (run relationDataProcessing.py to get these 3 files), and then run them separately
```
// import new node
LOAD CSV WITH HEADERS FROM "file:///new_node.csv" AS line
CREATE (:NewNode { title: line.title })

// import new node
LOAD CSV WITH HEADERS FROM "file:///new_nodef.csv" AS line
CREATE (:NewNodef { title: line.title })

//Add index
CREATE CONSTRAINT ON (c:NewNode)
ASSERT c.title IS UNIQUE

//Add index
CREATE CONSTRAINT ON (c:NewNodef)
ASSERT c.title IS UNIQUE


//Import the relationship between hudongItem and newly added nodes
LOAD CSV  WITH HEADERS FROM "file:///wikidata_relation2.csv" AS line
MATCH (entity1:HudongItem{title:line.HudongItem}) , (entity2:NewNode{title:line.NewNode})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)

//Import the relationship between hudongItem and newly added nodes
LOAD CSV  WITH HEADERS FROM "file:///wikidata_relation2f.csv" AS line
MATCH (entity1:ForestryDb{title:line.HudongItem}) , (entity2:NewNodef{title:line.NewNode})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)

LOAD CSV  WITH HEADERS FROM "file:///wikidata_relation.csv" AS line
MATCH (entity1:HudongItem{title:line.HudongItem1}) , (entity2:HudongItem{title:line.HudongItem2})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)


LOAD CSV  WITH HEADERS FROM "file:///wikidata_relationf.csv" AS line
MATCH (entity1:ForestryDb{title:line.HudongItem1}) , (entity2:ForestryDb{title:line.HudongItem2})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)
```

**Import Entity attributes**


```cypher
LOAD CSV WITH HEADERS FROM "file:///attributes.csv" AS line
MATCH (entity1:HudongItem{title:line.Entity}), (entity2:HudongItem{title:line.Attribute})
CREATE (entity1)-[:RELATION { type: line.AttributeName }]->(entity2);
                                                            
LOAD CSV WITH HEADERS FROM "file:///attributes.csv" AS line
MATCH (entity1:HudongItem{title:line.Entity}), (entity2:NewNode{title:line.Attribute})
CREATE (entity1)-[:RELATION { type: line.AttributeName }]->(entity2);
                                                            
LOAD CSV WITH HEADERS FROM "file:///attributes.csv" AS line
MATCH (entity1:NewNode{title:line.Entity}), (entity2:NewNode{title:line.Attribute})
CREATE (entity1)-[:RELATION { type: line.AttributeName }]->(entity2);
                                                            
LOAD CSV WITH HEADERS FROM "file:///attributes.csv" AS line
MATCH (entity1:NewNode{title:line.Entity}), (entity2:HudongItem{title:line.Attribute})
CREATE (entity1)-[:RELATION { type: line.AttributeName }]->(entity2)  
                                                                                                                    
```

The above steps are to import the crawled relationship


**2.Start service**

Go to the demo directory and run the script:

```
sudo sh django_server_start.sh
```

----------------------
### Added forestry question and answer

### Shortest path relation query
-Modify some configuration information
-In relational queries, the shortest query between 2 entities has been added to mine some strange implicit relationships between entities

### Forestry entity identification + entity classification

Click the entity's hyperlink to jump to the entry page (the word cloud uses word vector technology):

### Entity query

In the entity query part, we can search for entities related to an entity and the relationship between them:

### Relation query

The relation query is to query the triple relationship entity1- [relation]-> entity2, which is divided into the following cases:

* Specify the first entity entity1
* Specify the second entity entity2
* Specify the first entity entity1 and relationship
* Specify the relationship relation and the second entity entity2
* Specify the first entity entity1 and the second entity entity2
* Specify the first entity entity1 and the second entity entity2 and the relationship

### Knowledge tree structure forestry knowledge  overview section, we can list a list of entries under a forestry classification, these concepts are organized in a tree structure:

## Idea

### Named entity recognition:

Use the `thulac` tool for word segmentation, part-of-speech tagging, named entity recognition (person name, place name, institution name only)
To identify specific entities in the forestry sector, we need to:

1. Word segmentation, part-of-speech tagging, named entity recognition
2. Recognized as a named entity (person, location, organization), if the entity library does not exist, you can mark it out
3. For the non-named entity part, use certain word combinations and part-of-speech rules to scan all participles at O ​​(n) time to filter out parts that are not likely to be agricultural entities (for example, verbs are definitely not agricultural entities)
4. For the remaining words and word combinations, match the classified entities in the knowledge base. If no entity is matched, or the matched entity belongs to class 0 (that is, non-entity), it is filtered out.
5. The classification algorithms for entities are described below.

### Entity Classification:

#### Feature extraction:

#### Classifier: KNN Algorithm

-No need to be expressed as a vector, just compare the similarity
-K value obtained by grid search

#### Define the similarity sim (p1, p2) of the two pages:
- Cosine similarity of word vectors between titles (word vectors calculated using fasttext can avoid out of vocabulary)
- Mean value of cosine similarity of word vectors between 2 groups of openType
- The sum of the IDF values ​​of the same baseInfoKey (because the attribute contribution of 'Chinese name' should be small)
- The same number of baseInfoValue under the same baseInfoKey
- When predicting a page, because KNN compares this page with all pages in the training set, the complexity of each prediction is O (n), n is the training set size. In this process, we can count the IDF values, mean, variance, and standard deviation of each sub-similarity, and then normalize the four similarities: ** (x-mean) / variance **
- The weighted sum of the similarity of the above four parts is the final similarity of the two pages. The weight is controlled by the vector weight, which is obtained through 10-fold cross-validation + grid search.
### Labels：（Classification of named entities）

### Relation extraction(see detail in the directory of relationExtraction)