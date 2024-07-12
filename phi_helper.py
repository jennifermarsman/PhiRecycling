from PIL import Image
import requests
import torch
from transformers import AutoModelForCausalLM
from transformers import AutoProcessor

model_id = "microsoft/Phi-3-vision-128k-instruct"

kwargs = {}
kwargs['torch_dtype'] = torch.bfloat16

processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, torch_dtype="auto", _attn_implementation='eager').cuda() # use _attn_implementation='eager' to disable flash attention

user_prompt = '<|user|>\n'
assistant_prompt = '<|assistant|>\n'
prompt_suffix = "<|end|>\n"


def call_with_single_online_image(image_url, input_prompt):
    prompt = f"{user_prompt}<|image_1|>\n{input_prompt}{prompt_suffix}{assistant_prompt}"

    image = Image.open(requests.get(image_url, stream=True).raw)

    inputs = processor(prompt, image, return_tensors="pt").to("cuda:0")
    
    generate_ids = model.generate(**inputs, 
                                max_new_tokens=1000,
                                eos_token_id=processor.tokenizer.eos_token_id,
                                )
    
    generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

    response = processor.batch_decode(generate_ids, 
                                    skip_special_tokens=True, 
                                    clean_up_tokenization_spaces=False)[0]
    return response


def call_with_single_local_image(imagePath, input_prompt):
    prompt = f"{user_prompt}<|image_1|>\n{input_prompt}{prompt_suffix}{assistant_prompt}"

    image = Image.open(imagePath, 'r')

    inputs = processor(prompt, image, return_tensors="pt").to("cuda:0")
    
    generate_ids = model.generate(**inputs, 
                                max_new_tokens=100,
                                eos_token_id=processor.tokenizer.eos_token_id,
                                )
    
    generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

    response = processor.batch_decode(generate_ids, 
                                    skip_special_tokens=True, 
                                    clean_up_tokenization_spaces=False)[0]
    return response
