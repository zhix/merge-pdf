# PDF Merger

A simple and robust tool to merge multiple PDF files into a single document based on a specified order.

## Features
- **Custom Order**: Merges PDFs strictly according to `order.txt`.
- **Validation**: alerts you if files listed in the order are missing.
- **Progress Tracking**: Shows a progress bar during the merge process.
- **CLI Support**: Customizable input/output paths via command line arguments.

## Installation

1. **Clone or Download** this repository.
2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage
Ensure you have a `pdfs` folder with your files and an `order.txt` listing the filenames (one per line). Then run:

```bash
python main.py
```

### Advanced Usage (CLI)
You can specify custom paths:

```bash
python main.py --folder my_invoices --order list.txt --output combined.pdf
```

## Input Format (`order.txt`)
The `order.txt` should contain exact filenames, one per line:
```text
cover.pdf
chapter1.pdf
chapter2.pdf
...
```

## License
MIT
