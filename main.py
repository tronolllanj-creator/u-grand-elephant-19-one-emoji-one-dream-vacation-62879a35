"""
# Entry validated: output is 1-8 chars, a single emoji, deterministic.
Entrypoint that writes a specific emoji to the designated output file.
"""

import os
from pathlib import Path

EMOJI = "🛖"


def main():
    # Determine output directory
    out_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    out_dir = Path(out_dir_env)
    out_dir.mkdir(parents=True, exist_ok=True)
    
    out_file = out_dir / "entry.txt"
    
    # Construct content: emoji + newline
    content = f"{EMOJI}\n"
    
    # Validate content using the exact specified condition
    if not (1 <= len(content) <= 8 and content.strip()):
        raise ValueError("Invalid content validation")
    
    # Write to file using UTF-8
    out_file.write_text(content, encoding="utf-8")
    
    # Print the output path, character count (including newline), and the emoji
    print(f"{out_file}")
    print(f"{len(content)}")
    print(f"{EMOJI}")


if __name__ == "__main__":
    main()
