import os
import sys
import importlib

def main():
    # Root directory of the project
    root_dir = os.path.dirname(os.path.abspath(__file__))

    # Ensure the root and ui folder are on the Python path
    ui_path = os.path.join(root_dir, "ui")
    for p in [root_dir, ui_path]:
        if p not in sys.path:
            sys.path.insert(0, p)

    print("🚀 Starting Gradio app (ui/app.py)...\n")

    # Import and launch the UI
    app_module = importlib.import_module("ui.app")

    if hasattr(app_module, "ui"):
        app_module.ui.launch(inbrowser=True)
    else:
        print("❌ Could not find `ui` object in ui/app.py")

if __name__ == "__main__":
    main()
