from openai import AsyncOpenAI

import asyncio
import instructor
from pydantic import BaseModel
from pydantic import NonNegativeFloat 
import json
import os
import dotenv

dotenv.load_dotenv()

aclient = instructor.apatch(AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY")))

class Solution(BaseModel):
    task_1: NonNegativeFloat 
    task_2: NonNegativeFloat 
    task_3: NonNegativeFloat 
    task_4: NonNegativeFloat 
    task_5: NonNegativeFloat 
    feedback: str

# gpt-4-turbo-preview
PRICE_PER_PROMPT_TOKEN = 0.01
PRICE_PER_COMPLETION_TOKEN = 0.03

async def call_evaluator(instructions, tasks_text, student_code, student_email, exam_password):
    prompt = f"{instructions}\n\n###{tasks_text}\n\n### Student's Code:\n{student_code}\n\n### Evaluation: Please provide task points for each task, but no more than MAX_TASK_POINTS. For task with no solution provided give 0 points."

    json_response = {}
    json_response['student_email'] = student_email
    json_response['exam_password'] = exam_password

    response = await aclient.chat.completions.create(
        model="gpt-4-turbo-preview",
        response_model = Solution,
        messages=[
            {"role": "system", "content": "You're a professor grading JavaScript exams of first-year IT students. First work out your own solution to the problem. Then compare your solution to the student's solution and evaluate if the student's solution is correct or not. Don't decide if the student's solution is correct until you have done the problem yourself. After you finish evaluating, give short general feedback in Croatian language of your evaluation for each student solution for given task. The feedback should be structured like: 'Zadatak 1: feedback of task 1. Zadatak 2: feedback of task 2. Zadatak 3: feedback of task 3.' etc."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
    )
    
    total_points = sum(value for key, value in response.model_dump().items() if key != 'feedback')
    
    raw_response = response._raw_response

    usage_data = raw_response.usage

    prompt_tokens = usage_data.prompt_tokens
    completion_tokens = usage_data.completion_tokens
    total_tokens = usage_data.total_tokens

    total_cost = (prompt_tokens / 1000 * PRICE_PER_PROMPT_TOKEN) + (completion_tokens / 1000 * PRICE_PER_COMPLETION_TOKEN)

    json_response['prompt_tokens'] = prompt_tokens
    json_response['completion_tokens'] = completion_tokens
    json_response['total_tokens'] = total_tokens
    json_response['total_cost'] = total_cost
    
    for i in range(1, 6):
        task_key = f'task_{i}'
        json_response[task_key] = getattr(response, task_key)
    
    json_response['total_points'] = total_points
    json_response['feedback'] = response.feedback
    
    output_dir = f"results/{exam_password}/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    return json_response
