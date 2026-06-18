# Email Tool

A Python tool to extract emails from files and validate them using DNS MX records. Supports multi-threading for faster processing on large datasets.

## Features

- Extract emails from text files
- Remove duplicates automatically
- Validate email domains using MX records
- Multi-threaded processing (faster execution)
- Live progress tracking
- Outputs valid and invalid emails separately

## Installation

Install dependencies:

pip install dnspython requests

## Project Structure

emailtool/
├── main.py          Entry point
├── extractor.py     Email extraction logic
├── validator.py     MX validation logic
├── utils.py         Helper functions
└── requirements.txt

## Usage

Run the tool:

python main.py

You will be prompted to enter a file path:

File path: data.txt

## Input Format

Any text file containing emails:

john@gmail.com hello
support@github.com
test.user@domain.com

## Output

After running, two files are created:

valid.txt
invalid.txt

## Example Output

Found 282626 emails

Processed 1000/282626
Processed 2000/282626
Processed 3000/282626

Done
Valid: 145321
Invalid: 137305

## Performance

- Uses ThreadPoolExecutor with 50 workers
- Best for medium to large datasets
- Speed depends on DNS response time

## How It Works

1. Extract emails using regex
2. Remove duplicates
3. Extract domain from each email
4. Query MX records via DNS
5. Cache results to reduce repeated lookups
6. Split into valid and invalid lists

## Limitations

- DNS lookup is network dependent
- Large datasets may take time
- No proxy rotation or distributed processing

## Future Improvements

- Domain-level deduplication (major speed boost)
- Async DNS resolver
- ISP classification
- Export to CSV/JSON
- CLI arguments support

## License

Educational use only