# Llama Chat App

## This Chat App was made using the *Llama 3 8b Instruct* and the *Llama-CPP-Python* library along with *Flask* for the webpage

### Model Installation

This program is designed to work with any quantized version of *Llama 3 8b Instruct*. They can be found [here](https://huggingface.co/QuantFactory/Meta-Llama-3-8B-Instruct-GGUF/tree/main). The default model is named *'Meta-Llama-3-8B-Instruct.Q6_K.gguf'*. Once a *GGUF* file is downloaded it has to be put in this directory with all the other files. If the downloaded file is not the default file `model_id` needs to be changed in *config.json*.

### Package Installation

This program requires *flask* and *llama-cpp-python*. Pip will be required to install these modules but once you have that *install.bat* can be run.

### Chatbot Configuration

This chatbot can be fully conifgured using the *config.json* file. See below for an explanation of all the variables that can be adjusted.

## Adjustable Variables

1.**model_id:** Name of model file being used, see **Model Installation** for details.
2.**n_gpu_layers:**  Number of layers of the model being offloaded to the GPU.
3.**n_ctx:** Maximum number of tokens that the model can account for when processing a response.
4.**chat_template:** Template dictating how the chat bot will talk. **A bad chat template can mess up the chtabot completely.**
5.**max_tokens:** Max tokens to be used when generating response. Leave at `null` for no cap. **Setting a value for this that is too low can cause the bot to cut off.**
6.**stop_conditions:** String conditions that cause the bot to stop it's message. **The bot will still stop if it has nothing else to say.**
