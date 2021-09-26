'''Test di unità per plural6.py'''

import plural6
import unittest

class KnownValues(unittest.TestCase):
    def test_sxz(self):
        'parole che finiscono con S, X, o Z'
        nouns = {
            'bass': 'basses',
            'bus': 'buses',
            'walrus': 'walruses',
            'box': 'boxes',
            'fax': 'faxes',
            'suffix': 'suffixes',
            'mailbox': 'mailboxes',
            'buzz': 'buzzes',
            'waltz': 'waltzes'
            }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_h(self):
        'parole che finiscono con H'
        nouns = {
            'coach': 'coaches',
            'glitch': 'glitches',
            'rash': 'rashes',
            'watch': 'watches',
            'cheetah': 'cheetahs',
            'cough': 'coughs'
            }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_y(self):
        'parole che finiscono con Y'
        nouns = {
            'utility': 'utilities',
            'vacancy': 'vacancies',
            'boy': 'boys',
            'day': 'days'
            }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_ouce(self):
        'parole che finiscono con OUSE'
        nouns = {
             'mouse': 'mice',
             'louse': 'lice'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_child(self):
        'caso particolare: child'
        nouns = {
             'child': 'children'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_oot(self):
        'caso particolare: foot'
        nouns = {
             'foot': 'feet'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_ooth(self):
        'parole che finiscono con OOTH'
        nouns = {
             'booth': 'booths',
             'tooth': 'teeth'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_f_ves(self):
        'parole che finiscono con una F che diventa VES'
        nouns = {
             'leaf': 'leaves',
             'loaf': 'loaves'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_sis(self):
        'parole che finiscono con SIS'
        nouns = {
             'thesis': 'theses'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_man(self):
        'parole che finiscono con MAN'
        nouns = {
             'man': 'men',
             'mailman': 'mailmen',
             'human': 'humans',
             'roman': 'romans'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_ife(self):
        'parole che finiscono con IFE'
        nouns = {
             'knife': 'knives',
             'wife': 'wives',
             'lowlife': 'lowlifes'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_eau(self):
        'parole che finiscono con EAU'
        nouns = {
             'tableau': 'tableaux'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_elf(self):
        'parole che finiscono con ELF'
        nouns = {
             'elf': 'elves',
             'shelf': 'shelves',
             'delf': 'delfs',
             'pelf': 'pelfs'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_same(self):
        'parole che sono il loro stesso plurale'
        nouns = {
             'sheep': 'sheep',
             'deer': 'deer',
             'fish': 'fish',
             'moose': 'moose',
             'aircraft': 'aircraft',
             'series': 'series',
             'haiku': 'haiku'
             }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_default(self):
        'parole comuni'
        nouns = {
            'papaya': 'papayas',
            'whip': 'whips',
            'palimpsest': 'palimpsests'
            }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)
        
if __name__ == '__main__':
    unittest.main()

# Copyright (c) 2009, Mark Pilgrim, All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
