import csv
import json
import os
from abc import ABC, abstractmethod
from typing import Any, Dict, List


class FileParser(ABC):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    @abstractmethod
    def parse(self) -> Any:
        pass

    @abstractmethod
    def validate(self) -> bool:
        pass

    def get_file_size(self) -> int:
        if os.path.exists(self.file_path):
            return os.path.getsize(self.file_path)
        return 0

    def get_extension(self) -> str:
        return os.path.splitext(self.file_path)[1]


class CSVParser(FileParser):
    def validate(self) -> bool:
        return self.get_extension().lower() == ".csv"

    def parse(self) -> List[Dict[str, str]]:
        if not os.path.exists(self.file_path):
            return []

        data = []
        with open(self.file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(dict(row))
        return data


class JSONParser(FileParser):
    def validate(self) -> bool:
        return self.get_extension().lower() == ".json"

    def parse(self) -> Dict[str, Any] | List[Any] | None:
        if not os.path.exists(self.file_path):
            return None

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return None


class FileProcessor:
    def __init__(self) -> None:
        pass

    def process_file(self, parser: FileParser) -> Any:
        return parser.parse()

    def process_batch(self, parsers: List[FileParser]) -> Dict[str, Any]:
        results = {}
        for parser in parsers:
            results[parser.file_path] = parser.parse()
        return results

    def get_summary(self, parsers: List[FileParser]) -> Dict[str, int | List[str]]:
        total_size = sum(parser.get_file_size() for parser in parsers)
        formats = [parser.get_extension().lstrip(".") for parser in parsers]

        return {
            "total": len(parsers),
            "total_size": total_size,
            "formats": formats,
        }


def create_parser(file_path: str) -> FileParser:
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".csv":
        return CSVParser(file_path)
    elif extension == ".json":
        return JSONParser(file_path)
    else:
        raise ValueError(f"Unsupported file format: {extension}")


if __name__ == "__main__":
    import tempfile

    # Create temporary test files
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as csv_file:
        csv_file.write("name,age,city\n")
        csv_file.write("Alice,30,NYC\n")
        csv_file.write("Bob,25,LA\n")
        csv_path = csv_file.name

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False
    ) as json_file:
        json.dump({"app": "MyApp", "version": "1.0", "debug": True}, json_file)
        json_path = json_file.name

    try:
        csv_parser = CSVParser(csv_path)
        json_parser = JSONParser(json_path)

        print("=== CSV Parsing ===")
        csv_data = csv_parser.parse()
        print(f"Parsed {len(csv_data)} records from CSV")
        print(f"First record: {csv_data[0]}")

        print("\n=== JSON Parsing ===")
        json_data = json_parser.parse()
        print(f"JSON data: {json_data}")

        print("\n=== File Validation ===")
        parsers = [csv_parser, json_parser]
        for parser in parsers:
            is_valid = parser.validate()
            print(f"{parser.get_extension()} file valid: {is_valid}")

        processor = FileProcessor()

        print("\n=== Batch Processing ===")
        results = processor.process_batch(parsers)
        print(f"Processed {len(results)} files")

        print("\n=== Processing Summary ===")
        summary = processor.get_summary(parsers)
        print(f"Total files: {summary['total']}")
        print(f"Total size: {summary['total_size']} bytes")
        print(f"Formats: {summary['formats']}")

        print("\n=== Auto-Detection ===")
        parser1 = create_parser(csv_path)
        print(f"Auto-detected: {type(parser1).__name__}")

    finally:
        os.unlink(csv_path)
        os.unlink(json_path)
