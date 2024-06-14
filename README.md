# Fully functional chatbot with RAG vector search of set local directory.
## llama 3 for llm, huggingface transformer/aws titan text embedding v2 for embedding




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
#### Feel free to change the model in query_data.py, simply run the model in terminal for ollama (ex. for mistral: ollama run mistral)

## Start flask server by running app.py, then cd rag_frontend and npm start.

## How to Use:
### Data directory: set data directory upon first launch, will be saved as default upon further launches, update directory as needed.
### Update database: Upon setting a new directory, click the reset button and update database. This effectively clears the vector database and reconstructs it. If you have added a file to the current directory, do not click reset button, simply run update database to add the new file to the database.
