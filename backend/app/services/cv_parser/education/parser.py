from .entry_parser import EducationEntryParser
from .entry_splitter import EducationEntrySplitter
from .output_builder import OutputBuilder
from .section_locator import EducationSectionLocator


class EducationParser:
    @staticmethod
    def parse(raw_text: str) -> list[dict]:
        section = EducationSectionLocator.locate(raw_text)
        if not section:
            return []

        entries = EducationEntrySplitter.split(section)
        parsed_entries = [EducationEntryParser.parse(entry) for entry in entries if entry.strip()]
        return OutputBuilder.build(parsed_entries)
