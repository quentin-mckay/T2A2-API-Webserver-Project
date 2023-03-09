from flask import Blueprint, request, jsonify

import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")


openai_bp = Blueprint('openai', __name__, url_prefix='/openai')


@openai_bp.post('/description')
def generate_description():
    print(request.json)
    description = 'hello'
    
    repository_url = request.json['githubURL']
    
    prompt = f'Give a short description of the following github repository #{repository_url}.'
    
    response = openai.Completion.create(
		model='text-davinci-003',
		prompt=prompt,
		temperature=0.6,
		max_tokens=1024
	)
    
    description = response.choices[0].text
    description = description.strip()
    
    return jsonify(description=description), 200


@openai_bp.post('/tags')
def generate_tags():
    print(request.json)
    description = 'hello'
    
    repository_url = request.json['githubURL']
    
    prompt = f'What are the primary web technologies used by the following github repository: #{repository_url}'
    
    response = openai.Completion.create(
		model='text-davinci-003',
		prompt=prompt,
		temperature=0.6,
		max_tokens=1024
	)
    
    description = response.choices[0].text
    
    return jsonify(description=description), 200


@openai_bp.post('/image')
def generate_image():
    # print(request.json)
    
    # prompt = "A cute baby sea otter"
    prompt = "A neon soaked night scene in New York city"
    # prompt = request.json.get('githubURL')
    
    try:
        response = openai.Image.create(
			prompt=prompt,
			n=1,
			size="512x512",
			response_format="b64_json"
		)
    except Exception as err:
        print(err)
        return jsonify(message=err), 500
    
    
    image = response.data[0]['b64_json']
    
    return jsonify(message='Image generated', image=image), 200