from agents.base_agent import BaseAgent
from agents.base_agent import BaseAgent
import os

class CodeReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Code Reviewer", 
            goal="""You are a code reviewer. Your task is to check code quality, correctness, adherence to SOLID/repository pattern, 
            find bugs, suggest fixes. 
            List all the findings in a list and say no issues found if clean"""
        )

    def execute(self, code_package):
        code_contents = []
        for code_file_path in code_package["files"]:
            with open(code_file_path, "r", encoding="utf-8") as f:
                relative_path = os.path.relpath(code_file_path, code_package["directory"])
                code_contents.append(f"File: {relative_path}\n{f.read()}")

        content = "\n\n".join(code_contents)
        review = super().execute(content)
        path = self.saveToFile(review, "CodeReviews", "review_code")
        return path