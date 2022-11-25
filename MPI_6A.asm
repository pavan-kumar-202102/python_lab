LABEL:
     MOV AH,01H
     INT 21H
     CMP AL,'0'
     JZ LAST
     JMP LABEL
LAST:
     MOV AH,4CH
     INT 21H
     END