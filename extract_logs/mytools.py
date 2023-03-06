__author__ = "Satiya WaraPutra"
__version__ = "1.0"
__maintainer__ = "Satiya WaraPutra"
__email__ = "satiya_wp@yahoo.com"

import argparse
import json


class LogExtractor:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='CLI Tool to extract log files from Linux file system')
        self.parser.add_argument('logfile', type=str, help='Path to the log file')
        self.parser.add_argument('-t', '--type', type=str, choices=['text', 'json'], default='text',
                                 help='Type of output: text or json')
        self.parser.add_argument('-o', '--output', type=str, help='Path to the output file')

    def extract_log(self):
        args = self.parser.parse_args()
        with open(args.logfile, 'r') as f:
            logdata = f.read()

        if args.type == 'json':
            logdata = {'logdata': logdata}
            logdata = json.dumps(logdata)

        if args.output:
            with open(args.output, 'w') as f:
                f.write(logdata)
        else:
            print(logdata)


if __name__ == '__main__':
    log_extractor = LogExtractor()
    log_extractor.extract_log()
