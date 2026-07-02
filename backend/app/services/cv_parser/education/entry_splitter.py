class EducationEntrySplitter:
    @staticmethod
    def split(section_text: str) -> list[str]:
        entries = []
        current_entry = []

        for line in section_text.splitlines():
            if not line.strip():
                if current_entry:
                    entries.append("\n".join(current_entry).strip())
                    current_entry = []
                continue

            current_entry.append(line)

        if current_entry:
            entries.append("\n".join(current_entry).strip())

        return entries
