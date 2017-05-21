#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

sys.path.append('../../../')
sys.path.append('../../../../')
from prepare_path import Prepare
from labels.ctc.dialog.character import read_sdb


class TestCTCLabelDialogChar(unittest.TestCase):
    def test(self):
        prep = Prepare()
        label_dialog_core_paths = prep.trans(data_type='dialog_core')
        label_dialog_non_core_paths = prep.trans(data_type='dialog_noncore')

        print('===== dialog (character) =====')
        read_sdb(label_paths=label_dialog_core_paths, label_type='character')
        read_sdb(label_paths=label_dialog_non_core_paths,
                 label_type='character')


if __name__ == '__main__':
    unittest.main()
