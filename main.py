import argparse
import sys
from pathlib import Path
from PyPDF2 import PdfMerger

try:
    from tqdm import tqdm
except ImportError:
    # Fallback if tqdm is not installed
    def tqdm(iterable, desc=None, unit=None):
        if desc:
            print(desc)
        return iterable

def validate_paths(pdf_folder, order_file):
    if not pdf_folder.exists():
        print(f"Error: PDF folder '{pdf_folder}' not found.")
        sys.exit(1)
    if not order_file.exists():
        print(f"Error: Order file '{order_file}' not found.")
        sys.exit(1)

def get_pdf_list(order_file):
    with order_file.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def check_orphans_and_missing(pdf_list, pdf_folder):
    existing_pdfs = {f.name for f in pdf_folder.glob("*.pdf")}
    ordered_pdfs = set(pdf_list)
    
    # Missing files (Critical)
    missing = [name for name in pdf_list if name not in existing_pdfs]
    if missing:
        print(f"Error: The following {len(missing)} files listed in order.txt are missing from '{pdf_folder}':")
        for m in missing[:10]:
            print(f" - {m}")
        if len(missing) > 10:
            print(f" ... and {len(missing) - 10} more.")
        sys.exit(1)

    # Orphaned files (Warning)
    orphans = existing_pdfs - ordered_pdfs
    # Exclude output file if it happens to be in there
    if "merged_output.pdf" in orphans:
        orphans.remove("merged_output.pdf")
        
    if orphans:
        print(f"Warning: Found {len(orphans)} PDF(s) in '{pdf_folder}' that are NOT in the order list:")
        for o in list(orphans)[:5]:
            print(f" - {o}")
        if len(orphans) > 5:
            print(f" ... and {len(orphans) - 5} more.")
        print("-" * 30)

def merge_pdfs(pdf_folder, order_file, output_file):
    validate_paths(pdf_folder, order_file)
    
    pdf_list = get_pdf_list(order_file)
    check_orphans_and_missing(pdf_list, pdf_folder)
    
    merger = PdfMerger()
    
    print(f"Merging {len(pdf_list)} files...")
    
    for pdf_name in tqdm(pdf_list, desc="Processing", unit="pdf"):
        pdf_path = pdf_folder / pdf_name
        try:
            merger.append(str(pdf_path))
        except Exception as e:
            print(f"\nFailed to append {pdf_name}: {e}")
            sys.exit(1)

    # Write merged PDF
    print(f"Writing output to {output_file}...")
    with output_file.open("wb") as f:
        merger.write(f)
    
    merger.close()
    print(f"Success! Merged PDF saved at: {output_file.resolve()}")

def main():
    parser = argparse.ArgumentParser(description="Merge PDF files in a specific order.")
    parser.add_argument("--folder", type=Path, default=Path("pdfs"), help="Folder containing PDF files")
    parser.add_argument("--order", type=Path, default=Path("order.txt"), help="Text file with filenames in order")
    parser.add_argument("--output", type=Path, default=Path("merged_output.pdf"), help="Output filename")
    
    args = parser.parse_args()
    
    merge_pdfs(args.folder, args.order, args.output)

if __name__ == "__main__":
    main()
