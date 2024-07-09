# Llama Chat App

## This Chat App was made using a quantized version of *Llama 3 8b Instruct* and the *Llama-CPP-Python* Library

### Additional Installation Requirements

**Model Installation:** This program is designed to work with any quantized version of *Llama 3 8b Instruct*. They can be found [here](https://huggingface.co/QuantFactory/Meta-Llama-3-8B-Instruct-GGUF/tree/main). The default model is named *'Meta-Llama-3-8B-Instruct.Q6_K.gguf'*. Once a *GGUF* file is downloaded it has to be put in this directory with all the other files. If the downloaded file is not the default file `model_id` needs to be changed in *config.json*

**Package Installation:** This program requires *flask* and *llama-cpp-python*. Pip will be required to install these modules but once you have that *install.bat* can be run.

**Chatbot Configuration:** This chatbot can be fully conifgured using the *config.json* file. See below for an explanation of all the variables that can be adjusted.
