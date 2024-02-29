from helpers import normalize_line_endings
with open('code.txt', 'r') as file:
    content = file.read()
    normalized_content = normalize_line_endings(content)
    print("content\n", content)
    print("normalized_content\n", normalized_content)
    
