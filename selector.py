import json
with open("system.json", "r") as file:
     var = json.loads(file.read())



def scan():
    iterate = var
    isNext = True
    while isNext:
        txt = input(" Enter selector StackView class, container classNames or #videoMode identifier: ")

        i = 0
        isStillSearch = True
        while isStillSearch and 'subviews' in iterate and i < len(iterate['subviews']):
            if 'contentView' in iterate['subviews'][i]: #  content view contains identifier, find the selector
                j = 0
                while j < (len(iterate['subviews'][i]['contentView']['subviews'])):
                    # print(iterate['subviews'][i]['contentView']['subviews'][j])
                    if ("identifier" in iterate['subviews'][i]['contentView']['subviews'][j]['control'] and \
                    iterate['subviews'][i]['contentView']['subviews'][j]['control']["identifier"] == txt) or \
                    (iterate['subviews'][i]['contentView']['subviews'][j]["class"] == txt): # or \
                        #iterate['subviews'][i]['contentView']['subviews'][j]['control']["identifier"] == txt :
                        print(iterate['subviews'][i]['contentView']['subviews'][j] )
                        return

                    j += 1


            if iterate['subviews'][i] and "class" in iterate['subviews'][i]  and iterate['subviews'][i]["class"] == txt:
                print(iterate['subviews'][i]) # if the selector is class
                break
            elif  iterate['subviews'][i] and "classNames" in iterate['subviews'][i]  and txt in iterate['subviews'][i]["classNames"] :
                print(iterate['subviews'][i]) # if the selector is className
                break

            else:
                if i == len(iterate['subviews']) - 1:  # if there is no  such selector and searched is finished, exit loop
                    isNext = False
                    break
            i += 1

        if ('subviews' in iterate and len(iterate['subviews']) == 0):# or  # the end is reached, exit
            print('end here')
            isNext = False
        if ('subviews' not in iterate and 'contentView' not in iterate):
            print('end here not subview in iterate')
            isNext = False
        if 'subviews' in iterate:
            iterate = iterate['subviews'][i]
        if 'contentView' in iterate:
            iterate = iterate['contentView']

        print(" ")
        print(" ************************************************************************ ")
        print(" ")

scan()
