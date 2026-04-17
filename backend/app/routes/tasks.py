from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Task
from app.schemas import task_schema, tasks_schema
from app.utils.ai_client import suggest_task_priority
from app import db
import json

tasks_bp = Blueprint('tasks', __name__)


   
@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    
    if not task:
        return jsonify({"msg": "Task not found"}), 404
        
    db.session.delete(task)
    db.session.commit()
    return jsonify({"msg": "Task deleted"}), 200

@tasks_bp.route('/', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return tasks_schema.jsonify(tasks), 200

@tasks_bp.route('/', methods=['POST'])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({"error": "Title is required", "code": "VALIDATION_ERROR"}), 400

    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        user_id=user_id
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    return task_schema.jsonify(new_task), 201

@tasks_bp.route('/<int:task_id>/ai-suggest', methods=['POST'])
@jwt_required()
def ai_suggest(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    
    if not task:
        return jsonify({"error": "Task not found", "code": "NOT_FOUND"}), 404

    try:
        suggestion = suggest_task_priority(task.title, task.description)
        task.priority = suggestion.get('priority', task.priority)
        task.ai_suggestion = json.dumps(suggestion)
        db.session.commit()
        return task_schema.jsonify(task), 200
    except Exception as e:
        return jsonify({"error": str(e), "code": "AI_API_ERROR"}), 500
    
