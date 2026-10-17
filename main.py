"""FastAPI app (in-memory, hackathon prototype). Run: uvicorn app.main:app --reload"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .credits import InsufficientCredits, Ledger
from .matching import User, find_matches

app = FastAPI(title="SkillSwap API")
users = {}
ledger = Ledger()


class UserIn(BaseModel):
    id: str
    name: str
    offers: list[str]
    wants: list[str]


class SessionIn(BaseModel):
    teacher_id: str
    learner_id: str
    minutes: int


@app.post("/users")
def create_user(u: UserIn):
    users[u.id] = User(u.id, u.name, set(u.offers), set(u.wants))
    ledger.register(u.id)
    return {"id": u.id, "balance": ledger.balance(u.id)}


@app.get("/users/{user_id}/matches")
def matches(user_id: str):
    if user_id not in users:
        raise HTTPException(404, "unknown user")
    found = find_matches(users[user_id], list(users.values()))
    return [{"user": m.user.name, "kind": m.kind, "they_teach": sorted(m.they_teach),
             "you_teach": sorted(m.you_teach), "score": m.score} for m in found]


@app.get("/users/{user_id}/balance")
def balance(user_id: str):
    if user_id not in users:
        raise HTTPException(404, "unknown user")
    return {"balance": ledger.balance(user_id)}


@app.post("/sessions/complete")
def complete(s: SessionIn):
    for uid in (s.teacher_id, s.learner_id):
        if uid not in users:
            raise HTTPException(404, f"unknown user {uid}")
    try:
        ledger.complete_session(s.teacher_id, s.learner_id, s.minutes)
    except (InsufficientCredits, ValueError) as e:
        raise HTTPException(400, str(e))
    return {"teacher": ledger.balance(s.teacher_id), "learner": ledger.balance(s.learner_id)}
