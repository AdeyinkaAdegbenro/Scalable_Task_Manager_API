from datetime import datetime
from models import Task
from init_db import get_db, get_redis
from flask import g
from sqlalchemy import select
from typing import Dict
import json


def create_task(name: str, description: str, priority: str, due_date: str, done: bool=False) -> Dict[str, str]:
    db = get_db()
    with db as session:
        with session.begin():
            task = Task(
                name=name,
                description=description,
                priority=priority,
                due_date=due_date,
                done=done,
                user_id=g.user['id']
            )
            session.add(task)
        return task_to_json(task)

def get_tasks():
    redis_client = get_redis()
    query_key = f"get_user_tasks:{g.user['id']}"
    cached_result = redis_client.get(query_key)
    if cached_result:
        return json.loads(cached_result)

    db = get_db()
    with db as session:
        tasks = session.execute(
            select(Task).where(
                Task.user_id == g.user['id'])
        ).scalars().all()

        to_cache_result = [
            task_to_json(task)
            for task in tasks
        ]
        redis_client.set(query_key, json.dumps(to_cache_result), ex=10)
        return to_cache_result

def get_task(task_id):
    redis_client = get_redis()
    query_key = f"get_task_with_id:{task_id}"
    cached_result = redis_client.get(query_key)
    if cached_result:
        return json.loads(cached_result)
    db = get_db()
    with db as session:
        # TODO query by user  only
        task = session.get(Task, task_id)
        if not task:
            return "Not found"
        if task and (task.user_id != g.user['id']):
            return "Not found"
    to_cache = task_to_json(task)
    redis_client.set(query_key, json.dumps(to_cache), ex=10)
    return to_cache

def update_task(task_id, name: str, description: str, priority: str, due_date: str, done: bool):
    db = get_db()
    arguments = locals()
    with db as session:
        with session.begin():
            task = session.get(Task, task_id)
            assert task.user_id == g.user['id'], "Task does not belong to current user"
            for arg, val in arguments.items():
                if arg == 'task_id': continue
                if val:
                    setattr(task, arg, val)
        return task_to_json(task)

def delete_task(task_id):
    db = get_db()
    with db as session, session.begin():
        task = session.get(Task, task_id)
        assert task.user_id == g.user['id'], "Task does not belong to current user"
        session.delete(task)

def task_to_json(task: Task):
    return dict(
        id=task.id,
        name=task.name,
        description=task.description,
        priority=task.priority,
        due_date=datetime.strftime(task.due_date, '%Y-%m-%d %H:%M:%S'),
        done=task.done,
        user_id=task.user_id
    )

def get_overdue_tasks():
    g.session = get_db()
    return g.session.execute(select(Task).where(
        Task.done == False,
        Task.due_date < datetime.now(),
    )).scalars().all()