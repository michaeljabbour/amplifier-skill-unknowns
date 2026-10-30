"""Keep the bundle skill collection attached to this capability's actual method."""
import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def test_skill_source_resolves_declared_method():
    manifest = json.loads((ROOT / "capability.json").read_text())
    behavior = (ROOT / "behaviors/unknowns.yaml").read_text()
    sources = re.findall(r"git\+https://github\.com/michaeljabbour/[^\s\"']+", behavior)
    assert len(sources) == 1
    source = urlsplit(sources[0][4:])
    repository, ref = source.path.rsplit("@", 1)
    assert source.scheme == "https" and source.netloc == "github.com"
    assert "https://github.com" + repository == manifest["repository_url"]
    assert ref == "main"
    collection = (ROOT / parse_qs(source.fragment)["subdirectory"][0]).resolve()
    collection.relative_to(ROOT)
    method = (ROOT / manifest["portable_method"]["path"]).resolve()
    method.relative_to(collection)
    frontmatter = re.match(r"^---\n(.*?)\n---", (method / "SKILL.md").read_text(), re.S).group(1)
    name = re.search(r"^name:\s*(.+)$", frontmatter, re.M).group(1).strip()
    assert name == manifest["portable_method"]["name"] == "unknowns"
    assert re.search(r"^  name: unknowns$", (ROOT / "bundle.md").read_text(), re.M)


def test_interactive_dependency_resolves_without_a_prior_namespace_alias():
    """Fresh loaders must resolve the same declared dependency before alias registration."""
    bundle = (ROOT / "bundle.md").read_text().split("---", 2)[1]
    includes = re.findall(r"^  - bundle: (.+)$", bundle, re.M)
    assert "attractor:bundles/attractor-interactive" not in includes
    dependency = "git+https://github.com/microsoft/amplifier-bundle-attractor@main"
    assert dependency in includes
    interactive = next(source for source in includes if "bundles/attractor-interactive" in source)
    source = urlsplit(interactive[4:])
    assert "git+" + source._replace(fragment="").geturl() == dependency
    assert parse_qs(source.fragment) == {"subdirectory": ["bundles/attractor-interactive.yaml"]}
