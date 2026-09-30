from agents.base_agent import BaseAgent

class PoAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Product Owner", 
            goal="Define and prioritize product features and requirements and create the user stories."
        )

    def execute(self, task) -> str: 
        story = super().execute(task)
        path = self.saveToFile(story, "UserStories", "story")
        return path

    # def saveStory(self, story_text) -> str:
    #     os.makedirs("UserStories", exist_ok=True)
    #     story_id = uuid.uuid4()
    #     id_str = str(story_id)
    #     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #     filename = f"story_{id_str}_{timestamp}.txt"
    #     path = os.path.join("UserStories", filename)
    #     print(story_text)
    #     with open(path, "w", encoding="utf-8") as f:
    #         f.write(f"ID: {id_str}. Timestamp: {timestamp}\n")
    #         f.write(f"{story_text}\n")
    #     return path
