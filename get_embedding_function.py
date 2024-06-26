from transformers import AutoTokenizer, AutoModel
import torch
import boto3
import json

'''bedrock = boto3.client(
   service_name = 'bedrock-runtime',
   region_name = 'us-east-1'
)
prompt = "dc is the capital of US"
body = json.dumps({
    "inputText": prompt,
})

model_id = "amazon.titan-embed-text-v2:0"
accept = "application/json"
content_type = "application/json"

response = bedrock.invoke_model(
    body = body,
    modelId = model_id,
    accept = accept,
    contentType = content_type,
)

response_body = json.loads(response['body'].read())
embedding = response_body.get('embedding')
print(embedding)'''

class BedrockEmbeddings:
    def __init__(self, model_id="amazon.titan-embed-text-v2:0", region_name="us-east-1"):
        self.model_id = model_id
        self.bedrock = boto3.client('bedrock-runtime', region_name=region_name)

    def embed_text(self, text):
        body = json.dumps({"inputText": text})
        response = self.bedrock.invoke_model(
            body=body,
            modelId=self.model_id,
            accept="application/json",
            contentType="application/json"
        )
        response_body = json.loads(response['body'].read())
        embedding = response_body.get('embedding')
        return embedding

    def embed_query(self, query):
        return self.embed_text(query)

    def embed_documents(self, texts):
        embeddings = []
        for text in texts:
            embedding = self.embed_text(text)
            embeddings.append(embedding)
        return embeddings

#use aws bedrock for more accurate embeddings
#from langchain_community.embeddings.bedrock import BedrockEmbeddings


#def get_embedding_function():
#    embeddings = BedrockEmbeddings(
#        credentials_profile_name="default", region_name="us-east-1"
#    )
#    return embeddings

#embedding function for RAG vecotrization - huggingface transformers

class HuggingFaceEmbeddings:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def embed_text(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        # Get the embedding as a numpy ndarray
        embedding = outputs.last_hidden_state.mean(dim=1).numpy()
        # Convert the embedding ndarray to a list and flatten it
        embedding_list = embedding[0].tolist()
        return embedding_list  # Return the embedding as a single list

    def embed_query(self, query):
        return self.embed_text(query)

    def embed_documents(self, texts):
        embeddings = []
        for text in texts:
            embedding = self.embed_text(text)
            embeddings.append(embedding)  # Append the unflattened embedding
        return embeddings


def get_embedding_function():
    return BedrockEmbeddings()
