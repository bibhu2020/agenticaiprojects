import gradio as gr
from dotenv import load_dotenv
from appagents.orchestrator import Orchestrator
from agents import SQLiteSession
import uuid  # to generate session IDs if needed

load_dotenv(override=True)

# Keep sessions persistent between user interactions
# Key: session ID; Value: SQLiteSession instance
sessions = {}

async def run(query: str, session_id: str):
    """
    Run the orchestrator for a given query.
    Each user session keeps its own SQLiteSession so
    conversation context is remembered across queries.
    """
    # Get or create persistent session
    if session_id not in sessions:
        sessions[session_id] = SQLiteSession(f"session_{session_id}.db")

    session = sessions[session_id]
    orchestrator = Orchestrator(session=session)

    # Stream chunks from orchestrator
    async for chunk in orchestrator.run(query):
        yield chunk

with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# 🧠 Deep Research (Powered by Agentic AI)")

    query_textbox = gr.Textbox(
        label="What topic would you like to research?",
        placeholder="E.g., The impact of AI on healthcare",
        lines=2,
        max_lines=4,
        value="The impact of AI on USA stock market performance in 2025.",
    )

    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")

    # Create a State component for the session ID
    session_state = gr.State(value=str(uuid.uuid4()))

    # Connect button click and textbox submit to run()
    run_button.click(
        fn=run,
        inputs=[query_textbox, session_state],
        outputs=report,
    )
    query_textbox.submit(
        fn=run,
        inputs=[query_textbox, session_state],
        outputs=report,
    )

ui.launch(inbrowser=True)
