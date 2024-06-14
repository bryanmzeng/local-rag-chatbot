# Fully functional chatbot with RAG vector search of set local directory.
## llama 3 for llm, huggingface transformer/aws titan text embedding v2 for embedding

## Initial setup:
### Install python3: https://www.python.org/downloads/
### Install Node.js: https://nodejs.org/en/download/package-manager


## Directions to run:
### Setup langchain, Chroma, pyPDF:
```
pip install langchain
pip install chroma
pip install pypdf
```
### For embedding_function.py, choose either AWS Bedrock or Huggingface. 
#### For running Huggingface, run pip install transformers
#### If using AWS Bedrock, first pip install awscli and run aws configure to set up AWS CLI.

## To run llama3 locally
### Download Ollama: https://ollama.com/
### Run in terminal: ollama run llama3
#### Feel free to change the model in query_data.py, simply run the model in terminal for ollama (ex. for mistral: ollama run mistral). Browse additional models here: https://ollama.com/library
#### In query_data.py, the query_rag function:
```
model = Ollama(model="llama3") #feel free to change this model
response_text = model.invoke(prompt)
```
##### Note: Consider that the LLM is running locally, high performing models might take more time to run depending on the performance of your computer/workstation.

## Start flask server by running app.py, then cd rag-frontend and `npm` start.

## How to Use:
### Data directory: set data directory upon first launch, will be saved as default upon further launches, update directory as needed.
### Update database: Upon setting a new directory, click the reset button and update database. This effectively clears the vector database and reconstructs it. If you have added a file to the current directory, do not click reset button, simply run update database to add the new file to the database.
