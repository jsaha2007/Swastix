from agents.base_agent import BaseAgent

class DataPreparerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Data Preparer", 
            goal="""You are a data preparer. You will be given a user story and you need to prepare the data for it.
            The data should be prepared in a way that it can be used for testing the code generated from the user story.
            The data should be prepared in a separate file named data_<original_file_name>.py
            Only output the code — no explanations, no markdown formatting, no extra text."""
        )
    def execute(self, story_file_path):
        with open(story_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        data_code = super().execute(content)
        path = self.saveToFile(data_code, "Data", "data_code")
        return path