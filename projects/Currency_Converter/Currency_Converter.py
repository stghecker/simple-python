print("===============")
print("CURRENCY CONVERTER")
print("===============")
print("  ")
print('To convert from EUR, type "EUR"')
print('To convert from USD, type "USD"')
print('To convert from GBP, type "GBP"')
print('To convert from CNY, type "CNY"')
print('To convert from JPY, type "JPY"')
print("  ")
vinput = ["eur","usd","gbp","cny","jpy"]
vconvert = input("").lower()
while vconvert not in vinput:
    print("Please type EUR, USD, GBP, CNY or JPY")
    vconvert = input("").lower()
if vconvert == "eur":
    while True:
        print("Write the amount of Euros here:")
        veur = (input("").replace(",", "."))
        try:
            veur = float(veur)
            break
        except ValueError:
            print("Please input a number.")
    print("Convert" , veur , "euros to:")
    print('To convert to USD, type "USD"')
    print('To convert to GBP, type "GBP"')
    print('To convert to CNY, type "CNY"')
    print('To convert to JPY, type "JPY"')
    vincoin = ["usd","gbp","cny","jpy"]
    vmainconvert = input("Convert to:").lower()
    while vmainconvert not in vincoin:
        print("Please input USD, GBP, CNY or JPY")
        vmainconvert = input("")
        try:
            vmainconvert = str(vmainconvert)
        except ValueError:
            print("Please input USD, GBP, CNY or JPY")
    if vmainconvert == "usd":
        result = veur * 1.544
        print("=====================")
        print("Conversion completed! 🎉")
        print(veur ,"Euros to USD:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "gbp":
        result = veur * 0.8723
        print("=====================")
        print("Conversion completed! 🎉")
        print(veur ,"Euros to GBP:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "cny":
        result = veur * 7.9494
        print("=====================")
        print("Conversion completed! 🎉")
        print(veur ,"Euros to CNY:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "jpy":
        result = veur * 183.93
        print("=====================")
        print("Conversion completed! 🎉")
        print(veur ,"Euros to JPY:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")

elif vconvert == "usd":
    while True:
        print("Write the amount of Dollars here:")
        vusd = (input("").replace(",", "."))
        try:
            vusd = float(vusd)
            break
        except ValueError:
            print("Please input a number.")
    print("Write the amount of Dollars here:")
    vusd = input("")
    print("Convert" , vusd , "dollars to:")
    print('To convert to EUR, type "EUR"')
    print('To convert to GBP, type "GBP"')
    print('To convert to CNY, type "CNY"')
    print('To convert to JPY, type "JPY"')
    vincoin = ["eur","gbp","cny","jpy"]
    vmainconvert = input("Convert to:").lower()
    while vmainconvert not in vincoin:
        print("Please input EUR, GBP, CNY or JPY")
        vmainconvert = input("")
        try:
            vmainconvert = str(vmainconvert)
        except ValueError:
            print("Please input EUR, GBP, CNY or JPY")
    if vmainconvert == "eur":
        result = vusd * 0.8664
        print("=====================")
        print("Conversion completed! 🎉")
        print(vusd , "Dollars to EUR:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "gbp":
        result = vusd * 0.7553
        print("=====================")
        print("Conversion completed! 🎉")
        print(vusd , "Dollars to GBP:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "cny":
        result = vusd * 6.9223
        print("=====================")
        print("Conversion completed! 🎉")
        print(vusd , "Dollars to CNY:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "jpy":
        result = vusd * 159.37
        print("=====================")
        print("Conversion completed! 🎉")
        print(vusd , "Dollars to JPY:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")

elif vconvert == "gbp":
    while True:
        print("Write the amount of GBP here:")
        vgbp = (input("").replace(",", "."))
        try:
            vgbp = float(vgbp)
            break
        except ValueError:
            print("Please input a number.")
    print("Write the amount of GBP here:")
    print("Convert" , vgbp , "GBP to:")
    print('To convert to USD, type "USD"')
    print('To convert to EUR, type "EUR"')
    print('To convert to CNY, type "CNY"')
    print('To convert to JPY, type "JPY"')
    vincoin = ["usd","eur","cny","jpy"]
    vmainconvert = input("Convert to:").lower()
    while vmainconvert not in vincoin:
        print("Please input USD, EUR, CNY or JPY")
        vmainconvert = input("")
        try:
            vmainconvert = str(vmainconvert)
        except ValueError:
            print("Please input USD, EUR, CNY or JPY")
    if vmainconvert == "usd":
        result = vgbp * 1.3240
        print("=====================")
        print("Conversion completed! 🎉")
        print(vgbp , "GBP to USD:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "eur":
        result = vgbp * 1.1465
        print("=====================")
        print("Conversion completed! 🎉")
        print(vgbp , "GBP to EUR:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "cny":
        result = vgbp * 9.1650
        print("=====================")
        print("Conversion completed! 🎉")
        print(vgbp , "GBP to CNY:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "jpy":
        result = vgbp * 211.02
        print("=====================")
        print("Conversion completed! 🎉")
        print(vgbp , "GBP to JPY:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")

elif vconvert == "cny":
    while True:
        print("Write the amount of CNY here:")
        vcny = (input("").replace(",", "."))
        try:
            vcny = float(vcny)
            break
        except ValueError:
            print("Please input a number.")
    print("Write the amount of CNY here:")
    print("Convert" , vcny , "CNY to:")
    print('To convert to USD, type "USD"')
    print('To convert to EUR, type "EUR"')
    print('To convert to GBP, type "GBP"')
    print('To convert to JPY, type "JPY"')
    vincoin = ["usd","eur","gbp","jpy"]
    vmainconvert = input("Convert to:").lower()
    while vmainconvert not in vincoin:
        print("Please input USD, GBP, CNY or JPY")
        vmainconvert = input("")
        try:
            vmainconvert = str(vmainconvert)
        except ValueError:
            print("Please input USD, EUR, GBP or JPY")
    if vmainconvert == "usd":
        result = vcny * 0.145
        print("=====================")
        print("Conversion completed! 🎉")
        print(vcny , "CNY to USD:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "eur":
        result = vcny * 0.1258
        print("=====================")
        print("Conversion completed! 🎉")
        print(vcny, "CNY to EUR:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "gbp":
        result = vcny * 0.1091
        print("=====================")
        print("Conversion completed! 🎉")
        print(vcny, "CNY to GBP:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "jpy":
        result = vcny * 23.16
        print("Conversion completed!")
        print(vcny, "CNY to JPY:" , result)

elif vconvert == "jpy":
    while True:
        print("Write the amount of JPY here:")
        vjpy = (input("").replace(",", "."))
        try:
            vjpy = float(vjpy)
            break
        except ValueError:
            print("Please input a number.")
    print("Write the amount of JPY here:")
    print("Convert" , vjpy , "JPY to:")
    print('To convert to USD, type "USD"')
    print('To convert to EUR, type "EUR"')
    print('To convert to GBP, type "GBP"')
    print('To convert to CNY, type "CNY"')
    vincoin = ["usd","eur","gbp","cny"]
    vmainconvert = input("Convert to:").lower()
    while vmainconvert not in vincoin:
        print("Please input USD, EUR, GBP or CNY")
        vmainconvert = input("")
        try:
            vmainconvert = str(vmainconvert)
        except ValueError:
            print("Please input USD, EUR, GBP or CNY")
    if vmainconvert == "usd":
        result = vjpy * 0.0063
        print("=====================")
        print("Conversion completed! 🎉")
        print(vjpy, "JPY to USD:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "eur":
        result = vjpy * 0.0054
        print("=====================")
        print("Conversion completed! 🎉")
        print(vjpy, "JPY to EUR:" , result)
        print("======================")
        print("Conversions are based on 2=nd of April, 2026.")
    elif vmainconvert == "gbp":
        result = vjpy * 0.47
        print("=====================")
        print("Conversion completed! 🎉")
        print(vjpy, "JPY to GBP:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")
    elif vmainconvert == "cny":
        result = vjpy * 4.32
        print("=====================")
        print("Conversion completed! 🎉")
        print(vjpy, "JPY to CNY:" , result)
        print("======================")
        print("Conversions are based on 2nd of April, 2026.")

elif vconvert not in ["eur","usd","gbp","cny","jpy"]:
    print("ERROR. Reload and try again.")

#STGHECKER#
