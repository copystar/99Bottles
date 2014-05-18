def plureler(word, amount):
    ''' adds s to a word to make it plurel''' 
    
    if amount == 1:
        return word
    else:
        return word + 's'

def sing(rounds):
    ''' function will sing 99 Bottles of Beer for as many rounds as given'''
    
    for num in range(rounds, 0, -1):
        print str(num) + ' ' + plureler('bottle', num) + ' of beer on the wall! ' + str(num) + \
        plureler(' bottle', num) + ' of beer! Take one down! Pass it around! ' + str(num - 1) + ' bottles of beer on the wall! '
           
sing(5)
