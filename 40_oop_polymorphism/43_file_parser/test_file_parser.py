import json
import os
import tempfile
from abc import ABC, abstractmethod

import pytest

try:
    from file_parser import (
        CSVParser,
        FileParser,
        FileProcessor,
        JSONParser,
        create_parser,
    )
except ImportError:

    class FileParser(ABC):
        @abstractmethod
        def __init__(self, file_path) -> None:
            raise NotImplementedError("Implement FileParser class")

    class CSVParser:
        def __init__(self, file_path) -> None:
            raise NotImplementedError("Implement CSVParser class")

    class JSONParser:
        def __init__(self, file_path) -> None:
            raise NotImplementedError("Implement JSONParser class")

    class FileProcessor:
        def __init__(self) -> None:
            raise NotImplementedError("Implement FileProcessor class")

    def create_parser(file_path):
        raise NotImplementedError("Implement create_parser()")


@pytest.fixture
def temp_csv_file():
    content = """name,age,city
Alice,30,NYC
Bob,25,LA
Charlie,35,Chicago"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(content)
        temp_path = f.name
    yield temp_path
    os.unlink(temp_path)


@pytest.fixture
def temp_json_file():
    data = {"app": "MyApp", "version": "1.0", "debug": True, "count": 42}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(data, f)
        temp_path = f.name
    yield temp_path
    os.unlink(temp_path)


@pytest.fixture
def temp_invalid_json():
    content = '{"invalid": json syntax}'
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        f.write(content)
        temp_path = f.name
    yield temp_path
    os.unlink(temp_path)


class TestCSVParser:
    def test_csv_parser_initialization(self, temp_csv_file):
        parser = CSVParser(temp_csv_file)
        assert parser.file_path == temp_csv_file

    def test_csv_validation(self, temp_csv_file):
        parser = CSVParser(temp_csv_file)
        assert parser.validate() is True

    def test_csv_wrong_extension(self):
        parser = CSVParser("test.txt")
        assert parser.validate() is False

    def test_csv_parse(self, temp_csv_file):
        parser = CSVParser(temp_csv_file)
        data = parser.parse()
        assert isinstance(data, list)
        assert len(data) == 3
        assert isinstance(data[0], dict)
        assert "name" in data[0]
        assert data[0]["name"] == "Alice"
        assert data[1]["name"] == "Bob"

    def test_csv_get_extension(self, temp_csv_file):
        parser = CSVParser(temp_csv_file)
        assert parser.get_extension() == ".csv"

    def test_csv_get_file_size(self, temp_csv_file):
        parser = CSVParser(temp_csv_file)
        size = parser.get_file_size()
        assert isinstance(size, int)
        assert size > 0


class TestJSONParser:
    def test_json_parser_initialization(self, temp_json_file):
        parser = JSONParser(temp_json_file)
        assert parser.file_path == temp_json_file

    def test_json_validation(self, temp_json_file):
        parser = JSONParser(temp_json_file)
        assert parser.validate() is True

    def test_json_wrong_extension(self):
        parser = JSONParser("test.txt")
        assert parser.validate() is False

    def test_json_parse(self, temp_json_file):
        parser = JSONParser(temp_json_file)
        data = parser.parse()
        assert isinstance(data, dict)
        assert data["app"] == "MyApp"
        assert data["version"] == "1.0"
        assert data["debug"] is True
        assert data["count"] == 42

    def test_json_parse_invalid(self, temp_invalid_json):
        parser = JSONParser(temp_invalid_json)
        try:
            data = parser.parse()
            assert data is None or data == {}
        except (json.JSONDecodeError, ValueError):
            pass

    def test_json_get_extension(self, temp_json_file):
        parser = JSONParser(temp_json_file)
        assert parser.get_extension() == ".json"


class TestFileProcessor:
    def test_processor_initialization(self):
        processor = FileProcessor()
        assert processor is not None

    def test_process_single_csv(self, temp_csv_file):
        processor = FileProcessor()
        parser = CSVParser(temp_csv_file)
        data = processor.process_file(parser)
        assert isinstance(data, list)
        assert len(data) > 0

    def test_process_single_json(self, temp_json_file):
        processor = FileProcessor()
        parser = JSONParser(temp_json_file)
        data = processor.process_file(parser)
        assert isinstance(data, dict)

    def test_process_batch(self, temp_csv_file, temp_json_file):
        processor = FileProcessor()
        parsers = [
            CSVParser(temp_csv_file),
            JSONParser(temp_json_file),
        ]
        results = processor.process_batch(parsers)
        assert isinstance(results, dict)
        assert len(results) == 2

    def test_get_summary(self, temp_csv_file, temp_json_file):
        processor = FileProcessor()
        parsers = [
            CSVParser(temp_csv_file),
            JSONParser(temp_json_file),
        ]
        summary = processor.get_summary(parsers)
        assert isinstance(summary, dict)
        assert "total" in summary
        assert summary["total"] == 2
        assert "total_size" in summary
        assert "formats" in summary


class TestCreateParser:
    def test_create_csv_parser(self, temp_csv_file):
        parser = create_parser(temp_csv_file)
        assert isinstance(parser, CSVParser)

    def test_create_json_parser(self, temp_json_file):
        parser = create_parser(temp_json_file)
        assert isinstance(parser, JSONParser)

    def test_create_parser_unsupported_format(self):
        with pytest.raises((ValueError, NotImplementedError)):
            create_parser("test.txt")

    def test_create_parser_no_extension(self):
        with pytest.raises((ValueError, NotImplementedError)):
            create_parser("testfile")


class TestPolymorphism:
    def test_parsers_share_interface(self, temp_csv_file, temp_json_file):
        parsers = [
            CSVParser(temp_csv_file),
            JSONParser(temp_json_file),
        ]

        for parser in parsers:
            assert hasattr(parser, "parse")
            assert hasattr(parser, "validate")
            assert hasattr(parser, "get_file_size")
            assert hasattr(parser, "get_extension")

    def test_process_mixed_formats_polymorphically(self, temp_csv_file, temp_json_file):
        processor = FileProcessor()
        parsers = [
            CSVParser(temp_csv_file),
            JSONParser(temp_json_file),
        ]

        for parser in parsers:
            data = processor.process_file(parser)
            assert data is not None

    def test_extensible_design(self, temp_csv_file):
        class TextParser(FileParser):
            def __init__(self, file_path) -> None:
                self.file_path = file_path

            def parse(self):
                with open(self.file_path, "r") as f:
                    return {"lines": f.readlines()}

            def validate(self):
                return self.file_path.endswith(".txt")

            def get_file_size(self):
                return os.path.getsize(self.file_path)

            def get_extension(self):
                return os.path.splitext(self.file_path)[1]

        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("Hello\nWorld\n")
            temp_txt = f.name

        try:
            processor = FileProcessor()
            parsers = [CSVParser(temp_csv_file), TextParser(temp_txt)]
            results = processor.process_batch(parsers)
            assert len(results) == 2
        finally:
            os.unlink(temp_txt)

    def test_no_type_checking_in_processor(self, temp_csv_file, temp_json_file):
        processor = FileProcessor()
        parsers = [
            CSVParser(temp_csv_file),
            JSONParser(temp_json_file),
        ]

        results = processor.process_batch(parsers)

        assert len(results) == len(parsers)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
