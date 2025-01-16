interact_with = {
    "type": "function",
    "function": {
        "name": "interact_with",
        "description": "Facilitate an interaction with another agent to exchange information, build relationships, or negotiate actions.",
        "parameters": {
            "type": "object",
            "properties": {
                "agent_name": {
                    "type": "string",
                    "description": "The name of the agent you want to interact with.",
                },
                "action": {
                    "type": "string",
                    "description": "The specific action of the interaction.",
                },
            },
            "required": ["agent_name", "action"],
            "additionalProperties": False,
        },
    },
}

transfer_gold = {
    "type": "function",
    "function": {
        "name": "transfer_gold",
        "description": "Send a specified amount of gold to another agent, typically for trade, alliances, or as a gift.",
        "parameters": {
            "type": "object",
            "properties": {
                "agent_name": {
                    "type": "string",
                    "description": "The name of the agent who will receive the gold.",
                },
                "amount": {
                    "type": "number",
                    "description": "The quantity of gold to transfer to the recipient.",
                },
            },
            "required": ["agent_name", "amount"],
            "additionalProperties": False,
        },
    },
}

grow_food = {
    "type": "function",
    "function": {
        "name": "grow_food",
        "description": "Invest gold to produce food units, typically used to sustain agents or for trading purposes.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
}

mine_gold = {
    "type": "function",
    "function": {
        "name": "mine_gold",
        "description": "Consume food to extract gold, enabling agents to acquire resources for trading or survival.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
}
