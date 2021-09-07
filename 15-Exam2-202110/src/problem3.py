"""
Exam 2, Problem 3

Authors: David Mutchler, Sana Ebrahimi, Mohammad Noureddine, their colleagues,
         and Jordan Asman
"""  # DONE: 1. Put your name in the line above

import testing_helper
import time


def main():
    """ Calls the TEST functions for this module """
    print()
    print("--------------------------------------------------")
    print("Un-comment the tests one by one")
    print("as you work the problems.")
    print("--------------------------------------------------")
    run_test_problem3a()
    run_test_problem3b()

def run_test_problem3a():
    """ Tests the problem3a function """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem3a   function:")
    print("--------------------------------------------------")

    format_string = "    problem3a( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    expected = 4
    argument = "hello"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 2
    expected = 4
    argument = "hellO"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 3
    expected = -1
    argument = ""
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 4
    expected = -1
    argument = "hjlr"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 5
    expected = 0
    argument = "abc"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 6
    expected = 12
    argument = "MJahegTYiXOVoJvwJpKK"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 7
    expected = 97
    argument = "NTsMxHGwwcCbCiADLBbItQbDSplTiFzgZHJpABdoKZSUtyNngtJBpoklghxntJDnKkILOCzcKFFPKyUZQaWyQiUfFHUWojiijaMg"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 8
    expected = 51
    argument = "HsgKbSKOqDjlgTYtVlZLYGfecfEIPyeYEZEIeZXHEYErpCNNwOgaHHdrrQmHsZQJflFsFcfLyx"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 9
    expected = -1
    argument = ""
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 10
    expected = 21
    argument = "hBUYfstqNkXOEMAsQmxMlup"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 11
    expected = 40
    argument = "QZTkRtcSEjktbSAWuGHtlDSBlyzqLcmeJCRMGyEBeBZk"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 12
    expected = 52
    argument = "hIKsrDoQaulCdWPqwSrrbcHSrOQyPwazvHOctOnDDSgxXcOYZRjaADPfJxWyl"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 13
    expected = 75
    argument = "mOoZHRyhXgaIswczFBIoxruYLQJQOjNIaEadjgYAEXuiVEGPUOGAzuNamhiBTfkVyqgfAWhVvBWu"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 14
    expected = 32
    argument = "DtwsswnwOGLkhVGQjjTnmxmEbLNWGgvreg"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 15
    expected = 25
    argument = "GkUrmvLiPNdUDfSCLshKRaPDHaFkDl"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 16
    expected = 2
    argument = "XRIlCqv"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 17
    expected = 81
    argument = "OKQFeevMycxLegnEebzeJyolQIuvXUuiqrlQxhMajMzcfBbcxntUObMGqFxXhdnxakXHyFhzmlRbFvpzVi"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 18
    expected = 88
    argument = "MWwiKFfULYDkLsFepNIXXitgdhujfcMORgwvqMpEDRPApSHIcaftPqmuxImmUxXEgsIOJgKoRjjcpMWhTjMFwmQzezl"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 19
    expected = 71
    argument = "KNGRnFKpOHZVnvnoBQfQHzIHQGYXNmEroSuaqkrLYVILvPJziGzkMiBrTIPNiDBUdeQnAdKAhJ"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 20
    expected = 84
    argument = "ZFTZDSNoMtYkSAtXoJtKFYcQfTrGXZcJjMbAgzpicHcsJuBstxCpInfnQEdDkVcYFLBfwlvcZUKpqSWSDpbgivkTvHTjd"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 21
    expected = 5
    argument = "mmmmmA"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 22
    expected = 0
    argument = "A"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 23
    expected = 1
    argument = "aA"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 24
    expected = 2
    argument = "aAe"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 25
    expected = 0
    argument = "a"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 26
    expected = 0
    argument = "e"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 27
    expected = 0
    argument = "i"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 28
    expected = 0
    argument = "o"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    # Test 29
    expected = 0
    argument = "u"
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3a)

    print_summary_of_test_results(test_results)


def problem3a(s):
    """
    Find the LAST index of a vowel in a string.

    What comes in:
        - A string s
    What goes out:
        - Returns an integer representing the index of the LAST vowel
          in the string.
            - If the string is empty or contains no vowels, then
                this function returns -1.
    Side effects: None.
    Recall that vowels are a, e, i, o, u and you look for them
      CASE INSENSITIVE.
    Examples:
        problem3a("hello"): returns 4 since the last vowel is 'o' and appears
         at index 4.

        problem3a("hellO"): returns 4 also since we check vowels case
         insensitive so 'O' is also a vowel.

        problem3a(""): returns -1 since the string is empty.

        problem3a("hgrjl"): return -1 since there are no vowels.

    Type hints:
      :type s: str
      :rtype: int
    """
    vowel_index = []
    for k in range(len(s)):
        letter = s[k].lower()
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            vowel_index = vowel_index + [k]
    if len(vowel_index) > 0:
        return (vowel_index[-1])
    return -1
    ###########################################################################
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################


