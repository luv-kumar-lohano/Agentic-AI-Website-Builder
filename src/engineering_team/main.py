#!/usr/bin/env python
import warnings
import os
from datetime import datetime

from engineering_team.crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
A simple account management system for a trading simulation platform.
The system should allow users to create an account, deposit funds, and withdraw funds.
The system should allow users to record that they have bought or sold shares, providing a quantity.
The system should calculate the total value of the user's portfolio, and the profit or loss from the initial deposit.
The system should be able to report the holdings of the user at any point in time.
The system should be able to report the profit or loss of the user at any point in time.
The system should be able to list the transactions that the user has made over time.
The system should prevent the user from withdrawing funds that would leave them with a negative balance, or
 from buying more shares than they can afford, or selling shares that they don't have.
 The system has access to a function get_share_price(symbol) which returns the current price of a share, and includes a test implementation that returns fixed prices for AAPL, TSLA, GOOGL.
"""
module_name = "accounts.py"
class_name = "Account"


def run():
    """
    Run the research crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = EngineeringTeam().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()



# ---------------------------------------------------------------------------
# Alternative CLI-driven main (commented out) (Result stored in sample_output)
# ---------------------------------------------------------------------------
# import argparse
# from pathlib import Path
#
# DEFAULT_REQUIREMENTS = """
# You are building a multi-surface digital product planning assistant that delivers
# architecture, design guidance, and implementation tasks for a combined website
# and mobile application.
#
# The module must:
# - capture a project brief including audience, brand voice, success metrics, and
#   primary features;
# - generate a sitemap / navigation map for both the website and app, including
#   top-level pages, user flows, and cross-surface entry points;
# - produce detailed page specifications outlining sections, layout hints,
#   component suggestions, and copy prompts;
# - define a design system summary covering typography, color palette, spacing,
#   and interaction tokens that can be reused by design tools;
# - construct a prioritized implementation backlog with epics, user stories,
#   acceptance criteria, and rough sizing;
# - export all artefacts as JSON-serialisable dictionaries so they can be saved or
#   rendered by downstream automation.
#
# Ensure the module keeps identifiers unique, maintains referential integrity
# between navigation, components, and backlog items, and exposes clear methods for
# updating any part of the blueprint without corrupting the overall plan.
# """
#
# DEFAULT_MODULE_NAME = "project_blueprint.py"
# DEFAULT_CLASS_NAME = "ProjectBlueprint"
# DEFAULT_OUTPUT_DIR = Path("output")
#
#
# def build_parser() -> argparse.ArgumentParser:
#     parser = argparse.ArgumentParser(
#         description=(
#             "Kick off the CrewAI engineering team to generate a website/app "
#             "planning module."
#         )
#     )
#     parser.add_argument(
#         "--requirements-file",
#         type=Path,
#         help="Path to a text file containing high-level requirements.",
#     )
#     parser.add_argument(
#         "--requirements-text",
#         type=str,
#         help="Requirements provided directly on the command line.",
#     )
#     parser.add_argument(
#         "--module-name",
#         type=str,
#         default=DEFAULT_MODULE_NAME,
#         help=f"Name for the generated Python module (default: {DEFAULT_MODULE_NAME}).",
#     )
#     parser.add_argument(
#         "--class-name",
#         type=str,
#         default=DEFAULT_CLASS_NAME,
#         help=f"Name for the primary class inside the module (default: {DEFAULT_CLASS_NAME}).",
#     )
#     parser.add_argument(
#         "--output-dir",
#         type=Path,
#         default=DEFAULT_OUTPUT_DIR,
#         help="Directory where agent outputs will be written (default: output/).",
#     )
#     return parser
#
#
# def resolve_requirements(args: argparse.Namespace) -> str:
#     if args.requirements_text and args.requirements_file:
#         raise SystemExit("Provide either --requirements-file or --requirements-text, not both.")
#
#     if args.requirements_file:
#         try:
#             return args.requirements_file.read_text(encoding="utf-8")
#         except FileNotFoundError as exc:
#             raise SystemExit(f"Requirements file not found: {exc}") from exc
#     if args.requirements_text:
#         return args.requirements_text
#     return DEFAULT_REQUIREMENTS
#
#
# def run_cli(argv: list[str] | None = None) -> None:
#     parser = build_parser()
#     args = parser.parse_args(argv)
#
#     requirements = resolve_requirements(args)
#     module_name = args.module_name
#     class_name = args.class_name
#     output_dir = args.output_dir
#     output_dir.mkdir(parents=True, exist_ok=True)
#
#     inputs = {
#         "requirements": requirements,
#         "module_name": module_name,
#         "class_name": class_name,
#     }
#
#     EngineeringTeam().crew().kickoff(inputs=inputs)
#
#
# if __name__ == "__main__":
#     run_cli()
