from flask import Blueprint, request, jsonify

import openai
import os
from random import choice

openai.api_key = os.environ.get("OPENAI_API_KEY")


openai_bp = Blueprint('openai', __name__, url_prefix='/openai')


suffix = [
    'pixel art',
    'digital art',
    # 'one-line drawing',
    # 'synthwave',
    # 'by Picasso'
]


@openai_bp.post('/description')
def generate_description():
    print(request.json)
    description = 'hello'
    
    repository_url = request.json['githubURL']
    
    prompt = f"Give a short description of the following github repository: {repository_url}. Don't mention the github repository in the description"
    #  or start the description with the word 'This'.
    
    try:
        # response = openai.Completion.create(
		# 	model='text-davinci-003',
		# 	prompt=prompt,
		# 	temperature=0.6,
		# 	max_tokens=1024
		# )
        
        # description = response.choices[0].text
        # description = description.strip()
        description = get_chatgpt_response(prompt)
        
        return jsonify(description=description), 200 # OK
    
    except Exception as err:
        print(err)
        return jsonify(message=err), 500 # Internal Server Error



@openai_bp.post('/image')
def generate_image():
    # print(request.json)
    
    github_url = request.json.get('githubURL')

    chat_gpt_response = get_chatgpt_response(f"Summarize the following repository in one word: {github_url}")
    # chat_gpt_response = get_chatgpt_response(f"In one sentence, describe the contents of a picture that represents the following github repository: {github_url}. Don't say 'The picture depicts' or 'In this picture' or make any mention of the picture itself.")
    
    print('ChatGPT response: ', chat_gpt_response)

    image_prompt = f"An abstract illustration of {chat_gpt_response}, digital art"
    # image_prompt = f"{chat_gpt_response}, digital art"

    print(image_prompt)
    
    try:
        response = openai.Image.create(
			prompt=image_prompt,
			n=1,
			size="512x512",
			response_format="b64_json"
		)
        
        image = response.data[0]['b64_json']
        
        return jsonify(message='Image generated', image=image), 200 # OK
        
    except Exception as err:
        print(err)
        return jsonify(message=err), 500 # Internal Server Error
    
    
    # return {}
    

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=0.6,
        max_tokens=1024
    )
    
    return response.choices[0].text.strip()
    
    


# @openai_bp.post('/tags')
# def generate_tags():
#     print(request.json)
#     description = 'hello'
    
#     repository_url = request.json['githubURL']
    
#     prompt = f'What are the primary web technologies used by the following github repository: #{repository_url}'
    
#     response = openai.Completion.create(
# 		model='text-davinci-003',
# 		prompt=prompt,
# 		temperature=0.6,
# 		max_tokens=1024
# 	)
    
#     description = response.choices[0].text
    
#     return jsonify(description=description), 200