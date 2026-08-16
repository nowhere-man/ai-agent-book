"""Enhanced ArXiv metadata tools."""

import json
import logging
import re
from typing import Union

import arxiv
from dotenv import load_dotenv
from mcp.types import TextContent

from base import ActionResponse

load_dotenv()


async def get_paper_details(paper_id: str) -> Union[str, TextContent]:
    """Return metadata for one ArXiv paper."""
    try:
        clean_id = re.sub(r"^arxiv:", "", paper_id, flags=re.IGNORECASE).strip()
        paper = next(arxiv.Client().results(arxiv.Search(id_list=[clean_id])), None)
        if not paper:
            raise ValueError(f"Paper not found: {clean_id}")
        result = {
            "entry_id": paper.entry_id,
            "title": paper.title,
            "authors": [author.name for author in paper.authors],
            "summary": paper.summary,
            "published": paper.published.isoformat(),
            "updated": paper.updated.isoformat() if paper.updated else None,
            "categories": paper.categories,
            "primary_category": paper.primary_category,
            "doi": paper.doi,
            "journal_ref": paper.journal_ref,
        }
        response = ActionResponse(success=True, message=result, metadata={"paper_id": clean_id})
    except Exception as exc:
        logging.exception("ArXiv metadata lookup failed")
        response = ActionResponse(
            success=False,
            message=f"Failed to get paper details: {exc}",
            metadata={"error_type": "arxiv_error"},
        )
    return TextContent(type="text", text=json.dumps(response.model_dump()))


async def get_arxiv_categories() -> Union[str, TextContent]:
    """Return the supported ArXiv subject categories."""
    categories = {
        "cs": "Computer Science",
        "math": "Mathematics",
        "physics": "Physics",
        "astro-ph": "Astrophysics",
        "cond-mat": "Condensed Matter",
        "q-bio": "Quantitative Biology",
        "q-fin": "Quantitative Finance",
        "stat": "Statistics",
        "econ": "Economics",
        "eess": "Electrical Engineering",
    }
    response = ActionResponse(
        success=True,
        message={"categories": categories, "count": len(categories)},
        metadata={"total_categories": len(categories)},
    )
    return TextContent(type="text", text=json.dumps(response.model_dump()))
