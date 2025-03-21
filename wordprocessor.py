'''
Derrian Cooper
March 18, 2025
word processor. tested with harrison bergeson by kurt vonnegut.
'''

def main():
    anyText = input('Input text file for word processing.\n')
    try:
        inFile = open(anyText,'r')

    except Exception as error:
        print('Something went wrong:',error)
    else:
        word_dict,char_list = getText(inFile)
        mostWord, mostValue, leastWord, leastValue = processText(word_dict)
        displayProcess(mostWord, mostValue, leastWord, leastValue, char_list, word_dict, anyText)

def getText(inFile):
    word_list=[]
    char_list=[]
    oneWord = set(())
    
    word_dict = {}
    
    for line in inFile:
        #formatted line
        f_line = (line.casefold().title())
        
        #extend is necessary for sepearate lines to not create sublists
        word_list.extend(f_line.split())
        char_list.extend(f_line.strip())
        
        #update is necessary for the same reasons above but .add() does not accept the .split as it is a list
        oneWord.update(f_line.split())
        
    # A key:value for every distinct word\char in inFile and every appearence of that word\char in word_list    
    for val in oneWord:
        word_dict.update({(val):word_list.count(val)})
    


    return word_dict, char_list 

def processText(word_dict):
    mostUsedValue = 1;
    leastUsedValue= 1;
    MINIMUM_COUNT = 1

    #list because can be multiple of least\most used words
    mostUsedWord=[]
    leastUsedWord=[]
    
    for key in word_dict:
    #Most Used Word
        if int(word_dict[key]) > mostUsedValue:
            mostUsedValue = (word_dict[key])
    #Least Used Word
        if int(word_dict[key]) > MINIMUM_COUNT:
            leastUsedValue = (word_dict[key])
    '''
    mostWordValue+=int(word_dict[key]) can also find the correct value,
        but breaks mostWord list as any given val cannot be equal to the total
    '''
    
            
    #in seperate for loops to guarantee every val is checked
    for key in word_dict:
        if (word_dict[key]) < leastUsedValue:
            leastUsedValue = (word_dict[key])
            
    for key in word_dict:
        if mostUsedValue == (word_dict[key]) and key.isalpha(): #checks for symbols and numbers like '-'
            mostUsedWord.append(key)
        if leastUsedValue == (word_dict[key]) and key.isalpha():
            leastUsedWord.append(key)

    return mostUsedWord, mostUsedValue, leastUsedWord, leastUsedValue
    '''
    considered turning mostWord and mostWordValue into a dict, but having a dict just for one or two values did not seem necessary
    in the case of the least used world, although likely many words will be used 1 time, at the same time, they will all share the same value 
    '''


def displayProcess(mW,mV,lW,lV,char,word,anyFile):
    print(f'''In {anyFile}...\nThe most used word(s) are {mW} used a total of {mV} times.
The least used word(s) are {lW} used a total of {lV} times.
The total used words are {sum(word.values())}
The total used characters are {len(char)}.''')

        
    
    
    
        
#technically complete on 2:54 PM 3/19/2025
#refined on 4:37 PM 3/21/2025
if __name__=="__main__":
    main()
        
