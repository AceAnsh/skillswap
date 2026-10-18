# SkillSwap

**Teach what you know. Learn what you need.**
A peer-to-peer micro-mentorship exchange where students trade knowledge using Time-Credits instead of money.

## The problem
Online courses are one-directional, and learners who each know a different niche skill (one knows Python, another knows C) have no structured way to trade expertise.

## The solution
Teach 30 minutes of Python, earn 30 credits, spend them learning C from someone else.

## Key features
- **Skill matching:** pairs users by what they offer vs. what they want (mutual swaps rank first, credit-based matches next)
- **Shared workspace:** synchronized multi-language code editor, live video and whiteboard
- **Trust and reputation:** peer ratings, milestone badges and endorsements after each session
- **Micro-mentoring:** focused 20 to 30 minute sessions

## Time-Credit rules
- 1 minute taught = 1 credit earned
- New users start with 30 credits
- Credits move from learner to teacher only when a session is completed

## Project structure
```
backend/    FastAPI API, matching engine, credit ledger, tests
frontend/   Planned UI (see frontend/index.html)
docs/       Hackathon pitch deck (TEAM-AUSTERLITZ.pptx)
```

## Getting started
```bash
cd backend
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m unittest discover -s tests -t .           # run tests
uvicorn app.main:app --reload                       # API docs at http://127.0.0.1:8000/docs
```

## Roadmap
- [x] Matching engine and credit ledger (in-memory)
- [ ] Frontend matching screen
- [ ] Collaborative editor with code execution
- [ ] Video chat and whiteboard
- [ ] Ratings, badges and endorsements
- [ ] Persistent database and authentication

## Author
Ansh Tiwari ([@AceAnsh](https://github.com/AceAnsh))

## License
MIT
