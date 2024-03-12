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

ADMINS = ["lblaskovi@student.unipu.hr", "azuzic@student.unipu.hr", "ntankov@unipu.hr"]

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
    if len(blobs) < 2:  # 2 - because of the placeholder.txt file
        return f"No files found in {filepath}"

    solutions = []

    for blob in blobs:
        if blob.name.endswith('placeholder.txt') or not blob.name.endswith('.json'):
            continue
        
        # Admin files are not fetched by default
        is_admin_file = any(admin_email in blob.name for admin_email in ADMINS)
        if is_admin_file and not student:
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
    else:
        return solutions


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

def solutions_extracted(exam: str):
    exam_folder = f"exams/{exam}"
    """
    Checks if solutions have been extracted to the code folder inside the specified exam folder.
    
    :param exam_folder: The path to the exam folder where solutions are expected to be stored.
    :return: True if solutions have been extracted and found in the code folder, False otherwise.
    """
    code_folder = os.path.join(exam_folder, "code_solutions")
    return os.path.isdir(code_folder) and bool(os.listdir(code_folder))

def extract_code_from_solutions(exam_folder, js=True, html=False):
    
    if not os.listdir(exam_folder):
        return "The exam folder is empty. No code snippets to extract."
    
    code_folder = os.path.join(exam_folder, "code_solutions")
    os.makedirs(code_folder, exist_ok=True)

    for filename in os.listdir(exam_folder):
        filepath = os.path.join(exam_folder, filename)
        if os.path.isfile(filepath) and filename.endswith('.json'):
            with open(filepath, 'r', encoding="utf-8") as file:
                data = json.load(file)

            code_snippets = []

            for solution in data['examData']['exam_solutions']:
                snippet = {}
                if js and 'js_code' in solution:
                    snippet['js_code'] = solution['js_code'] if solution['js_code'].strip() else "[NOT_SOLVED]"
                if html and 'html_code' in solution:
                    snippet['html_code'] = solution['html_code'] if solution['html_code'].strip() else "[NOT_SOLVED]"

                if snippet:
                    code_snippets.append(snippet)

            if code_snippets:
                code_data = {
                    "code_snippets": code_snippets
                }

                prefix = "code"
                if js and not html:
                    prefix = "js_code"
                elif html and not js:
                    prefix = "html_code"
                elif js and html:
                    prefix = "js_html_code"

                new_filename = f"{prefix}_{filename}"
                new_filepath = os.path.join(code_folder, new_filename)
                with open(new_filepath, 'w', encoding="utf-8") as new_file:
                    json.dump(code_data, new_file, indent=4)

    return f"Code snippets have been extracted and saved in {code_folder}."
