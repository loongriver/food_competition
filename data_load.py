import pandas as pd 

class data_reader(object):
	"""docstring for data_reader"""
	def __init__(self, data_path):
		super(data_reader, self).__init__()
		self.data_path = data_path
		self.df = pd.read_csv(self.data_path,sep = '\t', header = 'infer', engine = 'python') 

	def show_data(self):
		print(self.df[0:1])

		# 检查缺失值： eventID 和 abstract 有缺失
		print(self.df.isnull().any())

data_path = "Training Set for Competition.txt"
data = data_reader(data_path)
data.show_data()