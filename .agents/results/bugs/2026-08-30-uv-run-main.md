# Bug Report: `uv run main/main.py` → program not found + `bind()` TypeError

## Symptom
- `uv run main` and `uv run main.py` failed with `error: Failed to spawn ... program not found`.
- After switching to the correct entry, the server crashed with:
  `TypeError: bind(): AF_INET address must be tuple, not str`

## Root Cause
1. **No runnable file/command named `main`/`main.py`.** The only entry point is the
   script `py-chat = "py_chat:main"` in `pyproject.toml`. There was no root-level
   `main.py`.
2. **Wrong `bind()` argument.** `src/py_chat/__init__.py` called
   `s.bind(f"127.0.0.1:{PORT}")` passing a string; `bind()` requires a
   `(host, port)` tuple.

## Fix Applied
- Created `main.py` at project root that calls `py_chat.main()`, so
  `uv run main.py` works.
- Changed `src/py_chat/__init__.py:9` to `s.bind(("127.0.0.1", PORT))`.

## Files Changed
- `main.py` (new)
- `src/py_chat/__init__.py` (line 9)

## Regression Test
Manual integration test: launch `py_chat.main()` in a thread, connect a client
socket to `127.0.0.1:3000`, assert received payload `b'Hello world!'`. Passes.

## Similar Patterns
None — only one `bind()` call in the project.
