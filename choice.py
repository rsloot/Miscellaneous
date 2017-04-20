from random import choice


def main():
    s = input('What are you having trouble deciding on? ').strip().split(' ')
    print('Go with: %s' % choice(s))

if __name__ == '__main__':
    main()