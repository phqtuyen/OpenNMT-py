
def eval(f1, f2):
    c = 0
    total = 0
    with open(f1) as file1, open(f2) as file2:
        for line1, line2 in zip(file1, file2):
            if line1.strip() == line2.strip():
                c += 1
            total += 1
    print(float(c) / float(total))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "compare pred and test label")
    parser.add_argument("--pred", dest = "predFilePath", help = "path to pred file")
    parser.add_argument("--test", dest = "test", help = "path to test label")
    args = parser.parse_args()
    eval(parser.pred, parser.test)