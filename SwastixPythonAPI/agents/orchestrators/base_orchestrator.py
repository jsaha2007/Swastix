from agents.po_agent import PoAgent
from agents.dev_agent import DevAgent
from agents.code_reviewer_agent import CodeReviewerAgent
from agents.data_preparer_agent import DataPreparerAgent
from agents.qa_agent import QaAgent

class BaseOrchestrator:
    def __init__(self, domain_context: str):
        self.domain_context = domain_context
        self.po = PoAgent()
        self.dev = DevAgent()
        self.code_reviewer = CodeReviewerAgent()
        self.data_preparer = DataPreparerAgent()
        self.qa = QaAgent()

    def run(self, backlog_item: str) -> dict:
        full_task = f"{self.domain_context}\n\nBacklog Item: {backlog_item}"
        story_path = self.po.execute(full_task)
        code_path = self.dev.execute(story_path)
        review_path = self.code_reviewer.execute(code_path)
        data_path = self.data_preparer.execute(story_path)
        test_path = self.qa.execute(code_path, data_path)

        return {
            "story": story_path,
            "code": code_path,
            "review": review_path,
            "data": data_path,
            "tests": test_path
        }
