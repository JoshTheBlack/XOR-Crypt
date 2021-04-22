# coding=utf-8
# XOR Crypt/Decrypt with web interface.
from flask import Flask, render_template, request

app = Flask(__name__)

def decryptXor(data,key):
    result = []
    for i in range(len(data)):
        result.append(int(data[i]) ^ int(key[i%len(key)]))
    return result

def convertToAscii(data):
    ###Takes in a list of ASCII codes and returns a string###
    result = ""
    for bit in data:
        result += chr(int(bit))
    return result

@app.route("/xor/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('data-input', None):
            input = [ord(x) for x in request.values['data-input']]
        else: input = ""
        if request.form.get('data-output', None):
            output = request.values['data-output']
        else: output = ""
        if request.form.get('key', None): okey = request.values['key']
        else: okey = "defaultkey"
        key = [ord(x) for x in okey]
        if output == '' and input != '':
            e = ','.join([str(i) for i in decryptXor(input,key)])
            d = ''
        if input == '' and output != '':
            d = convertToAscii(decryptXor(output.split(','),key))
            e = ''
        return render_template("xor.html", decrypted=d, encrypted=e, key=okey)
    d, key, e = "", "", ""
    return render_template("xor.html", encrypted=e, decrypted=d, key=key)



if __name__ == "__main__":
    app.run()