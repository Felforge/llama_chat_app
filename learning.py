from llama_cpp import Llama

llm = Llama(
      model_path="Meta-Llama-3-8B-Instruct-Q6_K.gguf",
      n_gpu_layers=30, # Uncomment to use GPU acceleration
      n_ctx=2048, # Uncomment to increase the context window
      # seed=1337, # Uncomment to set a specific seed
)
output = llm(
      "Q: How do I make a pizza? A: ", # Prompt
      max_tokens=None, # Generate up to 32 tokens, set to None to generate up to the end of the context window
      # stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
      stop=["Q:"],
      echo=False, # Echo the prompt back in the output
) # Generate a completion, can also call create_completion

# Example Format:
# {
#   "id": "cmpl-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "object": "text_completion",
#   "created": 1679561337,
#   "model": "./models/7B/llama-model.gguf",
#   "choices": [
#     {
#       "text": "Q: Name the planets in the solar system? A: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune and Pluto.",
#       "index": 0,
#       "logprobs": None,
#       "finish_reason": "stop"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 14,
#     "completion_tokens": 28,
#     "total_tokens": 42
#   }
# }

def get_answer(llm_output):
    """_summary_

    Args:
        llm_output (dict): All data from output in OpenAI format

    Returns:
        string: Answer to given question
    """
    text = llm_output["choices"][0]["text"]
    if text[:1] == "Q:":
        for i, _ in enumerate(text):
            if text[i] + text[i + 1] == "A:":
                return text[i + 3:]
    else:
        return text

print(get_answer(output))