def run_test_problem3b():
    """ Tests the problem3a function """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem3b   function:")
    print("--------------------------------------------------")

    format_string = "    problem3b( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    expected = "ae"
    argument = ["abc", "def"]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 2
    expected = ""
    argument = ["", "bhj", "rst"]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 3
    expected = "oO"
    argument = ["Hello", "wOrld"]
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 4
    expected = "IE"
    argument = ['PwfWyUJLkXqtZdfglweKlqqAItPaTOriozuFKwoKhvguddjIJZSJq',
                'QxqZBIloWKvxWYzGXXEXOxAoupfCPjztxrpAAfIJhruzHhAkRrfDE']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 5
    expected = "iUEuaoUioo"
    argument = [
        'yhKSIcRaDOffzZdXYJkiXoiWqTBVoIKpYGFcGEUDDBseReWyzhEMJlTSWxxDziAwvAhsyTmJyxDmcATxVxdIvBpRkqzQrQijbYJG',
        'rroUgTdyeMtxpiiCVjdqprsNoYqTowKolxQMDsDhmhrnthVnWKJrYWAdjCxVSeOwDVQabwUIyIRwvWTqUjQItVGagPDXHMcarDOU',
        'hwLoVXTChAYUVSEUaJxuHwhcVrgnoMceXbwvoibycbdmpGJmRoJbwtrQSWOIMFlaYbEsrbfoUklVYhXHMSJpmkiHpgrEppWrYKFk',
        'JgPFBHAoMPJpfdHAlHNftkzvzxxSPvkeYIEoOdkfpERPEOJJogitdxmeakARbLZEublqzRggPWzYtRqXmjhqMNDltZHgPrLHFdur',
        'ilwwiZqnceZlZUEeaNOeXnDMnmEsRjqqnaTPnlNHuMHpOWoaSuOsZdwhzITLAQDagEOhcYFPLyefCCFfaRKMbGCSGHqWwdRCVMyl',
        'MvWelEqmRmVVcTKmRhtabSDzyzzgicKgDutWtEOijfiXvKoJzLybKGhcCOKSWkEpDVUgXBcIKoTChGVveOJSKzCezmlLSXwmoZfx',
        'sLsgOZOKoMHGOCVfOKKsqGrtbCgnvDUZhMJDRbChsLPRnDPWXKFEmonGjgrPAulPGCVJCpzGPXtZQywlZTnavtObyWKQSOqNFUWf',
        'DSTyZAOKXKABgCSBqsVRJHTeZvTjZUMAoITRUTINGmFQSZyewdKQFcKjGJCriAwijUpNmhzvCYjeaSEWEAELXsBhNqbNQiDQBprJ',
        'aqDjytNUvFFMtTVuWWJFhjkHDIlooaLUPEGkrYtObKQvfMOmmDkkgCTpiYpumUMFWymRSxqzAyKBAqpUAMnzaxWCFGGmuzodloSB',
        'omjGToypXNVkWXXkJGsttIEvUovXQUpgFwfnwRSwspCPFSJYnznpKlncpmcpbUoKOKLPjRkwrvgQLKGcWfGofHqkxxpxvbYwMMhJ']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 6
    expected = "IeuO"
    argument = [
        'GNdWKClFZscRLxSLNUXeomxhmjAuWlVUeablqKNNCqeWaXZwsbyUQfgwVgxiOsGtWMWtISHIIaaswxbyKImGpHsQnTYzd',
        'qbpwWjcqCJYhUxfgLdsmmBrHUyHSVTkusDlWWQvDqkucOJsQcPHGSkIbNPdgiaITdVgdcgZrIDzZtIskIpmbhhtcytjMe',
        'tIpqhOuSRQDGnQOeUphwGKunCWuMjXyToMnhqXjDJKdMkFcApeOISfCqEMBdQUsRCweHAIKlzjpfaUPjKKiLnHXTuCnWW',
        'EfKEForHlDHUcdjWWOYOrxANmgZwOFLqDxkCyGYvEzWBaxeVuKIHJLxuuaJJMZuddHqWOdtwsSgwZasfkMYpALDFGPfOd']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 7
    expected = "eoII"
    argument = ['yxbYRgHiNHWyTccbVlipwelcqe', 'jnxScgQZCskeFvdCxoevPfnoMt',
                'URdRwdcmcWzIBpXdBtvDyMkhdZ', 'NcVWmwlAVgumEvhuKnuIrcPWSQ']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 8
    expected = "iEIueo"
    argument = [
        'LKEZnHbWdaCvUSnmPYqNNXFGDsexYxqFxicsZaDHPufKxVpVztrQbFyOBpFnHbJSOhWcainFfnrNFomgiZPRnzbnc',
        'asAaOKrmbffLosAREcFMJPVOWqdRMmRZgYxzoIgwufcaMleJvuhBxDYXyaTPWbfgSwvfUxYIeyLiZznjmHrKpKEBx',
        'mTMCgxZzrFaBlJxotSjpCEMKZiSuinrbZFVBTxDvohuyKfhzpWNnPwYwbNoAaDhhrVrgvDpFexKNNpaTHOJKEPuiI',
        'mkwMQmrhQHoYrzZrnjTMEcjYgJzsMLmSEOzUMyZIHGVSLAKOiNyjnswgZkJqQVBhiBkeyEhrcHdetAwdTFaYRuXjx',
        'bBHiVxcEUGKHCFztsrnqSPjjtlGtFDjwJMYqgBOfrSxiUukNQzDkGwrWYPHMWkPVJSZKFhowzWvXnjiAZfqIVScej',
        'coQPiQHIwiRtIvIfNYMluVFEHNzmuerwMQQbMBfPZnUZbpEyHPzRSpFQlDSQBtTdvjqcmCfWmFoymwKbWoQdPtTGw']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 9
    expected = "oEOE"
    argument = ['osX', 'tOE', 'YmD', 'vOq', 'EFp', 'xWQ', 'jXy', 'BlP']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 10
    expected = "ouii"
    argument = [
        'WzVwLsvrAGmiQhlElEMmBGbaEJQCtHEutBPcVGNHrHBtCoocUQnNMSymgzZVouokLbbnbRbwS',
        'SxOzxeQiNAehufTFtvIvlUcDZGmFpJYcuOHhIfgMHoETfHvfsHkmxLXxunnmlQMwTWSTcgvhP',
        'OSAQdeUwVtHMivSJjBEWOaQMNFJMTKXldgvqQZAHaQoWgKKcVBVKNxqhaxubWkiWljDKvyqRL',
        'HJWYjApCKxIcfyNiHwqijTNkbOJYClNOkzFRUmJyqGzLUniiHSDBwGZRDrXJOisriVMNCrggh']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 11
    expected = "oeIiieu"
    argument = [
        'gAFZuxYYVedupUAamzEGUCaHYyrFmbFeHyVfDHvThnvrbpIoivarQqRYUjiPLrIUoHxWvf',
        'FAAadGfDdhuInkDskmvGSWCvewfxFlEEifdwKAwNUbbDogOeoVaUOjjbTacJrEdCXtuSeh',
        'wYsUzzRNSSpNbLnEkXlkyyuNhtWmfKsxtXHbTHBKzCdMuavDZIyFtLdsWcFHMnlcGfVqjd',
        'WLRDPzvaZcormhjsUhmMlNAuYOYsAUtftabQKkoKUomFJPDKhVnKtzyVPLURihATfRWeis',
        'AaPGoLgzVBTYHFoEevHqckVJnSfGXdvvLTujyJBQoKDOGNmjSEFeLElPIMUlIRMcNHKOiC',
        'sBZKCfXyKorWlFBWWxlsovbMUWjMOjWHsdTHgxoxunjJkRwStJXsIDeCxQKwwxkRPbwLdg',
        'euVmAqCwlWOaBawmizydCckwxVUIXHuxOXxnprxtPwFyswkBuzaxtoRBMxAaNMfMgxnruF']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 12
    expected = "uiAi"
    argument = [
        'szOTiCxVeyRMcXcOekiLjHkAolfKnuWfAoMtsFsEUDveBIjpWOxQrjbHiQRSgKFyZKulOZhFdMxnPFBLHcKdfuyzF',
        'jkHIZniNtLqeSUEmXGwgDGAPvVYwSoLaKXNOlmxjMEwJQPSWmWsDnrdojOfyJrTMlhRepXEVGMLsSHkHRidplxiKX',
        'VwZcgVRcyaXqWOpXmLAjQwdGbjQfzzZSTWtUqYJmmgHMVlLFXsGvjzojYVAuGYPQJtpwFXDOEgVtdOxllAxzyStAD',
        'LvPjCfCkpMAkEGQxXAkUgJvYPjnLstesNuSyvgYUQgXKZrKSwGNOKzZrBhadgUQRZxKuFZLryQwoSjmHbzidWiyWY']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 13
    expected = "UIoeuE"
    argument = ['rUOTXFjJopSsqKRuevVbikngKecHLGraTGZDdsCXzmOcHhLeSLaWpNOUfW',
                'peXkhftELewxejfIBHAlsXaNYEeOSpePHOUqaoXQWgFcPsmOgqLPcWwTIY',
                'CDiWTAYJGOnyfgihJnyXdfOCQbBIgWRcTTrkvnNqgOlCXShBktvdtyKpoY',
                'JAoVokYXTqinOCMmBEmLXkKaIBPfWEKobgawRkjDuYaicZMkcOyIeVfrMR',
                'yOtJmXFvQUtNmzpwsqAtaMJiNfIvRrAvorWWLekahYtKswTpWeRtiNODGu',
                'ApywcUGrwXwqCuLrGrKeWuzroYCBrYNVNvOHjFHbmsbIiMYJkixxbXVEFj']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 14
    expected = "AaaO"
    argument = ['LOERVMpyPSetJRWtCYZbjVkQOuOxWMDRIXywDUSgApWghWpPH',
                'pOIrYjhgznYehsZOljgqoEIOCzfWmELQAjWCPnCabbYVWTWQm',
                'FWXHhfKeeilZhYDardoIPcHluxOVMHMYJsANLtgUIYrTbabKg',
                'ENMdffMkayPdJyPWGZPhhTGubZlCycoutnapVrnBeSPOcMHnf']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 15
    expected = "IOi"
    argument = [
        'EvGOUzrDdSNuZZapQpgsHfxkMZkrxPVKulXCSSrrqarrtBrYGZMLUcyVKdvdaI',
        'OjBJLxdcskjmASNyTaXyrQSxuVFHoiRbqWaXXsuyUhlGOBPZKVNbZltqmzFzlm',
        'ziHqACrkAQbqvWcojyVOGCNmaAdIzsYxVRXLRhHlFuqBKxdOpNjZIDqlCZKizL']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 16
    expected = "OeUUU"
    argument = ['uhcO', 'Uepb', 'LVFn', 'zfYb', 'UqxY', 'FGKv', 'AZkU', 'WFYg',
                'ZkUj']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 17
    expected = ""
    argument = []
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 18
    expected = "aOEa"
    argument = ['wa', 'pO', 'Eh', 'ma', 'wG']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 19
    expected = "iee"
    argument = ['DXxnURobbZFwQtNprCewIumZXfcViGKM',
                'bDmOHnPACONCFSImQMPYYFeXfgdTbIqe',
                'xOGmeypTyciDlncspGvzaKaflirOGOPe']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    # Test 20
    expected = "I"
    argument = ['mmVsKGFIBMqzeHJtajHsXCSZKlUgpKDLWEdCI']
    run_and_print_test([argument], expected, test_results, format_string,
                       problem3b)

    print_summary_of_test_results(test_results)


