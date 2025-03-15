from transformers import pipeline

class QwenGenerator:
    def __init__(self, model_name="Qwen/Qwen2.5-0.5B", max_tokens=100):
        """Initialize the Qwen text generation model."""
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.generator = pipeline("text-generation", model=model_name, max_new_tokens=max_tokens)

    def _format_prompt(self, question):
        """Formats the prompt to fit the instruction and context."""
        prompt = f"""
        <INSTRUCTION>
        You are a helpful bot and are answering all questions the human has. 
        You only answer the question and do not provide any additional information. 
        You are not allowed to ask questions.
        </INSTRUCTION>

        <CONTEXT>
        Big Thought's favorite color is blue.
        </CONTEXT>

        <QUESTION>
        {question}
        </QUESTION>

        <ANSWER>
        """
        return prompt.strip()

    def generate_answer(self, question):
        """Generates an answer based on the given question."""
        formatted_prompt = self._format_prompt(question)
        response = self.generator(formatted_prompt)
        return response[0]["generated_text"].strip()

    def set_max_tokens(self, n):
        """Updates the max token limit for text generation."""
        self.max_tokens = n
        self.generator = pipeline("text-generation", model=self.model_name, max_new_tokens=n)

    def change_model(self, new_model):
        """Updates the model used for text generation."""
        self.model_name = new_model
        self.generator = pipeline("text-generation", model=new_model, max_new_tokens=self.max_tokens)

    def get_current_model(self):
        """Returns the current model name."""
        return self.model_name
