def analyze_code(lines):
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

    return {
        "total_lines": total_lines,
        "blank_lines": blank_lines,
        "comment_lines": comment_lines,
        "functions": function_count,
        "classes": class_count,
        "complexity": complexity
    }