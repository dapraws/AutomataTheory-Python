# Python Syntactic Analyzer for Grammar Validation

This Python script serves as a syntactic analyzer, evaluating the structure of a given sentence against predefined grammar rules. It analyzes various components within the input sentence, such as conditional statements, Boolean expressions, mathematical operations, and control flow structures.

## How the Analyzer Works

### Input Processing

- Accepts a sentence input.
- Divides the sentence into individual words and stores them in a list.

### Parsing and Evaluation

- Iterates through each word in the input sentence.
- Checks words against predefined grammar rules.
- Identifies conditional statements (`if`), Boolean expressions, mathematical operations, and control flow structures (`{}`).
- Constructs separate lists to track labels, conditions, and actions based on recognized components.

### Grammar Validation

- Validates identified components against predefined grammar rules.
- Checks if conditions and actions adhere to defined grammar for Boolean expressions and mathematical operations.
- Validates structure and sequence of labels, conditions, and actions for compliance with specified grammar.

### Stack-based Validation

- Utilizes a stack-based approach to verify the sentence's syntactic correctness.
- Validates sequence of recognized labels, conditions, and actions against expected control flow structures.
- Determines whether parsed sentence conforms to specified grammar rules.

### Result Display

- Outputs message indicating if input sentence adheres to defined grammar rules.
- Displays confirmation of sentence's syntactic correctness or indicates encountered syntax errors during evaluation.

## Usage

1. **Run the Analyzer:**
   - Input a sentence when prompted.
   - Execute the script to validate sentence against predefined grammar.

2. **Interpreting Results:**
   - Upon completion, script displays if input sentence conforms to grammar rules.
   - Review output to determine if provided sentence has syntactically correct structure based on specified grammar.

## Notes

- Script uses predefined grammar rules to evaluate syntactic correctness of input sentence.
- Ensure input sentence adheres to defined grammar for accurate validation results.
