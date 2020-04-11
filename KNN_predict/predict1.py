# coding: utf-8
from classifier import Classifier
import pickle

def create_predict(HudongItem_csv):
	classifier = Classifier('wiki.zh.bin')
	data_set=[]
	f = open("Dataset1.txt", "rb")
	while 1:
		try:
			obj = pickle.load(f)
			data_set.append(obj)
		except:
			break
	f.close()

	classifier.load_trainSet(data_set)
	classifier.set_parameter(weight=[1.0, 3.0, 0.2, 4.0, 0],k=10)
	file_object = open('predict_labels.txt','a')
	
	count = 0
	vis = set()
	file = open("cur_list1.txt", "rb")
	cur_list=[]
	while 1:
		try:
			obj = pickle.load(file)
			cur_list.append(obj)
		except:
			break
	file.close()

	for cur in cur_list:
		title = cur.title
		if title in vis:
			continue
		vis.add(title)
		label = classifier.KNN_predict(cur)
		print(str(title)+" "+str(label)+": "+str(count)+"/")
		file_object.write(str(title)+" "+str(label)+"\n")
	file_object.close()
create_predict('forestry_pedia.csv')
	