#!/usr/bin/env python

'''
Basic information retrieval (IR) engine.
'''

def tokenize(text):
    '''
    tokenize(text) -> list
    '''
    t_text = text.split()
    return t_text

def normalize(t_text):
    '''
    normlize(t_text: list) -> list
    '''
    n_text = t_text.lower()
    return n_text

def process_corpus():
    pass


def main():
    pass


if __name__ == "__main__":
    main()