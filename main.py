import argparse

list_of_interest = {
    'chr1',
    'chr2',
    'chr3',
    'chr4',
    'chr5',
    'chr6',
    'chr7',
    'chr8',
    'chr9',
    'chr10',
    'chr11',
    'chr12',
    'chr13',
    'chr14',
    'chr15',
    'chr16',
    'chr17',
    'chr18',
    'chr19',
    'chr20',
    'chr21',
    'chr22',
    'chrX',
    'chrY'
}


def main(input_path: str, output_path: str):
    with open(input_path) as input_file, open(output_path, 'w') as output_file:
        for line in input_file:
            if not line.startswith("@SQ"):
                continue

            name = None
            length = None
            for element in line.split("\t"):
                if element.startswith("SN:"):
                    name = element[3:]
                elif element.startswith("LN:"):
                    length = int(element[3:])
            if name in list_of_interest:
                output_file.write("{0}\t0\t{1}\n".format(name, length))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="From a reference's dict file, a bed file mapping to the entirety of "
                                                 "the relevant sequences is generated.")
    parser.add_argument('input', help='Input file name')
    parser.add_argument('output', help='Output file name')
    args = parser.parse_args()

    main(args.input, args.output)
