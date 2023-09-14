from flask import Flask,render_template,request
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'jsansu64@gmail.com'
app.config['MAIL_PASSWORD'] = 'okyxvztpovpjsncz'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

@app.route('/home',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':

        msg=Message("Email sending feature",sender='jsansu64@gmail.com',recipients=['jsansu64@gmail.com','viditgupta84@gmail.com'])
        print(msg)
        msg.body= "Hey, how are you?"
        mail.send(msg)
        return "sent email"
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)