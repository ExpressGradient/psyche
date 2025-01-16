class Agent:
    def __init__(self, name: str, developer_prompt: str, tools):
        self.gold = 5
        self.food = 10
        self.hour = 0

        self.name = name
        self.messages = [{"role": "developer", "content": developer_prompt}]
        self.tools = tools
