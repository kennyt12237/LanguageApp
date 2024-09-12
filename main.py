from src import Controller, ChineseLanguageModelV2, BasicView, DataTransformer

model = ChineseLanguageModelV2()
view = BasicView(windowsize=0.7)
dataTransformer = DataTransformer()

controller = Controller(model, view, dataTransformer)
controller.start()