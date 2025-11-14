---
title: Deep Research App        # Give your app a title
emoji: 🤖                       # Pick an emoji
colorFrom: indigo               # Theme start color
colorTo: blue                   # Theme end color
sdk: gradio                     # SDK type
sdk_version: "4.39.0"           # Example Gradio version
app_file: ui/app.py             # <-- points to your app.py inside ui/
pinned: false
---

# AI Deep Researcher

**AI Deep Researcher** is a generative AI learning project built using the OpenAI Agentic Framework. This app performs deep-level web research based on user queries and generates a well-structured, consolidated report.

To achieve this, the project integrates the following technologies and AI features:
- **OpenAI SDK**
- **OpenAI Agents**
- **OpenAI WebSearch Tool**
- **Serper API** - a free alternative to OpenAI WebSearch Tool (https://serper.dev/api-keys)
- **News API** (https://newsapi.org/v2/everything)
- **SendGrid** (for emailing report)
- **LLMs** - (OpenAI, Geminia, Groq)


## How it works?
The system is a multi-agent solution, where each agent has a specific responsibility:

1. **Planner Agent**
    - Receives the user query and builds a structured query plan.

2. **Guardrail Agent**
    - Validates user input and ensures compliance.
    - Stops the workflow if the input contains inappropriate or unparliamentary words.

3. **Search Agent**
    - Executes the query plan.
    - Runs multiple web searches in parallel to gather data.

4. **Writer Agent**
    - Reads results from all search agents.
    - Generates a well-formatted, consolidated report.

5. **Email Agent**
    - Responsible for sending the report via email using SendGrid.

6. **Orchestrator**
    - The entry point of the system.
    - Facilitates communication and workflow between all agents.

