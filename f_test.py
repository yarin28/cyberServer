from flask import Flask, render_template, request
from .messege_saver import Message, read_messeges, write_messeges

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = read_messeges()
    print(request.form.get('msg'))
    if request.form:
        print('data=====')
        print(request.form)
        messages.append(Message(request.form.get('msg'),
                                request.form.get('user'),
                                request.form.get('time')))
        # print(messages)
        write_messeges(messages)
    return render_template('chatUi.html', name="weeee",
                           messeges=messages)


if __name__ == "__main__":
    index()
