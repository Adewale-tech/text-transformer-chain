# text-transformer-chain
# Text Transformer Chain (Telex.im Agent)

Three FastAPI agents:
- Capitalizer Agent (`/capitalize/`): Converts text to UPPERCASE.
- Reverse Agent (`/reverse/`): Reverses word order.
- Input Agent (`/transform-text/`): Chained orchestrator.

## How to Run

- Install Python 3.10+
- `pip install -r requirements.txt` in each agent directory
- Run each agent on separate ports

## API Example

POST /transform-text/
