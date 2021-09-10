class Menu:

    # program instruction
    # telling user what to input to initiate the crawling session
    def __init__(self):
        print('Scrapper for carlist website')
        print('Please key in the state wanted to crawl')
        print('Supported state: ')
        print('0: Whole Malaysia, 1: Selangor, 2: Penang, 3: Perak, 4: Kuala Lumpur, 5: Johor, 6: Sarawak, and 7: Sabah')

    # to receive user input from keybaord
    # the input is integer that represent which popular state to
    # start to crawl
    def input(self):
        while True:
            state = input('Enter the popular state to crawl using the index key as stated in menu: ')

            if int(state)>7:
                print('Please ensure the input is coorect')
                continue
            else:
                return (int(state))

    # match user input index to the desire popular state
    # 0: Whole Malaysia, 1: Selangor, 2: Penang, 3: Perak, 4: Kuala Lumpur, 5: Johor, 6: Sarawak, and 7: Sabah
    def match_state(self, state_index):
        return {
            0: 'malaysia',
            1: 'selangor',
            2: 'penang',
            3: 'perak',
            4: 'kuala_lumpur',
            5: 'johor',
            6: 'sarawak',
            7: 'sabah'
        }.get(state_index, 'malaysia')
