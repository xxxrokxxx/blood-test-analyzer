schema = {
    "tools": [{
        "name": "analyze_blood_test",
        "description": "Analyze blood test results and provide structured analysis with insights",
        "inputSchema": {
            "type": "object",
            "required": ["content"],
            "properties": {
                "content": {
                    "type": "string",
                    "description": "The content of the blood test report"
                }
            }
        }
    }]
}

requirements = {
    "v0": {
        "configs": [],
        "network": {
            "domains": [],
            "required": False
        },
        "filesystem": {
            "volumes": [],
            "required": False
        }
    }
}
