from openai import OpenAI, AsyncOpenAI
import asyncio
import json
import os
import dotenv
from helpers.file_operations import export_dict_to_csv

dotenv.load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

async def call_evaluator(instructions, tasks_text, student_code, student_email, exam_password):
    prompt = f"{instructions}\n\n###{tasks_text}\n\n### Student's Code:\n{student_code}\n\n### Evaluation:\nPlease return a structured response with the following format: '{{\"task_1\": \"task_1_points\", \"task_2\": \"task_2_points\", \"total_points\": \"total_points_here\", \"feedback\": \"feedback_here\"}}'. Please provide task points for each task. Provide task_x: 0 for task with with no solution ([NOT_SOLVED])."

    json_response = {}
    json_response['student_email'] = student_email
    json_response['exam_password'] = exam_password

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You're a professor grading JavaScript exams of first-year students designed to output JSON structured responses."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    total_tokens = prompt_tokens + completion_tokens

    price_per_prompt_token = 0.01
    price_per_completion_token = 0.03

    total_cost = (prompt_tokens / 1000 * price_per_prompt_token) + (completion_tokens / 1000 * price_per_completion_token)

    json_response['prompt_tokens'] = prompt_tokens
    json_response['completion_tokens'] = completion_tokens
    json_response['total_tokens'] = total_tokens
    json_response['total_cost'] = total_cost

    response_data = json.loads(response.choices[0].message.content) 
    json_response.update(response_data) 
    
    output_dir = f"results/{exam_password}/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    return json_response