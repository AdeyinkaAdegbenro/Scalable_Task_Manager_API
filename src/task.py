from flask import Blueprint, g, request
from auth import jwt_required
from celery import shared_task
from collections import defaultdict
from data.tasks import (
    create_task, get_task,
    get_tasks, delete_task,
    update_task,
    get_overdue_tasks)
from datetime import datetime
from models import Task
from flask_mail import Mail, Message
from typing import List

task_blueprint = Blueprint('tasks', __name__, url_prefix='/tasks')

@task_blueprint.route('/', methods=['GET', 'POST'])
@jwt_required
def tasks():
    if request.method == 'POST':
        data = request.json
        task = create_task(
            name=data['name'],
            description=data['description'],
            priority=data['priority'],
            due_date=datetime.strptime(data['due_date'], '%Y-%m-%d %H:%M:%S'),
        )
        return (task, 201)
    elif request.method == 'GET':
        tasks = get_tasks()
        return (tasks, 200)
    else:
        return 405

@task_blueprint.route('/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required
def task(task_id):
    if request.method == 'GET':
        task = get_task(int(task_id))
        return (task, 200)
    elif request.method == 'DELETE':
        delete_task(task_id)
        return 'OK'
    elif request.method == 'PUT':
        data = request.json
        task = update_task(
            task_id=int(task_id),
            name=data['name'],
            description=data['description'],
            priority=data['priority'],
            due_date=datetime.strptime(data['due_date'], '%Y-%m-%d %H:%M:%S'),
            done=data['done']
        )
        return (task, 200)
    return 405

@shared_task(ignore_result=False)
def send_overdue_task_reminder():
    # fetch all overdue undone tasks
    tasks: List[Task] = get_overdue_tasks()
    tasks_by_user =  defaultdict(list)
    for task in tasks:
        user_email = task.user.email
        tasks_by_user[user_email].append(task)
    send_email(tasks_by_user)
    g.session.close()
    print(tasks_by_user)
    

def send_email(user_tasks):
    for user, tasks in user_tasks.items():
        if len(tasks) == 1:
            task = tasks[0]
            msg = Message(
                subject=f"Reminder: {task.name} is due soon!", 
                sender="no-reply@example.com", 
                recipients=[tasks[0].user.email],
                body=f"Your task '{task.name}' is due on {task.due_date}. Don't forget to complete it!"
            )
        else:
            task_names = "\n".join([f"{idx + 1}. {task.name} is due on {task.due_date}." for (idx, task) in enumerate(tasks)])
            msg = Message(
                subject=f"You have several tasks due already!", 
                sender="no-reply@example.com", 
                recipients=[tasks[0].user.email],
                body=f"Your tasks: \n{task_names}\n Don't forget to complete them!"
            )

        print(msg)
        # from app import mail
        # mail.send(msg)