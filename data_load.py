import pandas as pd 

class data_reader(object):
	"""docstring for data_reader"""
	def __init__(self, data_path):
		super(data_reader, self).__init__()
		self.data_path = data_path
		self.df = pd.read_csv(self.data_path,sep = '\t', header = 'infer', engine = 'python') 

	def process_data(self):
		# 获取文本数据
		titles = df['Title']
		abstract = df['abstract']


	def show_data(self):
		print(self.df[0:1])

		# 检查缺失值： eventID 和 abstract 有缺失
		print(self.df.isnull().any())

	def cleanText(self, corpus):
		#对英文做简单的数据清洗预处理，
		punctuation = """.,?!:;(){}[]"""
		corpus = [z.lower().replace('\n','') for z in corpus]
        corpus = [z.replace('<br />', ' ') for z in corpus]

        #treat punctuation as individual words
        for c in punctuation:
            corpus = [z.replace(c, ' %s '%c) for z in corpus]
        corpus = [z.split() for z in corpus]
        return corpus


data_path = "Training Set for Competition.txt"
data = data_reader(data_path)
data.show_data()