from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Document
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
import json

class JobIndex:
    def _init_(self, data_path="job_data.json"):
        self.data_path = data_path
        self.index = self.load_index()

    def load_index(self):
        with open(self.data_path, "r") as f:
            job_list = json.load(f)
        documents = [
            Document(
                text=f"{job['title']} at {job['company']} in {job['location']}.\n{job['description']}",
                metadata=job,
            )
            for job in job_list
        ]
        return VectorStoreIndex.from_documents(documents)

    def query_jobs(self, prompt):
        query_engine = self.index.as_query_engine()
        response = query_engine.query(prompt)
        return str(response)