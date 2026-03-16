# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "jinja2",
#     "markdown",
# ]
# ///

import shutil
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader

DIR_ROOT = Path(__file__).parent
DIR_SRC = DIR_ROOT / "src"
DIR_DIST = DIR_ROOT / "dist"
DIR_TEMPLATES = DIR_SRC / "template"
DIR_EPISODES = DIR_SRC / "episodes"


def read_episodes():
    episodes = []

    for path in DIR_EPISODES.glob("*.md"):
        if path.stem.startswith("_"): continue
        day = int(path.stem)
        content = markdown.markdown(path.read_text(encoding="utf-8").strip())
        episodes.append({ "day": day, "content": content })

    episodes.sort(key=lambda ep: ep["day"])

    return episodes


def write(target, content):
    path = Path(target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("Wrote", path.relative_to(Path.cwd()))


def build():
    # Clean:
    if DIR_DIST.exists():
        shutil.rmtree(DIR_DIST)

    # Data:
    episodes = read_episodes()

    # Templates:
    env = Environment(loader=FileSystemLoader(DIR_TEMPLATES))
    shared = {
        "episodes": [ep["day"] for ep in episodes],
    }

    # Render index:
    index_html = env.get_template("index.html").render(**shared)
    write(DIR_DIST / "index.html", index_html)

    # Render episodes:
    for i, episode in enumerate(episodes):
        prev_day = episodes[i - 1]["day"] if i > 0 else None
        next_day = episodes[i + 1]["day"] if i < len(episodes) - 1 else None

        episode_html = env.get_template("episode.html").render(
            **shared,
            day=episode["day"],
            content=episode["content"],
            prev=prev_day,
            next=next_day,
        )

        write(DIR_DIST / "ep" / str(episode['day']) / "index.html", episode_html)


if __name__ == "__main__":
    build()
