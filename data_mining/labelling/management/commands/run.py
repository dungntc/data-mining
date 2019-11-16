from django.core.management.base import BaseCommand
from django.db import connections
from data_mining.labelling.models import Label
import re
import codecs
import os
import string

class Command(BaseCommand):
    help = 'Count'

    def handle(self, *args, **options):
        try:
            count = 0
            matchAll = 0

            input1 = 'data/predlabel.txt'
            input2 = 'data/predlabel2.txt'
            input3 = 'data/predlabel3.txt'
            input4 = 'data/predlabel4.txt'
            contentInput = 'data/preptest.txt'

            output = 'data/out.txt'

            if os.path.exists(output):
                os.remove(output)
            with codecs.open(output, 'a', 'utf-8') as o:
                with open(input1, 'rb') as i1:
                    with open(input2, 'rb') as i2:
                        with open(input3, 'rb') as i3:
                            with open(input4, 'rb') as i4:
                                with open(contentInput, 'rb') as ic:
                                    while True:
                                        line1 = i1.readline()
                                        line2 = i2.readline()
                                        line3 = i3.readline()
                                        line4 = i4.readline()
                                        lineContent = ic.readline()

                                        if line1 and line2 and line3 and line4 and lineContent:
                                            count = count + 1
                                            line1 = line1.decode('utf-8').strip()
                                            line2 = line2.decode('utf-8').strip()
                                            line3 = line3.decode('utf-8').strip()
                                            line4 = line4.decode('utf-8').strip()
                                            lineContent = lineContent.decode('utf-8').strip()
                                            check_good = 0
                                            result = ''
                                            if line1 == line2 and line2 == line3 and line3 == line4:
                                                matchAll = matchAll + 1
                                                check_good = 1
                                                result = line1
                                            label = Label(
                                                line = count,
                                                option1 = line1,
                                                option2 = line2,
                                                option3 = line3,
                                                option4 = line4,
                                                content = lineContent,
                                                result = result,
                                                is_good = check_good
                                            )
                                            label.save()
                                        else:
                                            print('input: ' + str(count) + ' line')
                                            print('matchAll: ' + str(matchAll) + ' line')
                                            o.close()
                                            i4.close()
                                            i3.close()
                                            i2.close()
                                            i1.close()
                                            print('done')
                                            return True
        except Exception as e:
            print('error: ' + str(e))
            return False
        print('call')


