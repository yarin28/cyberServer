from flask import Flask, render_template, request
from .messege_saver import Message, read_messeges, write_messeges

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = read_messeges()

    if request.method == 'POST':
        print('data=====')
        print(request.form)
        messages.append(Message(request.form.get('msg'),
                                request.form.get('name'),
                                request.form.get('timestamp')))
        # print(messages)
        write_messeges(messages)
    return render_template('first.html', name="weeee",
                           blobs=[1, 2, 3, 4, 5, 6], messeges=messages)


if __name__ == "__main__":
    index()
