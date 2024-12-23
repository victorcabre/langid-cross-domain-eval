import sys

def calculate_accuracy(predictions_file, gold_file):
    with open(predictions_file, 'r', encoding='utf-8') as pred_file:
        predictions = pred_file.readlines()

    with open(gold_file, 'r', encoding='utf-8') as gold_file:
        gold = gold_file.readlines()

    if len(predictions) != len(gold):
        raise ValueError("The number of lines in predictions file and gold file must be the same.")

    correct = 0

    for pred, true in zip(predictions, gold):
        pred = pred.strip()
        true = true.strip()

        if pred == true:
            correct += 1

    accuracy = correct / len(predictions) * 100
    return accuracy

if len(sys.argv) != 3:
    print("Usage: python calculate_accuracy.py <predictions_file> <gold_file>")
    sys.exit(1)

predictions_file = sys.argv[1]
gold_file = sys.argv[2]

try:
    accuracy = calculate_accuracy(predictions_file, gold_file)
    print(f"Accuracy: {accuracy:.2f}%")
except Exception as e:
    print(f"Error: {e}")

