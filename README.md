# For first time run this cmd
    python3 -m venv venv

# From second time run this cmds
    source venv/bin/activate
    pip install -r requirements.txt
    uvicorn nxt:app --reload
