from datetime import datetime
from typing import Any, Dict

from github.GithubObject import CompletableGithubObject

class Secret(CompletableGithubObject):
    def __repr__(self) -> str: ...
    @property
    def _identity(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def visibility(self) -> str: ...
    @property
    def selected_repositories_url(self) -> str: ...