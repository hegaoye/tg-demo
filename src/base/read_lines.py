import logging


def read_line(lines) -> list:
    list = []
    if lines:
        for line in lines:
            line = line.replace('\n', '')
            logging.info(line)
            list.append(line)

    return list
