def append_conversation_summary(version, timestamp, summary):
    with open("conversation_log.txt", "a") as log_file:
        log_entry = f"Version: {version}\nTimestamp: {timestamp}\nSummary: {summary}\n{'-' * 40}\n"
        log_file.write(log_entry)