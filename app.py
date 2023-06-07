from flask import Flask, render_template, request
from Service import GeneratorDM

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')


#Обработчик нажатия кнопки генерации ДМ
@app.route('/Onclick', methods=['POST'])
def onClickGenerate():
    inputText = request.form.get("DMText")
    dm_array = inputText.split('\n')
    file_names = GeneratorDM.generateDM(dm_array)
    gtins = GeneratorDM.getGtins(dm_array)
    return render_template('AfterInput.html', text = inputText.encode(), file_names = file_names,
                           gtins = gtins)


if __name__ == '__main__':
    app.run(debug=True)


