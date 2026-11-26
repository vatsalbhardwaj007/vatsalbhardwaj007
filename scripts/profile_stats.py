"""Render a profile card from GitHub's public repository metadata."""

import argparse
from collections import Counter
import json
from math import cos, pi, sin
import os
from pathlib import Path
import subprocess
from xml.sax.saxutils import escape


ASSETS = Path(__file__).resolve().parents[1] / "assets"
LANGUAGES = ("TypeScript", "Python", "JavaScript", "Other")


def public_projects(owner):
    result = subprocess.run(
        ["gh", "api", "--paginate", "--slurp",
         f"users/{owner}/repos?type=owner&per_page=100"],
        check=True, capture_output=True, text=True, encoding="utf-8",
    )
    return [
        repo for page in json.loads(result.stdout) for repo in page
        if not repo["fork"] and not repo["private"] and repo["name"].lower() != owner.lower()
    ]


def card(height, content):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{height}" viewBox="0 0 760 {height}">
  <rect x="0.5" y="0.5" width="759" height="{height - 1}" rx="12" fill="#101820" stroke="#2d464c"/>
  <g font-family="ui-monospace, Consolas, monospace" fill="#d5e7e8">
{content}
  </g>
</svg>
"""


def radar_points(values):
    points = []
    for index, value in enumerate(values):
        angle = (index - 1) * pi / 2
        points.append(f"{205 + 76 * value * cos(angle):.2f},{175 + 76 * value * sin(angle):.2f}")
    return " ".join(points)


def repository_card(projects):
    counts = Counter(
        repo["language"] if repo["language"] in LANGUAGES else "Other"
        for repo in projects if repo["language"]
    )
    max_count = max(counts.values(), default=1)
    grid = "\n".join(
        f'    <polygon points="{radar_points([level] * 4)}" fill="none" stroke="#365256"/>'
        for level in (0.25, 0.5, 0.75, 1)
    )
    data = radar_points([counts[language] / max_count for language in LANGUAGES])
    labels = "\n".join(
        f'    <text x="{x}" y="{y}" text-anchor="{anchor}" font-size="15">'
        f'{escape(language)} · {counts[language]}</text>'
        for language, (x, y, anchor) in zip(LANGUAGES, (
            (205, 82, "middle"), (296, 180, "start"),
            (205, 276, "middle"), (115, 180, "end"),
        ))
    )
    stars = sum(repo["stargazers_count"] for repo in projects)
    return card(300, f"""    <text x="26" y="34" font-size="18" fill="#7df9c1">Primary languages</text>
    <text x="26" y="55" font-size="13">Repositories per language</text>
{grid}
    <path d="M 205 99 V 251 M 129 175 H 281" stroke="#365256"/>
    <polygon points="{data}" fill="#7df9c1" fill-opacity=".28" stroke="#7df9c1" stroke-width="2"/>
{labels}
    <path d="M 410 25 V 275" stroke="#365256"/>
    <text x="440" y="34" font-size="18" fill="#7df9c1">Public GitHub stats</text>
    <text x="440" y="113" font-size="31" fill="#7df9c1">{len(projects):,}</text>
    <text x="440" y="137" font-size="15">Public repositories</text>
    <text x="440" y="196" font-size="31" fill="#7df9c1">{stars:,}</text>
    <text x="440" y="220" font-size="15">Stars across repositories</text>
    <text x="440" y="266" font-size="12">Forks and profile repo excluded</text>""")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--placeholder", action="store_true", help="Create images for the first publish")
    args = parser.parse_args()
    ASSETS.mkdir(parents=True, exist_ok=True)
    if args.placeholder:
        for name, label in (("repository-stats", "Language radar and repository stats"),
                            ("contribution-snake", "Contribution snake")):
            image = card(94, f"""    <text x="24" y="37" font-size="19" fill="#7df9c1">{label}</text>
    <text x="24" y="66" font-size="14">Appears after the first GitHub Actions run.</text>""")
            (ASSETS / f"{name}.svg").write_text(image, encoding="utf-8")
        return

    projects = public_projects(os.environ["PROFILE_OWNER"])
    (ASSETS / "repository-stats.svg").write_text(repository_card(projects), encoding="utf-8")


if __name__ == "__main__":
    main()
