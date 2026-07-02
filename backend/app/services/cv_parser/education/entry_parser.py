from .entry_preprocessor import EntryPreprocessor
from .line_labeler import LineLabeler
from .output_builder import OutputBuilder


class EducationEntryParser:
    @staticmethod
    def parse(entry_text: str) -> dict:
        normalized_lines = EntryPreprocessor.preprocess(entry_text)
        labeled_lines = LineLabeler.label(normalized_lines)
        return OutputBuilder.build_entry(labeled_lines)
