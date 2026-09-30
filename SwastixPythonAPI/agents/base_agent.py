from langchain_groq import ChatGroq
from dotenv import load_dotenv
from datetime import datetime
import uuid
import os

class BaseAgent:
    def __init__(self, role: str, goal: str):
        load_dotenv()
        self.role = role
        self.goal = goal
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="openai/gpt-oss-120b"
        )

    def execute(self, task: str) -> str:
        prompt = f"You are a {self.role}. Your goal is {self.goal}. Task: {task}"
        response = self.llm.invoke(prompt)
        return response.content

    def saveToFile(self, text, parent_folder, file_name_prefix) -> str:
        os.makedirs(parent_folder, exist_ok=True)
        story_id = uuid.uuid4()
        id_str = str(story_id)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{file_name_prefix}_{id_str}_{timestamp}.txt"
        path = os.path.join(parent_folder, filename)
        print(text)
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"ID: {id_str}. Timestamp: {timestamp}\n")
            f.write(f"{text}\n")
        return path