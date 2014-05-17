def sing(rounds):
    ''' function will sing 99 Bottles of Beer for as many rounds as given'''
    
    while rounds > 1:
        print str(rounds) + ' bottles of beer on the wall! ' + str(rounds) + \
        ' bottles of beer! Take one down! Pass it around! ' + str(rounds - 1) + ' bottles of beer on the wall!'
        rounds = rounds -1
        
    print '1 bottle of beer on the wall! 1 bottle of beer! Take one down! Pass it around! No bottles of beer on the wall!'
sing(99)
