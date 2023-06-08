from flask import Flask, render_template, request
from Service import GeneratorDM, XMLwork

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')


#Обработчик нажатия кнопки генерации ДМ
@app.route('/Onclick', methods=['POST'])
def onClickGenerate():
    inputText = request.form.get("DMText")
    dm_array = [line.strip() for line in inputText.split('\n') if line.strip()]
    file_names = GeneratorDM.generateDM(dm_array)
    gtins = GeneratorDM.getGtins(dm_array)
    return render_template('AfterInput.html', text=inputText.encode(), file_names=file_names, gtins=gtins)


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['fileInput']
    if file and file.filename.endswith('.xml'):
        file.save('uploads/' + file.filename)
        xml_file_path = 'uploads/' + file.filename
        datamatrix_list = XMLwork.parse_xml(xml_file_path)
        return render_template('index.html', datamatrix_list=datamatrix_list)
    else:
        return "Invalid file format or no file selected"




if __name__ == '__main__':
    app.run(debug=True)


