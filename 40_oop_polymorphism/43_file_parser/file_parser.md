# Python OOP Practice - Polymorphism: File Parser System

## Exercise: Polymorphic File Format Parser

Create a file parser system that can read and process different file formats (CSV, JSON) using a common interface. This demonstrates how polymorphism handles different data formats uniformly.

**Instructions:**
Design an abstract `FileParser` base class and concrete implementations for different file formats. Create a file processing system that works with any parser type polymorphically.

This exercise demonstrates real-world polymorphism in data processing pipelines where the same operations work across different file formats.

**Your Complete Task:**
1. Create an abstract `FileParser` class (using ABC) with:
   - Constructor accepting `file_path` parameter
   - Abstract method `parse()` that returns parsed data
   - Abstract method `validate()` that returns bool
   - Concrete method `get_file_size()` that returns file size in bytes
   - Concrete method `get_extension()` that returns file extension
2. Create `CSVParser` class:
   - Validates file has `.csv` extension
   - Parses CSV and returns list of dictionaries (each row as dict)
   - Handle header row as keys
3. Create `JSONParser` class:
   - Validates file has `.json` extension
   - Parses JSON and returns Python dictionary/list
   - Handle malformed JSON gracefully
4. Create a `FileProcessor` class with:
   - Method `process_file(parser)` that parses and returns data
   - Method `process_batch(parsers)` that processes multiple files
   - Method `get_summary(parsers)` that returns statistics
5. Create helper function `create_parser(file_path)` that:
   - Auto-detects file type from extension
   - Returns appropriate parser instance
   - Raises error for unsupported formats

**What You'll Learn:**
- **Format abstraction:** Same interface for different data formats
- **Factory pattern:** Auto-creating correct parser type
- **Error handling:** Graceful degradation with invalid files
- **Data pipeline:** Processing heterogeneous file collections
- **Extensibility:** Easy to add new file formats

**Example Usage:**
```python
from abc import ABC, abstractmethod
import csv
import json

# Create parsers for different formats
csv_parser = CSVParser("data/users.csv")
json_parser = JSONParser("data/config.json")

# Parse files polymorphically
print("=== CSV Parsing ===")
csv_data = csv_parser.parse()
print(f"Parsed {len(csv_data)} records from CSV")
print(f"First record: {csv_data[0]}")
# Output:
# Parsed 3 records from CSV
# First record: {'name': 'Alice', 'age': '30', 'city': 'NYC'}

print("\n=== JSON Parsing ===")
json_data = json_parser.parse()
print(f"JSON data: {json_data}")
# Output:
# JSON data: {'app': 'MyApp', 'version': '1.0', 'debug': True}

# Validation
print("\n=== File Validation ===")
parsers = [csv_parser, json_parser]
for parser in parsers:
    is_valid = parser.validate()
    print(f"{parser.get_extension()} file valid: {is_valid}")
# Output:
# .csv file valid: True
# .json file valid: True

# File information
print("\n=== File Information ===")
for parser in parsers:
    print(f"File: {parser.file_path}")
    print(f"  Extension: {parser.get_extension()}")
    print(f"  Size: {parser.get_file_size()} bytes")
# Output:
# File: data/users.csv
#   Extension: .csv
#   Size: 245 bytes
# File: data/config.json
#   Extension: .json
#   Size: 128 bytes

# Using FileProcessor
processor = FileProcessor()

# Process single file
print("\n=== Processing Single File ===")
data = processor.process_file(csv_parser)
print(f"Processed data: {data}")

# Process batch of files polymorphically
print("\n=== Batch Processing ===")
all_parsers = [csv_parser, json_parser]
results = processor.process_batch(all_parsers)
print(f"Processed {len(results)} files")
for file_path, data in results.items():
    print(f"  {file_path}: {type(data).__name__}")
# Output:
# Processed 2 files
#   data/users.csv: list
#   data/config.json: dict

# Get summary statistics
print("\n=== Processing Summary ===")
summary = processor.get_summary(all_parsers)
print(f"Total files: {summary['total']}")
print(f"Total size: {summary['total_size']} bytes")
print(f"Formats: {summary['formats']}")
# Output:
# Total files: 2
# Total size: 256 bytes
# Formats: ['csv', 'json']

# Auto-detect parser type
print("\n=== Auto-Detection ===")
parser1 = create_parser("data/users.csv")
parser2 = create_parser("data/config.json")

print(f"Auto-detected: {type(parser1).__name__}")  # CSVParser
print(f"Auto-detected: {type(parser2).__name__}")  # JSONParser

# Error handling
try:
    invalid_parser = create_parser("data/file.txt")
except ValueError as e:
    print(f"\nError: {e}")
# Output: Error: Unsupported file format: .txt
```

**Sample Data Files:**

**users.csv:**
```csv
name,age,city
Alice,30,NYC
Bob,25,LA
Charlie,35,Chicago
```

**config.json:**
```json
{
  "app": "MyApp",
  "version": "1.0",
  "debug": true,
  "settings": {
    "timeout": 30,
    "retries": 3
  }
}
```

**Key Polymorphism Concepts:**
- **Format independence:** Same interface works for CSV, JSON
- **Transparent processing:** FileProcessor doesn't care about format
- **Easy extension:** Add YAML, TOML, INI parsers without changing existing code
- **Factory method:** Auto-create correct parser based on file extension
- **Uniform error handling:** All parsers validate consistently

**Challenge Extensions:**
- Add `YAMLParser` and `TOMLParser` classes
- Implement `write(data)` method to save parsed data back
- Create `convert_format(source_parser, target_format)` function
- Add data transformation: `transform(data, transformer_func)`
- Implement caching to avoid re-parsing same files
- Add `get_schema()` method that returns data structure
- Create `merge_files(parsers)` that combines data from multiple files
