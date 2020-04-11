import json
from py2neo import Node, Relationship ,Graph
from langconv import *
import re
class loadDatatoNeo4j(object):
	graph = None
	def __init__(self):
		print("start load data ...")
	def connectDB(self):
		self.graph = Graph("http://localhost:7474",username = "neo4j" , password = "xiaohen2018")
		print("connect neo4j success!")

	def readData(self):
		count = 0
		#新写的的new node.csv  先写标题
		with open("new_nodef.csv",'w') as fw:
			fw.write("title,lable"+'\n')


		#新写进去的  先写标题
		with open("wikidata_relationf.csv","w") as fw:
			fw.write("HudongItem1,relation,HudongItem2"+'\n')

		# 新写进去的
		with open("wikidata_relation2f.csv","w") as fw:
			fw.write("HudongItem,relation,NewNode"+'\n')

		#读取实体关系json
		with open("../wikidataRelation/entityRelation1.json","r") as fr:

			#	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
			with open("new_nodef.csv",'a') as fwNewNode:

				with open("wikidata_relationf.csv",'a') as fwWikidataRelation:
					with open("wikidata_relation2f.csv",'a') as fwWikidataRelation2:
						newNodeList = list()
						for line in fr:
							# print(line)
							entityRelationJson = json.loads(line)
							entity1 = entityRelationJson['entity1']
							entity2 = entityRelationJson['entity2']
							#搜索entity1
							find_entity1_result = self.graph.find_one(
								property_key = "title" ,
								property_value = entity1,
								label = "HudongItem"
							)
							#搜索entity2
							find_entity2_result = self.graph.find_one(
								property_key = "title",
								property_value = entity2,
								label = "HudongItem"
							)
							count += 1
							print(count/12358)
							# 如果entity1不在实体列表中(emmmmmm,不可能吧)，那么就不要继续了
							if(find_entity1_result is None):
								continue

							#去掉entityRelationJson['relation']中的逗号和双引号
							entityRelationList = re.split(",|\"",entityRelationJson['relation'])
							entityRelation = ""
							for item in entityRelationList:
								entityRelation = entityRelation + item
							#去掉entity2字符串中的逗号,并将繁体转成简体
							entity2List = re.split(",|\"",entity2)
							entity2 = "" 
							for item in entity2List:
								entity2 = entity2 + item
							entity2 = Converter('zh-hans').convert(entity2)

							# 如果entity2既不在实体列表中，又不在NewNode中，则新建一个节点，该节点的lable为newNode，然后添加关系
							if(find_entity2_result is None):
								if(entity2 not in newNodeList):
									fwNewNode.write(entity2+","+"newNode"+'\n')
									newNodeList.append(entity2)
								fwWikidataRelation2.write(entity1+","+entityRelation+","+entity2+'\n')
							#如果entity2在实体列表中，直接连关系即可
							else:
								fwWikidataRelation.write(entity1+","+entityRelation+","+entity2+'\n')



if __name__ == "__main__":
	loadData = loadDatatoNeo4j()
	loadData.connectDB()
	loadData.readData()









		
