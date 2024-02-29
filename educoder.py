import os
import json
import firebase_admin
from firebase_admin import credentials, firestore, storage
from google.cloud.exceptions import NotFound
from dotenv import load_dotenv
from rich import print

load_dotenv()

cred = credentials.Certificate('./edu-coder-creds.json')
firebase_admin.initialize_app(cred)

BUCKET_NAME = os.getenv("BUCKET_NAME")

db = firestore.client()
bucket = storage.bucket(BUCKET_NAME)

def educoder_fetch(collection: str = "exams"):
    docs = db.collection(collection).stream()
    doc_list = []
    for doc in docs:
        print(f'=> {doc.id}', end='\n')
        doc_list.append(doc.to_dict()) 
        
    return doc_list

def educoder_fetch_exam_solutions(filepath: str, student: str = "", save: bool = False):
    blobs = list(bucket.list_blobs(prefix=filepath))
    assert len(blobs) > 0, f"No files found in {filepath}"
    student_file = f"{student}.json" if student else "everyone.json"
    found = False

    for blob in blobs:
        if blob.name.endswith('placeholder.txt'):
            continue
        
        if student and not blob.name.endswith(student_file):
            continue 

        if not blob.name.endswith('.json'):
            continue 

        print(f"Loaded: {blob.name}")
        found = True

        if save:
            path = blob.name.replace('/', os.sep)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            blob.download_to_filename(path)
        else:
            blob_content = blob.download_as_text()
            return blob_content

    if not found:
        return "No matching files found."

def print_json(data):
    """
    Prints the provided data in a JSON-readable format.
    """

    print(json.dumps(data, indent=4, sort_keys=True))

    