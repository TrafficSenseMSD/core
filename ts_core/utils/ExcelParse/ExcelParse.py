import openpyxl as xl
class ExcelParser():
	def __init__(self, workbook):
		self.workbook = xl.load_workbook(filename=workbook)
		self.worksheet = self.workbook.active
		self.configuration_index = {
		'Intersection Shape':'A4',
		'Route Weights':'A7',
		'Randomize':'A11',
		'Vehicles Size Distribution':'B4',
		'Vehicles V2I Distribution':'B7',
        'Initialize the Directory':'B11',
		'Driver Impatience':'C4',
		'Autonomous Distribution':'C7',
		'Traffic Demand':'D2',
		'Accident Response':'E2',
		'Optimizer':'F2'
		}
		
	def get_worksheet_value(self, title):
		return self.worksheet[self.configuration_index[title]].value
	
	def get_worksheet_values(self):
		values = {}
		for config in self.configuration_index.keys():
			values[config] = self.get_worksheet_value(config)
		return values
		
	def print_worksheet_values(self):
		values = self.get_worksheet_values()
		for config in values.keys():
			print('{}: {}'.format(config,values[config]))
	
	def print_sheet_names(self):
		print(self.workbook.sheetnames)
		
		
		
		
		
if __name__ == "__main__":
	xlParser = ExcelParser('Configuration.xlsx')
	xlParser.print_worksheet_values()