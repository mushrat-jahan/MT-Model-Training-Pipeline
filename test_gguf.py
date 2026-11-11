# from llama_cpp import Llama

# llm = Llama(
#     model_path="output/model_gguf/gemma-4-e2b-it.Q4_K_M.gguf",
#     verbose=False,
# )

# response = llm.create_chat_completion(
#     messages=[
#         {
#             "role": "user",
#             "content": "Translate English to Bangla: The cat is on the table."
#         }
#     ],
#     max_tokens=100,
# )

# print(response["choices"][0]["message"]["content"])

# from llama_cpp import Llama

# llm = Llama(
#     model_path="output/model_gguf/gemma-4-e2b-it.Q4_K_M.gguf",
#     verbose=False,
# )

# print(llm.metadata)


# from llama_cpp import Llama

# llm = Llama(
#     model_path="output/model_gguf/gemma-4-e2b-it.Q4_K_M.gguf",
#     verbose=False,
# )

# response = llm(
#     "The capital of Bangladesh is",
#     max_tokens=20,
#     temperature=0,
# )

# print(response)


import json

with open(
    "/home/mushrat/MT-model-training-pipeline/MT-Model-Training-Pipeline/output/lora/adapter_config.json"
) as f:
    config = json.load(f)

print("Base model:", config["base_model_name_or_path"])
print("LoRA rank:", config["r"])
print("LoRA alpha:", config["lora_alpha"])
print("Target modules:", config["target_modules"])
