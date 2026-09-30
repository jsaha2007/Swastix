from agents.base_agent import BaseAgent

class CodeReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Code Reviewer", 
            goal="""You are a code reviewer. Your task is to check code quality, correctness, adherence to SOLID/repository pattern, 
            find bugs, suggest fixes. 
            List all the findings in a list and say no issues found if clean"""
        )

    def execute(self, code_file_path):
        with open(code_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        review = super().execute(content)
        path = self.saveToFile(review, "CodeReviews", "review_code")
        return path