from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_options', methods=['POST'])
def get_options():
    selected_option = request.form.get('selected_option')
    if selected_option == 'option1':
        options = '''
            <option value="option1_1">Option 1.1</option>
            <option value="option1_2">Option 1.2</option>
        '''
    elif selected_option == 'option2':
        options = '''
            <option value="option2_1">Option 2.1</option>
            <option value="option2_2">Option 2.2</option>
        '''
    else:
        options = ''
    return options

if __name__ == '__main__':
    app.run()
