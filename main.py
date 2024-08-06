from src import Controller, ChineseLanguageModel, BasicView, DataTransformer

model = ChineseLanguageModel()
view = BasicView(windowsize=0.7)
dataTransformer = DataTransformer()

controller = Controller(model, view, dataTransformer)
controller.start()