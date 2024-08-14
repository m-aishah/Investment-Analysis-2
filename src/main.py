from flask import Flask, request, jsonify, abort
import os
from dotenv import load_dotenv
from flask_cors import CORS
from tools import tools

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/cmnd-tools", methods=['GET'])
def cmnd_tools_endpoint():
    tools_response = [
        {
            "name": tool["name"],
            "description": tool["description"],
            "jsonSchema": tool["parameters"],
            "isDangerous": tool.get("isDangerous", False),
            "functionType": tool["functionType"],
            "isLongRunningTool": tool.get("isLongRunningTool", False),
            "preCallPrompt": tool.get("preCallPrompt"),
            "postCallPrompt": tool.get("postCallPrompt"),
            "rerun": tool["rerun"],
            "rerunWithDifferentParameters": tool["rerunWithDifferentParameters"],
        } for tool in tools
    ]
    return jsonify({"tools": tools_response})

@app.route("/run-cmnd-tool", methods=['POST'])
def run_cmnd_tool_endpoint():
    data = request.json
    tool_name = data.get('toolName')
    print("tool_name", tool_name)
    props = data.get('props', {})
    print("props", props)
    #print(props)
    tool = next((t for t in tools if t['name'] == tool_name), None)
    print (tool["runCmd"])
    print(props["budget_max"])
    if not tool:
        abort(404, description="Tool not found")
    try:
        # conversation_id = props.pop("conversationId", None)
        # chatbot_conversation_id = props.pop("chatbotConversationId", None)
        # print("here")
        result = tool["runCmd"](**props)
        print("result", result)
        return jsonify(result)
    except Exception as e:
        abort(500, description=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
