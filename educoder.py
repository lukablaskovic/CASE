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

def educoder_fetch(collection: str = "exams", parent_path: str = "", depth: int = 0, max_depth: int = 1):
    """
    Fetch documents from a Firebase collection, including nested collections up to a specified depth.
    
    :param collection: The name of the collection to fetch from.
    :param parent_path: The Firestore path of the parent collection (used for recursion).
    :param depth: The current depth of recursion.
    :param max_depth: The maximum depth to fetch nested collections.
    :return: A list of documents, including nested documents up to max_depth.
    """
    full_path = f"{parent_path}/{collection}" if parent_path else collection
    docs = db.collection(full_path).stream()
    doc_list = []

    for doc in docs:
        doc_dict = {"id": doc.id, "fields": doc.to_dict()}

        if depth < max_depth:
            subcollections = doc.reference.collections()
            nested_docs = {}
            for subcol in subcollections:
                subcol_docs = educoder_fetch(subcol.id, parent_path=f"{full_path}/{doc.id}", depth=depth + 1, max_depth=max_depth)
                if subcol_docs:
                    nested_docs[subcol.id] = subcol_docs
            if nested_docs:
                doc_dict['nested'] = nested_docs

        doc_list.append(doc_dict)

    return doc_list

def educoder_fetch_exam_solutions(filepath: str, student: str = "", save: bool = False):
    blobs = list(bucket.list_blobs(prefix=filepath))
    if len(blobs) < 1: 
        return f"No files found in {filepath}"

    solutions = []

    for blob in blobs:
        if blob.name.endswith('placeholder.txt') or not blob.name.endswith('.json'):
            continue

        if student:
            student_file = f"{student}.json"
            if blob.name.endswith(student_file):
                print(f"Loaded: {blob.name}")
                if save:
                    save_blob(blob)
                else:
                    return blob.download_as_text()
                break
        else:
            if save:
                save_blob(blob)
            else:
                solutions.append(blob.download_as_text())

    if student:
        return "No matching files found for the specified student."
    else: return solutions

def save_blob(blob):
    """
    Helper function to save the blob to the local filesystem.
    """
    path = blob.name.replace('/', os.sep)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    blob.download_to_filename(path)
    print(f" Saved: {path}")


def print_json(data):
    """
    Prints the provided data in a JSON-readable format.
    """
    print(json.dumps(data, indent=4, sort_keys=True))

    