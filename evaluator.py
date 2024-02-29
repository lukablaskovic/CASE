from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)
def evaluate_student_submission(instructions, exam_instructions, student_code, student_email, exam_code):
    """
    Evaluates a student's code submission and returns a structured evaluation including total points.

    Parameters:
    - student_code (str): The student's code submission as a string.
    - instructions (str): The instructions or criteria for evaluating the submission.
    - exam_instructions (str): The instructions defined in the exam text.
    - student_email (str): The student's email.
    - exam_name (str): The name (code) of the exam.

    Returns:
    - dict: The evaluation result including total points.
    """

    # Format the prompt to include instructions, student's code, and ask for a structured response
    prompt = f"{instructions}\n\n###{exam_instructions}\n\n### Student's Code:\n{student_code}\n\n### Evaluation:\nPlease return a structured response with the following format: '{{\"student_email\": \"{student_email}\", \"exam_name\": \"{exam_code}\", \"total_points\": \"total_points_here\", \"feedback\": \"feedback_here\"}}'."

    stream  = client.chat.completions.create(
        model= "gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        stream=True
    )

    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")

# Example usage
if __name__ == "__main__":
    student_code = """
def add_numbers(a, b):
    return a + b
"""

    instructions = """
    You're a professor grading JavaScript exams for first-year students with a C++ background. Evaluate their code based on correctness, partial correctness (like semi-correct logic or syntax errors), and effort (like pseudocode). 
    Ignore variable naming, spacing, encoding errors (č, ć, š, đ), and unmentioned edge cases. Assign points (up to 10 total, with possible .5 increments) and provide feedback in Croatian in 2 sentence maximum for each task only. Do not provide general feedback.

    Instructions:
    Assign points for each task, ensuring the total doesn't exceed 10.
    Use whole numbers or .5 increments for points.
    """
    
    exam_instructions = """
    **1.** Napišite funkciju `hipotenuza(duzinaA, duzinaB)` koja prima dužine dvije katete pravokutnog trokuta. Funkcija treba izračunati i vratiti dužinu hipotenuze primjenjujući Pitagorin poučak, koji glasi: `c=√(a²+b²)`, gdje su `a` i `b` dužine kateta, a `c` dužina hipotenuze. Ispiši rezultat u formatu `"Dužina hipotenuze je: [hipotenuza]"`. Za implementaciju koristite metode iz `Math` objekta. MAX_EXERCISE_POINTS=5
    **2.** Napišite funkciju proizvoljnog naziva koja prima broj `n`. Funkcija provjerava je li `n` broj, ako nije vraća poruku `"Nije broj!"`. Ako je broj, funkcija vraća 10 brojeva većih od `n` u formatu: `"Broj 1: [n+1], Broj 2: [n+2], ..., Broj 10: [n+10]"`. Ako su `[Broj 1 - Broj 10]` decimalni brojevi, zaokružite ih na dvije decimale i ispišite ih u tom formatu u konzolu. Ako su `[Broj 1 - Broj 10]` cijeli brojevi, pretvorite ih u binarni oblik i ispišite u konzolu. MAX_EXERCISE_POINTS=5
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
exam_code = "matematika"

evaluation = evaluate_student_submission(student_code, instructions, exam_instructions, student_email, exam_code)
