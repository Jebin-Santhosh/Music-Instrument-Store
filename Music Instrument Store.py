userName = input("Enter Name: ")
print("Welcome ", userName)
flow = True
while flow == True:
    print("Select instrument: ")
    print("1. Drums")
    print("2. Keyboard")
    print("3. Guitar")
    print("4. Piano")
    choice = input()
    if choice == '1':
        drums = {'Beginner': {'Standard': (['Havana HV 522 5Pcs Acoustic Drum Set', 'Rs.21,999'], ['Pearl RSJ465C/C(31) 5 Pcs Drum Set Roadshow Junior - Jet Black', 'Rs.26.999'], ['Ludwig Accent Drive 5 Piece Acoustic Drum Kit With Hardware & Cymbals', 'Rs.31,141']),
                              'ELECTRIC PAD': (['ROCKSTAR PAD20 PRO Rockstar Pad20 Pro 29 Buttons, 8 Pad', 'Rs.20,970'], ['Roland SPD-20X Digital Percussion Pad- Black', 'Rs.42,850'], ['Alesis Compact Kit 7 | 7-Pad Electronic Table-top Drum Kit with Velocity-Sensitive Drum Pads, USB-MIDI Output and Drum Sticks Included', 'Rs.17,634'], ['Alesis SamplePad | Multi-Pad Sample Instrument with Velocity Sensitive Pads, Drum Sounds and SD Card Slot (Black)', 'Rs.11,858'], ['Alesis SamplePad Pro | 8-Pad Percussion and Sample-Triggering Instrument with Dual Zone Rubber Pads, Blue LED Illumination, and Built-in Sounds (Black)', 'Rs.31,999']),
                              'PRACTICE PAD': (['INDIROCK 8" DUAL SIDE DRUM PRACTICE PAD + BAG+DRUMSTICKS', 'Rs.549'], ['worldmacs 12'' Inches 2 Sided Drum Practice Pad + Bag + Drumsticks', 'Rs.902'], ['Clapbox CB-PPD Drum Practice Pad - 12 inches, Black (Practice pad only)', 'Rs.902'])},
                 'Pro': {'ELECTRIC PAD': (['Roland SPD-30 Version 2 Octopad Digital Percussion Pad, Black', 'Rs.56,233'], ['Roland SPD-SX Special Edition', 'Rs.62,786'], ['Yamaha DTXM12 Multi Pad', 'Rs.45,591']),
                         'STANDARD DRUMS': (['TAMA IP58NCMNB Imperialstar 5-Piece Drum Set with Cymbals (18" Bass Drum)', 'Rs.55,408'], ['Pearl Masters Maple Complete MCT924XEDP/C348 4 Piece Drum Shell Pack, Absinthe Sparkle', 'Rs.1,23,869'], ['Pacific Drums PDCM2014PW 4-Piece Drumset With Chrome Hardware - Pearlescent White', 'Rs.67,617'])}}
        print("Select: ")
        print("1. Beginner")
        print("2. Pro")
        choice1 = input()
        if choice1 == '1':
            print("Select: ")
            print("1. Standard")
            print("2. Electric pad")
            print("3. Practice pad")
            choice2 = input()
            if choice2 == '1':
                print("Select: ")
                print("1. ", drums['Beginner']['Standard'][0][0])
                print("2. ", drums['Beginner']['Standard'][1][0])
                print("3. ", drums['Beginner']['Standard'][2][0])
                choice3 = input()
                if choice3 == '1':
                    print("Instrument: ", drums['Beginner']['Standard'][0][0])
                    print("Price: : ", drums['Beginner']['Standard'][0][1])
                elif choice3 == '2':
                    print("Instrument: ", drums['Beginner']['Standard'][1][0])
                    print("Price: ", drums['Beginner']['Standard'][1][1])
                elif choice3 == '3':
                    print("Instrument: ", drums['Beginner']['Standard'][2][0])
                    print("Price" , drums['Beginner']['Standard'][2][1])
                else:
                    continue
            elif choice2 == '2':
                print("Select: ")
                print("1. ", drums['Beginner']['ELECTRIC PAD'][0][0])
                print("2. ", drums['Beginner']['ELECTRIC PAD'][1][0])
                print("3. ", drums['Beginner']['ELECTRIC PAD'][2][0])
                choice3 = input()
                if choice3 == '1':
                    print("Instrument: ", drums['Beginner']['ELECTRIC PAD'][0][0])
                    print("Price: ", drums['Beginner']['ELECTRIC PAD'][0][1])
                elif choice3 == '2':
                    print("Instrument: ", drums['Beginner']['ELECTRIC PAD'][1][0])
                    print("Price: ", drums['Beginner']['ELECTRIC PAD'][1][1])
                elif choice3 == '3':
                    print("Instrument: ", drums['Beginner']['ELECTRIC PAD'][2][0])
                    print("Price: ", drums['Beginner']['ELECTRIC PAD'][2][1])
                else:
                    pass
            elif choice2 == '3':
                print("Select: ")
                print("1. ", drums['Beginner']['PRACTICE PAD'][0][0])
                print("2. ", drums['Beginner']['PRACTICE PAD'][1][0])
                print("3. ", drums['Beginner']['PRACTICE PAD'][2][0])
                choice3 = input()
                if choice3 == '1':
                    print("Instrument: ", drums['Beginner']['PRACTICE PAD'][0][0])
                    print("Price: ", drums['Beginner']['PRACTICE PAD'][0][1])
                elif choice3 == '2':
                    print("Instrument: ", drums['Beginner']['PRACTICE PAD'][1][0])
                    print("Price: ", drums['Beginner']['PRACTICE PAD'][1][1])
                elif choice3 == '3':
                    print("Instrument: ", drums['Beginner']['PRACTICE PAD'][2][0])
                    print("Price: ", drums['Beginner']['PRACTICE PAD'][2][1])
                else:
                    continue
            else:
                continue
            print("Do you want to see more instruments? (y/n)")
            choice4 = input()
            if choice4 == 'y':
                flow = True
            else:
                flow = False
        elif choice1 == '2':
            print("Select: ")
            print("1. ELECTRIC PAD")
            print("2. STANDARD DRUMS")
            choice2 = input()
            if choice2 == '1':
                print("Select: ")
                print("1. ", drums['Pro']['ELECTRIC PAD'][0][0])
                print("2. ", drums['Pro']['ELECTRIC PAD'][1][0])
                choice3 = input()
                if choice3 == '1':
                    print("Instrument: ", drums['Pro']['ELECTRIC PAD'][0][0])
                    print("Price: : ", drums['Pro']['ELECTRIC PAD'][0][1])
                elif choice3 == '2':
                    print("Instrument: ", drums['Pro']['ELECTRIC PAD'][1][0])
                    print("Price: ", drums['Pro']['ELECTRIC PAD'][1][1])
                elif choice3 == '3':
                    print("Instrument: ", drums['Pro']['ELECTRIC PAD'][2][0])
                    print("Price", drums['Pro']['ELECTRIC PAD'][2][1])
                else:
                    continue
            elif choice2 == '2':
                print("Select: ")
                print("1. ", drums['Pro']['STANDARD DRUMS'][0][0])
                print("2. ", drums['Pro']['STANDARD DRUMS'][1][0])
                print("3. ", drums['Pro']['STANDARD DRUMS'][2][0])
                choice3 = input()
                if choice3 == '1':
                    print("Instrument: ", drums['Pro']['STANDARD DRUMS'][0][0])
                    print("Price: ", drums['Pro']['STANDARD DRUMS'][0][1])
                elif choice3 == '2':
                    print("Instrument: ", drums['Pro']['STANDARD DRUMS'][1][0])
                    print("Price: ", drums['Pro']['STANDARD DRUMS'][1][1])
                elif choice3 == '3':
                    print("Instrument: ", drums['Pro']['STANDARD DRUMS'][2][0])
                    print("Price: ", drums['Pro']['STANDARD DRUMS'][2][1])
                else:
                    continue
            else:
                continue
            print("Do you want to see more instruments? (y/n)")
            choice4 = input()
            if choice4 == 'y':
                flow = True
            else:
                flow = False
    elif choice == '2':
        keyboard = { 'BEGINNER' : (['Casio CTX700 61-Key Touch Sensitive Portable Keyboard', 'Rs.12,739'], ['YAMAHA PSR-E373 61-Keys Portable Keyboard', 'Rs.12,739'], ['Yamaha PSR-I400 61-Key Portable Keyboard, Metallic Dark Grey', 'Rs. 16568']),
                     'PRO' : (['Yamaha Motif XF6 Music Production Synthesizer', 'Rs. 16568'], ['Yamaha PSR-S975', 'Rs.97,849'], ['Roland Fantom 6 61 Key Synthesizer Keyboard', 'Rs.267,710'])}
        print("1. Beginner")
        print("2. PRO")
        choice1 = input()
        if choice1 == '1':
            print("1. ", keyboard['BEGINNER'][0][0])
            print("2. ", keyboard['BEGINNER'][1][0])
            print("3. ", keyboard['BEGINNER'][2][0])
            choice2 = input()
            if choice2 == '1':
                print("Instrument: ", keyboard['BEGINNER'][0][0])
                print("Price: ", keyboard['BEGINNER'][0][1])
            elif choice2 == '2':
                print("Instrument: ", keyboard['BEGINNER'][1][0])
                print("Price: ", keyboard['BEGINNER'][1][1])
            elif choice2 == '3':
                print("Instrument: ", keyboard['BEGINNER'][2][0])
                print("Price: ", keyboard['BEGINNER'][2][1])
            else:
                continue
        elif choice1 == '2':
            print("1. ", keyboard['PRO'][0][0])
            print("2. ", keyboard['PRO'][1][0])
            print("3. ", keyboard['PRO'][2][0])
            choice2 = input()
            if choice2 == '1':
                print("Instrument: ", keyboard['PRO'][0][0])
                print("Price: ", keyboard['PRO'][0][1])
            elif choice2 == '2':
                print("Instrument: ", keyboard['PRO'][1][0])
                print("Price: ", keyboard['PRO'][1][1])
            elif choice2 == '3':
                print("Instrument: ", keyboard['PRO'][2][0])
                print("Price: ", keyboard['PRO'][2][1])
            else:
                continue
        else:
            continue
        print("Do you want to see more instruments? (y/n)")
        choice4 = input()
        if choice4 == 'y':
            flow = True
        else:
            flow = False
    elif choice == '3':
        guitar = {'Beginner': {'Acoustic': (['Fender CD-60S Dreadnought Acoustic Guitar', 'Rs.16,800'], ['Yamaha FG800', 'Rs.18,000'], ['Ibanez AW54CE', 'Rs.25,000']),
                               'Electric': (['Fender Squier Bullet Stratocaster HSS', 'Rs.11,999'], ['Fender Squier Classic Vibe 50s Stratocaster', 'Rs.39,000'], ['Epiphone G-400 Pro SG', 'Rs.33,443'])},
                  'Pro': {'Acoustic': (['Martin D-15M', 'Rs.1,00,000'], ['Gibson G-45 Studio', 'Rs.1,04,600'], ['Breedlove Pursuit Exotic Concert', 'Rs.70,000']),
                          'Electric': (['PRS SE Custom 24', 'Rs.80,000'], ['Ibanez Genesis Collection RG550', 'Rs.73,000'], ['Fender American Ultra Stratocaster', 'Rs.1,80,000'])}
                  }
        print("Select: ")
        print("1. Beginner")
        print("2. Pro")
        choice1 = input()
        if choice1 == '1':
            print('Select: ')
            print('1. Acoustic')
            print('2. Electric')
            choice2 = input()
            if choice2 == '1':
                print("Select: ")
                print("1. ", guitar['Beginner']['Acoustic'][0][0])
                print("2. ", guitar['Beginner']['Acoustic'][1][0])
                print("3. ", guitar['Beginner']['Acoustic'][2][0])
                choice3 = input()
                if choice3 == '1':
                    print("Instrument: ", guitar['Beginner']['Acoustic'][0][0])
                    print("Price: ", guitar['Beginner']['Acoustic'][0][1])
                elif choice3 == '2':
                    print("Instrument: ", guitar['Beginner']['Acoustic'][1][0])
                    print("Price: ", guitar['Beginner']['Acoustic'][1][1])
                elif choice3 == '3':
                    print("Instrument: ", guitar['Beginner']['Acoustic'][2][0])
                    print("Price: ", guitar['Beginner']['Acoustic'][2][1])
                else:
                    continue
            elif choice2 == '2':
                print("Select: ")
                print("1. ", guitar['Beginner']['Electric'][0][0])
                print("2. ", guitar['Beginner']['Electric'][1][0])
                print("3. ", guitar['Beginner']['Electric'][2][0])
                choice3 = input()
                if choice3 == '1':
                    print("Instrument: ", guitar['Beginner']['Electric'][0][0])
                    print("Price: ", guitar['Beginner']['Electric'][0][1])
                elif choice3 == '2':
                    print("Instrument: ", guitar['Beginner']['Electric'][1][0])
                    print("Price: ", guitar['Beginner']['Electric'][1][1])
                elif choice3 == '3':
                    print("Instrument: ", guitar['Beginner']['Electric'][2][0])
                    print("Price: ", guitar['Beginner']['Electric'][2][1])
                else:
                    continue
            else:
                pass
            print("Do you want to see more instruments? (y/n)")
            choice4 = input()
            if choice4 == 'y':
                flow = True
            else:
                flow = False
        elif choice1 == '2':
            print('Select: ')
            print('1. Acoustic')
            print('2. Electric')
            choice2 = input()
            if choice2 == '1':
                print("Select: ")
                print("1. ", guitar['Pro']['Acoustic'][0][0])
                print("2. ", guitar['Pro']['Acoustic'][1][0])
                print("3. ", guitar['Pro']['Acoustic'][2][0])
                choice3 = input()
                if choice3 == '1':
                    print("Instrument: ", guitar['Pro']['Acoustic'][0][0])
                    print("Price: ", guitar['Pro']['Acoustic'][0][1])
                elif choice3 == '2':
                    print("Instrument: ", guitar['Pro']['Acoustic'][1][0])
                    print("Price: ", guitar['Pro']['Acoustic'][1][1])
                elif choice3 == '3':
                    print("Instrument: ", guitar['Pro']['Acoustic'][2][0])
                    print("Price: ", guitar['Pro']['Acoustic'][2][1])
                else:
                    continue
            elif choice2 == '2':
                print("Select: ")
                print("1. ", guitar['Pro']['Electric'][0][0])
                print("2. ", guitar['Pro']['Electric'][1][0])
                print("3. ", guitar['Pro']['Electric'][2][0])
                choice3 = input()
                if choice3 == '1':
                    print("Instrument: ", guitar['Pro']['Electric'][0][0])
                    print("Price: ", guitar['Pro']['Electric'][0][1])
                elif choice3 == '2':
                    print("Instrument: ", guitar['Pro']['Electric'][1][0])
                    print("Price: ", guitar['Pro']['Electric'][1][1])
                elif choice3 == '3':
                    print("Instrument: ", guitar['Pro']['Electric'][2][0])
                    print("Price: ", guitar['Pro']['Electric'][2][1])
                else:
                    continue
            else:
                continue
            print("Do you want to see more instruments? (y/n)")
            choice4 = input()
            if choice4 == 'y':
                flow = True
            else:
                flow = False
    elif choice == '4':
        piano = { 'BEGINNER': (['Casio Privia PX-S3000 88-Key Digital Piano - Black', 'Rs.34,195'], ['Yamaha P45 88 Key Digital Piano', 'Rs.47,149'], ['Casio Privia PX-S3000 88-Key Digital Piano - Black', 'Rs.66,495']),
                  'PRO': (['B Steiner, Upright Piano, JS-118RID /Ebony High Polish (with Bench)', 'Rs.3,00,000'], ['B Steiner, Grand Piano, SIG-48D /Ebony High Polish (with Bench)', 'Rs.6,00,000'], ['Steinway & Sons Piano Model D', 'Rs.10,00,000'])}
        print('1. Beginner')
        print('2. Pro')
        choice1 = input()
        if choice1 == '1':
            print('1. ', piano['BEGINNER'][0][0])
            print('2. ', piano['BEGINNER'][1][0])
            print('3. ', piano['BEGINNER'][2][0])
            choice2 = input()
            if choice2 == '1':
                print('Instrument: ', piano['BEGINNER'][0][0])
                print('Price: ', piano['BEGINNER'][0][1])
            elif choice2 == '2':
                print('Instrument: ', piano['BEGINNER'][1][0])
                print('Price: ', piano['BEGINNER'][1][1])
            elif choice2 == '3':
                print('Instrument: ', piano['BEGINNER'][2][0])
                print('Price: ', piano['BEGINNER'][2][1])
            else:
                continue
        elif choice1 == '2':
            print('1. ', piano['PRO'][0][0])
            print('2. ', piano['PRO'][1][0])
            print('3. ', piano['PRO'][2][0])
            choice2 = input()
            if choice2 == '1':
                print('Instrument: ', piano['PRO'][0][0])
                print('Price: ', piano['PRO'][0][1])
            elif choice2 == '2':
                print('Instrument: ', piano['PRO'][1][0])
                print('Price: ', piano['PRO'][1][1])
            elif choice2 == '3':
                print('Instrument: ', piano['PRO'][2][0])
                print('Price: ', piano['PRO'][2][1])
            else:
                continue
        else:
            continue
        print("Do you want to see more instruments? (y/n)")
        choice4 = input()
        if choice4 == 'y':
            flow = True
        else:
            flow = False
    else:
        continue
print()
print("Thank you")
