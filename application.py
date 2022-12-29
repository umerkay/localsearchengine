
from flask import Flask, send_from_directory, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from Indices import loadIndices, genIndices
from Query import Query
from timeit import default_timer as timer
from flask_uploads import UploadSet, configure_uploads, ALL, extension
import shutil

app = Flask(__name__, static_url_path='', static_folder='client/dist')

files = UploadSet('files', ALL)
app.config['UPLOADED_FILES_DEST'] = 'uploads'
configure_uploads(app, files)

CORS(app)
api = Api(app)

lex, fwdInd, invInd = loadIndices()

print("Ready to Search..")

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return 'No files part'
    uploaded_files = request.files.getlist("files")
    for file in uploaded_files:
        if file and extension(file.filename) == 'json':
            filename = files.save(file)
        else:
            return 'Invalid file type'

    start = timer()
    genIndices("uploads", True, lex)
    elapsed = timer() - start

    shutil.rmtree('uploads')

    return {"msg": "Indexed in " + ((str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2))) + "s")}

@app.route('/search', methods=['GET'])
def search():
    queryText = request.args.get('q')
    pageStart = int(request.args.get("pageStart", default=0))
    pageSize = int(request.args.get("pageSize", default=15))

    start = timer()
    res, total = Query(fwdInd, invInd, lex, queryText).getResults().rankResults(pageStart, pageSize)
    elapsed = timer() - start
   
    return {"Search": res, "Response": True, "totalResults": total, "time": (str(round(elapsed * 1000)) + "ms") if elapsed < 1 else (str(round(elapsed, 2)) + "s")}

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')
