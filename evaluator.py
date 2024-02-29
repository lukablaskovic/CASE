from openai import OpenAI, AsyncOpenAI
import asyncio
import json
import os
import dotenv
from helpers.file_operations import export_dict_to_csv, read_file_content

dotenv.load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def evaluate(instructions, tasks_text, student_code, student_email, exam_password):
    prompt = f"{instructions}\n\n###{tasks_text}\n\n### Student's Code:\n{student_code}\n\n### Evaluation:\nPlease return a structured response with the following format: '{{\"task_1\": \"task_1_points\", \"task_2\": \"task_2_points\", \"total_points\": \"total_points_here\", \"feedback\": \"feedback_here\"}}'. Please provide task points for each task."
    
    json_response = {}
    json_response['student_email'] = student_email
    json_response['exam_password'] = exam_password
    
    """
    response  = await client.chat.completions.create(
        model= "gpt-4-turbo-preview",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You're a professor grading JavaScript exams of first-year students designed to output JSON structured responses."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )
    """
    
    response_data = {'student_email': 'lblaskovi@student.unipu.hr', 'exam_password': 'matematika', 'task_1': '5', 'task_2': '4.5', 'total_points': '9.5', 'feedback': 'ZADATAK 1: Funkcija ispravno implementira Pitagorin poučak i vraća očekivani rezultat. ZADATAK 2: Funkcija ispravno provjerava je li ulaz broj i vraća 10 brojeva većih od n, ali nije specificirano kako se ispisuju brojevi u binarnom obliku ili zaokruženi na dvije decimale u konzolu.'}
    
    output_file = f"results/{exam_password}/{student_email}.csv"
    
    #response_data = json.loads(response.choices[0].message.content) 
    json_response.update(response_data) 
    
    export_dict_to_csv(json_response, output_file)
    
    return json_response

instructions = read_file_content("instructions.txt")

print("instructions", instructions)

tasks_text = """
Tasks are as follows:
**1.** Napišite funkciju `hipotenuza(duzinaA, duzinaB)` koja prima dužine dvije katete pravokutnog trokuta. Funkcija treba izračunati i vratiti dužinu hipotenuze primjenjujući Pitagorin poučak, koji glasi: `c=√(a²+b²)`, gdje su `a` i `b` dužine kateta, a `c` dužina hipotenuze. Ispiši rezultat u formatu `"Dužina hipotenuze je: [hipotenuza]"`. Za implementaciju koristite metode iz `Math` objekta. MAX_TASK_POINTS=5
**2.** Napišite funkciju proizvoljnog naziva koja prima broj `n`. Funkcija provjerava je li `n` broj, ako nije vraća poruku `"Nije broj!"`. Ako je broj, funkcija vraća 10 brojeva većih od `n` u formatu: `"Broj 1: [n+1], Broj 2: [n+2], ..., Broj 10: [n+10]"`. Ako su `[Broj 1 - Broj 10]` decimalni brojevi, zaokružite ih na dvije decimale i ispišite ih u tom formatu u konzolu. Ako su `[Broj 1 - Broj 10]` cijeli brojevi, pretvorite ih u binarni oblik i ispišite u konzolu. MAX_TASK_POINTS=5
"""

student_code = """
#ZADATAK_1
  <script>
function hipotenuza(a, b) {
let c = Math.sqrt(Math.pow(a,2)+Math.pow(b,2))
return `Dužina hipotenuze je: ${c}`
}
console.log(hipotenuza(3, 4));
</script>
#ZADATAK_2
function fun(n) {
if (typeof(n) != 'number') { return "Nije broj!"}
else {
  let sum = ""
  for (let i = n+1; i<=n+10;i++) {
    if (Number.isInteger(i)){
      sum+=i.toString(2)
    }
    else {
      sum+=i.toFixed(2)
    }
    if (i!=n+10) {
      sum+=", "
    }
  }
  return sum;
}
}

console.log(fun(5));

console.log(fun(5.5));
  """
    
student_email = "lblaskovi@student.unipu.hr"
exam_password = "matematika"

evaluation = evaluate(instructions=instructions, tasks_text=tasks_text, student_code=student_code, student_email=student_email, exam_password=exam_password)

print("RESULT:", evaluation)