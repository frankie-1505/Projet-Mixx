from dataclasses import dataclass
from typing import List


@dataclass
class Partner:
    id: str
    nom: str
    alias: str = ""

    def matches(self, search_term: str) -> bool:
        search_lower = search_term.lower().strip()
        nom_lower = self.nom.lower()
        alias_lower = self.alias.lower() if self.alias else ""

        if nom_lower == search_lower or alias_lower == search_lower:
            return True

        if search_lower in nom_lower or search_lower in alias_lower:
            return True

        if nom_lower in search_lower or alias_lower in search_lower:
            return True

        first_word_search = search_lower.split()[0] if search_lower.split() else ""
        first_word_partner = nom_lower.split()[0] if nom_lower.split() else ""

        if first_word_search and first_word_partner and first_word_search == first_word_partner:
            return True

        return False

    @property
    def display_name(self) -> str:
        return self.nom
