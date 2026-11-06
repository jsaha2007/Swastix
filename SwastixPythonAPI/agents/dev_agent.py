from agents.base_agent import BaseAgent
import json
import os
import uuid


class DevAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Developer",
            goal="""You are a backend developer working with FastAPI, SQLAlchemy 2.0, and PostgreSQL.
Read the given user story and implement the corresponding code.
Maintain SOLID principles as much as possible. Follow the repository pattern for database connection.
The code flow should be Repository -> Service -> Controller and vice versa.
Return a valid JSON object with this exact shape:
{"files": [{"path": "relative/path.py", "content": "complete file content"}]}
Generate every file required by the user story. Paths must be relative and use forward slashes.
Only output valid JSON - no explanations, no markdown formatting, no extra text."""
        )

    def execute(self, story_file_path):
        with open(story_file_path, "r", encoding="utf-8") as f:
            content = f.read()

        response = super().execute(content).strip()
        if response.startswith("```json") and response.endswith("```"):
            response = response[7:-3].strip()

        try:
            feature = json.loads(response)
        except json.JSONDecodeError as error:
            raise ValueError("DevAgent returned invalid JSON for the generated feature") from error

        files = feature.get("files")
        if not isinstance(files, list) or not files:
            raise ValueError("DevAgent response must contain a non-empty 'files' list")

        feature_directory = os.path.join("generated", f"feature_{uuid.uuid4()}")
        feature_root = os.path.abspath(feature_directory)
        saved_files = []

        for generated_file in files:
            relative_path = generated_file.get("path")
            file_content = generated_file.get("content")

            if not isinstance(relative_path, str) or not isinstance(file_content, str):
                raise ValueError("Each generated file must contain string 'path' and 'content' values")
            if os.path.isabs(relative_path) or relative_path.startswith(("..", "../", "..\\")):
                raise ValueError(f"Unsafe generated file path: {relative_path}")

            file_path = os.path.normpath(os.path.join(feature_directory, relative_path))
            if not os.path.abspath(file_path).startswith(feature_root + os.sep):
                raise ValueError(f"Unsafe generated file path: {relative_path}")

            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(file_content)
            saved_files.append(file_path)

        return {
            "directory": feature_directory,
            "files": saved_files
        }







