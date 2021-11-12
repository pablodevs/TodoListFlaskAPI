from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Global variables
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# Get todo list
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

# Add a todo to the todo list
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    todos.append(request_body)
    return jsonify(todos), 200

# Delete a todo from the todo list
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos), 200

## LAST LINE OF CODE
# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)