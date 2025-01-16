from openai import OpenAI

client = OpenAI()


class Agent:
    def __init__(self, name: str, developer_prompt: str, tools: list, model="gpt-4o"):
        self.gold = 5
        self.food = 10
        self.hour = 0

        self.name = name
        self.messages = [{"role": "developer", "content": developer_prompt}]
        self.tools = tools
        self.model = model

    def chat(self, message: str):
        self.messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            messages=self.messages, model=self.model, tools=self.tools
        )

        if response.choices[0].finish_reason == "tool_calls":
            for call_dict in response.choices[0].message.tool_calls:
                match call_dict.function.name:
                    case 'interact_with':
                        pass
                    case 'transfer_gold':
                        pass
                    case 'grow_food':
                        pass
                    case 'mine_gold':
                        pass
