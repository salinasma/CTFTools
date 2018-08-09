import sys;

def getInput(input: str) -> str:
    if(".txt" in input):
        return open(input, 'r');
    else:
        return input;


def cypher(input: str, shiftAmount: int) -> str:
    shiftedText: str = "";
    for letter in input:
        offset: int = 0;
        if( letter.isupper() ):
            offset = ( ord(letter) + shiftAmount )
            if (offset > ord('Z')):
                offset -= ( ord('Z') - ord('A') ) ;

        if( letter.islower() ):
            offset = ( ord(letter) + shiftAmount )
            if (offset > ord('z')):
                offset -= (ord('z') - ord('a') );

        shiftedText += chr(offset);
    return shiftedText;

input: str = getInput( sys.argv[1] );
newText: str = cypher(input, int( sys.argv[2]));

print( newText );
