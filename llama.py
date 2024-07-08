""" Module provides a way to process AI models in the GGUF format """
from llama_cpp import Llama

DEFAULT_TEMPLATE = "You are are a helpful Assistant, and you only response to the \"Assistant\" remember, maintain a natural tone. Be precise, concise, and casual. Keep it short."

def create_llm(model_path="Meta-Llama-3-8B-Instruct-Q6_K.gguf", n_gpu_layers=30, n_ctx=2048):
    """Creates and returns LLM.
    
    Args:
        model_path (str, optional): Path to model to be used as a GGUF file. Defaults to "Meta-Llama-3-8B-Instruct-Q6_K.gguf".
        n_gpu_layers (int, optional): How many layers of the model are offloaded to the GPU. Defaults to 30.
        n_ctx (int, optional): Maximum number of tokens that the model can account for when processing a response. Defaults to 2048.

    Returns:
        LLama Function: Usable LLM
    """
    llm = Llama(
      model_path=model_path,
      n_gpu_layers=n_gpu_layers,
      n_ctx=n_ctx,
      prompt="You are are a helpful Assistant, and you only response to the \"Assistant\" remember, maintain a natural tone. Be precise, concise, and casual. Keep it short.",
    )
    return llm

def generate_output(question, llm, chat_template=DEFAULT_TEMPLATE, max_tokens=None, stop_conditions=["Q:"]):
    """Returns a response to the inputted question using the inputted LLM.

    Args:
        question (string): Qestion to be asked to the model.
        llm: Model to be used when generating response.
        max_tokens (int, optional): Max tokens to be used when generating response. Defaults to None.
        stop_conditions (list, optional): Condition for response to stop generating. Defaults to ["Q:"].
        include_question (bool, optional): If to include question in returned response. Defaults to False.

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
