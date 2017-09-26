#!/usr/bin/env/python3
import re
from collections import OrderedDict
import json
import codecs


def handler(f_name):
    tmp_line_num = 0
    target_encoding = 'utf-8'
    try:
        tmp = codecs.open(f_name, 'r', encoding=target_encoding)
        tmp.readlines()
    except UnicodeDecodeError:
        encoding_list = ["ascii",
                         'iso8859_1',
                         "iso8859_2",
                         "iso8859_3",
                         "iso8859_4",
                         "iso8859_5",
                         "iso8859_6",
                         "iso8859_7",
                         "iso8859_8",
                         "iso8859_9",
                         "iso8859_10",
                         "iso8859_13",
                         "iso8859_14",
                         "iso8859_15",
                         "iso8859_16",
                         "johab", "koi8_r", "koi8_u", "mac_cyrillic", "mac_greek", "mac_iceland", "mac_latin2", "mac_roman", "mac_turkish", "ptcp154", "shift_jis", "shift_jis_2004", "shift_jisx0213", "utf_32", "utf_32_be", "utf_32_le", "utf_16", "utf_16_be", "utf_16_le", "utf_7", "utf_8", "utf_8_sig"]
        for e in encoding_list:
            try:
                tmp = codecs.open(f_name, 'r', encoding=e)
                tmp.readlines()
                tmp.seek(0)
            except:
                pass
            else:
                target_encoding = e
                tmp.close()
                break
    finally:
        handled_dict = OrderedDict()
        with codecs.open(f_name, 'r', encoding=target_encoding) as f:
            for line in f.readlines():
                line = line.strip()
                if re.match(r'.*-->.*', line):
                    tmp_line_num += 1
                    handled_dict[tmp_line_num] = []
                if tmp_line_num and re.match(r'.*[:|a-zA-Z].*', line):
                    handled_dict[tmp_line_num].append(line)
            try:
                with open('db.json') as f:
                    origin_data = json.load(f)
                    if not isinstance(origin_data, dict):
                        origin_data = {}
            except:
                origin_data = {}
            finally:
                origin_data[f_name] = handled_dict

            with open('db.json', 'w') as tmp_json:
                json.dump(origin_data, tmp_json)
