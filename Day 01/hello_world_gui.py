from guizero import App, Text

app = App(title='Hello World')
message = Text(app, text='Welcome to the my Hello World ! app')
app.bg="white"
app.display()
