from prompt_toolkit.styles import Style

# style constant for the prompts
style: Style = Style.from_dict(
    {
        "dialog": "bg: #000000",
        "dialog.body": "bg: #000000 #dddddd",
        "checkbox-checked": "bg: #aa00ff",
        "frame": "bg: #aa00ff",
        "button.focused": "bg: #aa00ff",
        "frame.label": "bg: #dddddd",
        "prompt_text": "fg: #ffffff",
    }
)

prompt_txt: list = [
    ("class:prompt_text", ">>> ")
]