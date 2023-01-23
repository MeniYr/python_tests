import datetime
import os


class Exceptions_logs:
    def __init__(self):
        os.chdir("C:\Python\paiCharm\Car")

    def send(self, e):

        try:
            f = open('log.txt', 'a')
            if f.tell() > (1000 * 1024):
                raise ValueError(f'file is up to 1000kb {f.tell()}, open new file')
            else:
                date = datetime.datetime.now()
                f.write(f"""
name: Meni Rotblat.
date: {date.now()}. 
description: {e}.
                     """)
                f.flush()
        except Exception as e:
            print(e)
        finally:
            f.close()
