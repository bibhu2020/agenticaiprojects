# Agentic AI Projects
This is a collection of agentic AI projects. Every project has its own project folder with its project specific configurations and environment variable settings. However, they all share the same common python virtual environment.

## Folder Structure
```
agenticaiproject/
├── README.md
├── requirements.txt
├── pyproject.toml
├── .env
├── .gitignore
│
├── github/
│   ├── workflows/ --> it has the ci/cd pipelines that deploy the application into Hugging Face.
│
├── projects/
│   ├── accessibility/
│   ├── chatbot/
│   ├── deep-research/
│   ├── mcp-servers/  --> it has a list of mcp servers that are shared by the projects
│   ├── stock-advisor/
│   ├── trip-planner/

```
## Hugging Face URLs

- accessibility: In Progress
- chatbot: https://huggingface.co/spaces/mishrabp/chatbot-app
- deep-research: https://huggingface.co/spaces/mishrabp/deep-research
- stock-advisor: TBD
- trip-planner: https://huggingface.co/spaces/mishrabp/trip-advisor-app


## How to setup locally

- You must have python and uv packag managed installed on your PC.

- Run `uv sync` command to create the virtual environment and install the required packages listed in pyproject.toml.

- Activate the virtual environment `source .venv/bin/activate`.

- Now, you can navigate to each project folder and create an .env file.

- Setup all the environment variables listed in .env.name file in .env file.

- Run `python run.py` 
