# Fully functional chatbot with RAG vector search of set local directory.
## llama 3 for llm, huggingface transformer/aws titan text embedding v2 for embedding

## Initial setup:
### Install python3: https://www.python.org/downloads/
### Install Node.js: https://nodejs.org/en/download/package-manager

Then run the following to set up the react app:
```
cd rag-frontend
npm install
```


## Directions to setup chatbot:
### navigate back to local-rag-chatbot (ex. bryanzeng@Bryans-MacBook-Pro-2 local-rag-chatbot % )
### Setup langchain, Chroma, pyPDF:
```
pip install langchain
pip install chroma
pip install pypdf
```
### For the embedding function, choose either AWS Bedrock (default) or Huggingface. 
#### In get_embedding_function.py:
```
def get_embedding_function():
    return BedrockEmbeddings() #default is using titan embed text v2, which is more accurate, replace with the following code to run Huggingface model instead:
    #return HuggingFaceEmbeddings()

```

#### For running Huggingface, run the following
```
pip install transformers
pip install torch
```
#### If using AWS Bedrock, which is the default method, first navigate to an AWS user account (must be IAM user so can generate access keys and access through AWS CLI later).
#### Recommend to use US east 1 or US west 2 as the region.
#### Navigate to the AWS console, and search up Bedrock. On the left hand panel, find model access. Request access to Amazon Titan Text Embeddings v2.
#### Now to set up CLI, navigate to IAM. On the left hand panel, navigate to users. Choose the desired user, and create an access key, or use an existing one.
#### Navigate to the project terminal (ex. bryanzeng@Bryans-MacBook-Pro-2 local-rag-chatbot % ), and run the following:
```
pip install boto3
pip install awscli
aws configure
```
#### enter your access and secret access key as prompted, set default region to your region, and default format to json.
#### for a more complete tutorial on bedrock, here is a good one: https://www.youtube.com/watch?v=2TJxpyO3ei4

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

## Start flask server by running app.py, then in a new terminal run
```
cd rag-frontend
npm start
```
## How to Use:
### Data directory: set data directory upon first launch, will be saved as default upon further launches, update directory as needed.
### Update database: Upon setting a new directory, click the reset button and update database. This effectively clears the vector database and reconstructs it. If you have added a file to the current directory, do not click reset button, simply run update database to add the new file to the database.
