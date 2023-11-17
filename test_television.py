from television import Television 

def test_tv_init():
    tv = Television()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

def test_power():
    
    tv = Television()

    tv.power()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    tv.power()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

def test_mute():
    tv = Television()

    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'

    tv.power()
    tv.mute()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 1'

    tv.mute()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 1'

def test_channel_up():
    tv = Television()
 
    tv.power()
    tv.channel_up()
    assert str(tv) == 'Power = True, Channel = 1, Volume = 0'

    
    for _ in range(10):
        tv.channel_up()

    assert str(tv) == 'Power = True, Channel = 3, Volume = 0'