# Be sure to read the IMPORTANT note in the following specification!
def problem3b(list_of_strings):
    """
    Concatenate the last vowel from each string in a list of strings.

    What comes in:
        - A list of strings
    What goes out:
        - A string that represents the concatenation of the last vowel from
          each string in the list
    Side effects: None
    Examples:
        problem3b(["abc", "def"]): returns "ae" since a is the LAST vowel in
        the first string in the sequence and e is the LAST vowel in the second
        string in the sequence.

        problem3b(["", "bhj", "rst"]): returns "" since none of the strings
        in the sequence contain any vowels.

        problem3b(["Hello", "wOrld"]): returns "oO" since o is the last vowel
        in the first string of the sequence and O is the last vowel in the
        second string of the sequence.

    #   IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   appropriate   function(s) that are DEFINED ABOVE.

                ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **

    Type hints:
    :type list_of_strings: list[str]
    :rtype: str
    """
    last_vowels = ""
    for k in range(len(list_of_strings)):
        word = list_of_strings[k]
        vowel = problem3a(word)
        if vowel > -1:
            last_vowels = last_vowels + word[vowel]
    return last_vowels
    ###########################################################################
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   appropriate   function(s) that are DEFINED ABOVE.
    ###########################################################################


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


def run_and_print_test(args, expected, test_results, format_string, function):
    print_expected_result_of_test(args, expected, test_results,
                                  format_string)
    actual = function(*args)
    print_actual_result_of_test(expected, actual, test_results)


if __name__ == '__main__':
    # To allow color-coding the output to the console:
    USE_COLORING = True  # Change to False to revert to OLD style coloring

    testing_helper.USE_COLORING = USE_COLORING
    if USE_COLORING:
        # noinspection PyShadowingBuiltins
        print = testing_helper.print_colored
    else:
        # noinspection PyShadowingBuiltins
        print = testing_helper.print_uncolored

    # --------------------------------------------------------------------------
    # Calls  main  to start the ball rolling.
    # The   try .. except   prevents error messages on the console from being
    # intermingled with ordinary output to the console.
    # --------------------------------------------------------------------------
    try:
        main()
    except Exception:
        print("ERROR - While running this test,", color="red")
        print("your code raised the following exception:", color="red")
        print()
        time.sleep(1)
        raise
