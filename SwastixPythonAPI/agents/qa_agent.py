from agents.base_agent import BaseAgent

class QaAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="QA Engineer", 
            goal="""You are a QA engineer. You will be given a code snippet and you need to write test cases for it.
            The test cases should be written in pytest framework. 
            The test cases should cover all possible edge cases and scenarios.
            You will be given both the code AND sample test data.
            Use the provided sample data directly in your test cases wherever applicable.
            The test cases should be written in a separate file named test_<original_file_name>.py
            Only output the code — no explanations, no markdown formatting, no extra text."""
        )

    def execute(self, code_file_path, data_file_path) -> str:
        with open(code_file_path, "r", encoding="utf-8") as f:
            code_content = f.read()
        with open(data_file_path, "r", encoding="utf-8") as f:
            data_content = f.read()

        combined_input = f"Code:\n{code_content}\n\nTest Data:\n{data_content}"
        test_code = super().execute(combined_input)
        path = self.saveToFile(test_code, "Tests", "test_code")
        return path