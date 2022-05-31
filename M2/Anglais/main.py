import crepe
from flask import Flask, request, send_file

app = Flask(__name__)


@app.route('/')
def index():
    return ''


@app.route('/', methods=['POST'])
# request.data = wave file as byte array
def upload_file():
    if not request.content_type == 'audio/wave':
        return 'error'
    filename = 'audio.wav'
    f = open(filename, 'wb')
    f.write(request.data)

    crepe.process_file(
        file=filename,
        # output='',  # output directory
        model_capacity='medium',  # medium, full
        viterbi=True,  # ?
        center=True,  # ?
        save_activation=False,  # matrice des données
        save_plot=True,
        plot_voicing=False,
        step_size=10,
        verbose=True
    )
    image = 'audio.activation.png'
    return send_file(image, attachment_filename=image)
