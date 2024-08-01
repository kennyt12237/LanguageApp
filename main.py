from src import Controller, ChineseLanguageModel, BasicView, DataTransformer

model = ChineseLanguageModel()
view = BasicView()
dataTransformer = DataTransformer()

controller = Controller(model, view, dataTransformer)
controller.start()