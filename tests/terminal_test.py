# coding: utf-8
# vim: set ts=4 sw=4 expandtab sts=4:


from khal.terminal import merge_columns, colored, bstring, rstring


def test_rstring():
    assert rstring('test') == '\x1b[7mtest\x1b[0m'
    assert rstring(u'täst') == u'\x1b[7mtäst\x1b[0m'


def test_bstring():
    assert bstring('test') == '\x1b[1mtest\x1b[0m'
    assert bstring(u'täst') == u'\x1b[1mtäst\x1b[0m'


def test_colored():
    assert colored('test', 'light cyan') == '\33[1;36mtest\x1b[0m'
    assert colored(u'täst', 'white') == u'\33[37mtäst\x1b[0m'


class TestMergeColumns(object):

    def test_longer_right(self):
        left = ['uiae', 'nrtd']
        right = ['123456', '234567', '345678']
        out = ['uiae    123456',
               'nrtd    234567',
               '        345678']
        assert merge_columns(left, right, width=4) == out

    def test_longer_left(self):
        left = ['uiae', 'nrtd', 'xvlc']
        right = ['123456', '234567']
        out = ['uiae    123456', 'nrtd    234567', 'xvlc    ']
        assert merge_columns(left, right, width=4) == out
