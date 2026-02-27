import sys
from utils import analyze_code

def analyze_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        total_lines = len(lines)
        blank_lines = sum(1 for line in lines if line.strip() == "")
        comment_lines = sum(1 for line in lines if line.strip().startswith("#"))

        function_count = sum(1 for line in lines if line.strip().startswith("def "))
        class_count = sum(1 for line in lines if line.strip().startswith("class "))
        complexity_score = function_count + class_count

        if complexity_score > 10:
            complexity = "High"
        elif complexity_score >= 5:
            complexity = "Medium"
        else:
            complexity = "Low"

        print(f"\nAnalysis of: {filename}")
        print(f"Total Lines: {total_lines}")
        print(f"Blank Lines: {blank_lines}")
        print(f"Comment Lines: {comment_lines}")
        print(f"Functions: {function_count}")
        print(f"Classes: {class_count}")
        print(f"Complexity Level: {complexity}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <filename>")
    else:
        analyze_file(sys.argv[1])