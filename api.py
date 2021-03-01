import flask
from flask import request, jsonify, abort, render_template
import stringGenerator

app = flask.Flask(__name__)


@app.route('/api/v1.0/generate', methods=['GET'])
def generate():
    if 'mode' in request.args and 'length' in request.args:
        mode = request.args.get('mode', None)
        length = int(request.args.get('length', None))
        if length > 120:
            abort(400, 'Please understand that the maximum length is currently 120')
        elif length < 1:
            abort(400, 'The length of a string can not be below 1!')
        else:
            if mode == 'numbers':
                resultString = stringGenerator.generateNumbers(length)
            elif mode == 'letters':
                resultString = stringGenerator.generateLetterString('letters', length)
            elif mode == 'uppercaseLetters':
                resultString = stringGenerator.generateLetterString('uppercase', length)
            elif mode == 'lowercaseLetters':
                resultString = stringGenerator.generateLetterString('lowercase', length)
            elif mode == 'punctuation':
                resultString = stringGenerator.generateSpecialCharString(length)
            elif mode == 'allChar':
                resultString = stringGenerator.generateString(length)
            else:
                abort(400, 'Provided mode not found')
    elif 'help' in request.args:
        return '<body style="font-family: Arial, Helvetica, sans-serif;"><h1>Help for the random string generator api</h1><h3>by Alexander Pietsch</h3><a href="https://www.alexpts.de/api/generate">For more detailed help visit this site!</a><p>General syntax for a request:</p><pre>   alexpts.de:8000/api/v1.0/generate?mode=TYPE_OF_STRING_TO_GENERATE&length=LENGTH_OF_STRING_TO_GENERATE</pre><p>Possible modes are:</p><ul><li>numbers: Returns a string of numbers</li><li>letters: Returns a string of upper- and lowercase letters</li><li>uppercase: Returns a string of only uppercase letters</li><li>lowercase: Returns a string of only lowercase letters</li><li>punctuation: Returns a string of punctuation characters (such as: "$%!()$/)</li><li>allChar: Returns a string of all of the above characters (upper- and lowercase, punctuation, numbers)</li></ul></body>'
    else:
        abort(400, 'Please provide a mode and lenght! For help visit https://www.alexpts.de/api/generate')
    
    result = [
        {
            'mode' : mode,
            'stringLength' : length,
            'generatedString' : resultString
        }
    ]

    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
