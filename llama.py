""" 
JSON Import used to process config file 
llama_cpp used to use AI model
"""
import json
from llama_cpp import Llama

f = open("config.json", encoding="utf-8")
config = json.load(f)
llm_config = config["llm_config"]
chat_config = config["chat_config"]

def create_llm(model_path=llm_config["model_id"],
            n_gpu_layers=llm_config["n_gpu_layers"], n_ctx=llm_config["n_ctx"]):
    """Creates and returns LLM.
    
    Args:
        model_path (str): Path to model to be used as a GGUF file.
        n_gpu_layers (int): How many layers of the model are offloaded to the GPU.
        n_ctx (int): Maximum number of tokens that the model can account for when 
            processing a response.

    Returns:
        LLama Function: Usable LLM
    """
    llm = Llama(
      model_path=model_path,
      n_gpu_layers=n_gpu_layers,
      n_ctx=n_ctx,
    )
    return llm

def generate_output(question, llm, chat_template=chat_config["chat_template"],
            max_tokens=chat_config["max_tokens"], stop_conditions=chat_config["stop_conditions"]):
    """Returns a response to the inputted question using the inputted LLM.

    Args:
        question (string): Qestion to be asked to the model.
        llm: Model to be used when generating response.
        max_tokens (int): Max tokens to be used when generating response.
        stop_conditions (list): Condition for response to stop generating.
        include_question (bool): If to include question in returned response.

    Returns:
        string: Response to inputted question.
    """

    output = llm.create_chat_completion(
      messages = [
          {"role" : "system", "content" : chat_template},
          {"role" : "user", "content" : question}
          ],
      max_tokens=max_tokens,
      stop=stop_conditions,
    )

    return output['choices'][0]['message']['content']
