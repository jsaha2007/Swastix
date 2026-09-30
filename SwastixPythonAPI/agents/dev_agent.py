from agents.base_agent import BaseAgent

class DevAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Developer", 
            goal="""You are a backend developer working with FastAPI, SQLAlchemy 2.0, and PostgreSQL.
Read the given user story and implement the corresponding code.
Maintain SOLID Principals how much we can. Follow repository pattern for database connection. 
The code flow should be Repository -> Service -> Controller and vice-versa.
Only output the code — no explanations, no markdown formatting, no extra text."""
        )

    def execute(self, story_file_path):
        with open(story_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        code = super().execute(content)
        path = self.saveToFile(code, "Code", "code")
        return path

    # def saveCode(self, story_text) -> str:
    #     os.makedirs("Code", exist_ok=True)
    #     story_id = uuid.uuid4()
    #     id_str = str(story_id)
    #     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #     filename = f"code_{id_str}_{timestamp}.txt"
    #     path = os.path.join("Code", filename)
    #     print(story_text)
    #     with open(path, "w", encoding="utf-8") as f:
    #         f.write(f"ID: {id_str}. Timestamp: {timestamp}\n")
    #         f.write(f"{story_text}\n")
    #     return path







