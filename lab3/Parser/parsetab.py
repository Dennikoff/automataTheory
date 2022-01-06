
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AND BEGIN BOOL CLBR COMMA CUCLBR CUOPBR DO ELSE END ENDSTR EQUAL FALSE FIRST FUNCTION IF INT INTTYP LARGER LEFT LMS MOVE NEWLINE NOT OPBR OR RETURN RIGHT SECOND SET SHORT SHORTTYP SIZEOF SMALLER SQCLBR SQOPBR SUB THEN TRUE UNDEFINED VARIABLE VECTOROF WHILEprogram : statement_liststatement_list : statement_list single_statement\n                          | single_statementsingle_statement : declaration ENDSTR\n                            | setting ENDSTR\n                            | if\n                            | dowhile\n                            | function\n                            | callfunc ENDSTR\n                            | cmd ENDSTR\n                            | ENDSTRdeclaration : type vartype : INT\n                | BOOL\n                | SHORT INT\n                | SHORTvar : setting\n               | var COMMA varvar : VARIABLEsetting : variable SET exprexpr : variable\n                | const\n                | math_expr\n                | callfunc\n                | cmd\n                | OPBR expr CLBRsetting : variable SET setarrtype : vectorofvectorof : VECTOROF typesetarr : CUOPBR setarr CUCLBR\n                  | setarr COMMA setarr\n                  | CUOPBR exprarr CUCLBRexprarr : exprarr COMMA exprarr\n                   | exprconst : digit\n                 | bool\n                 | sizeofvariable : VARIABLE\n                    | VARIABLE indexindex : SQOPBR expr SQCLBR\n                 | index indexsizeof : SIZEOF OPBR type CLBR\n                  | SIZEOF OPBR variable CLBRbool : TRUE\n                | FALSE\n                | UNDEFINEDdigit : INTTYP\n                 | SHORTTYPmath_expr : expr EQUAL expr\n                     | expr SUB expr\n                     | expr ADD expr\n                     | expr SECOND LARGER expr\n                     | expr SECOND SMALLER expr\n                     | expr FIRST LARGER expr\n                     | expr FIRST SMALLER expr\n                     | expr AND expr\n                     | expr OR expr\n                     | expr NOT AND expr\n                     | expr NOT OR exprcallfunc : VARIABLE OPBR varlist CLBRvarlist : variable\n                   | const\n                   | varlist COMMA varlistif : IF expr THEN statement_gr ELSE statement_grif : IF expr THEN statement_gr error\n              | IF expr errorstatement_gr : BEGIN statement_list END\n                        | single_statementdowhile : DO statement_gr WHILE expr ENDSTRdowhile : DO errorfunction : FUNCTION VARIABLE OPBR arrtype CLBR statement_gr RETURN expr ENDSTRarrtype : type VARIABLE\n                   | arrtype COMMA arrtypecmd : MOVE\n               | MOVE dir\n               | RIGHT\n               | LEFT\n               | LMSdir : RIGHT\n               | LEFT'
    
_lr_action_items = {'ENDSTR':([0,2,3,4,5,6,7,8,9,10,11,15,18,19,20,21,27,28,29,30,31,32,33,34,37,38,39,40,41,43,44,45,46,47,48,49,50,51,54,55,56,59,61,62,63,67,68,70,71,83,89,91,97,98,99,104,105,108,111,112,115,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,138,142,143,],[5,5,-3,28,-11,29,-6,-7,-8,30,31,5,-74,-76,-77,-78,-2,-4,-5,-9,-10,-12,-17,-19,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-70,5,-68,-39,-75,-79,-80,-20,-27,5,-66,5,-41,-18,-49,-50,-51,-56,-57,-26,132,-67,-60,-40,-31,-30,-32,5,-65,-52,-53,-54,-55,-58,-59,-42,-43,-69,5,-64,143,-71,]),'IF':([0,2,3,5,7,8,9,15,27,28,29,30,31,54,55,56,70,71,83,112,122,123,132,133,138,143,],[14,14,-3,-11,-6,-7,-8,14,-2,-4,-5,-9,-10,-70,14,-68,14,-66,14,-67,14,-65,-69,14,-64,-71,]),'DO':([0,2,3,5,7,8,9,15,27,28,29,30,31,54,55,56,70,71,83,112,122,123,132,133,138,143,],[15,15,-3,-11,-6,-7,-8,15,-2,-4,-5,-9,-10,-70,15,-68,15,-66,15,-67,15,-65,-69,15,-64,-71,]),'FUNCTION':([0,2,3,5,7,8,9,15,27,28,29,30,31,54,55,56,70,71,83,112,122,123,132,133,138,143,],[16,16,-3,-11,-6,-7,-8,16,-2,-4,-5,-9,-10,-70,16,-68,16,-66,16,-67,16,-65,-69,16,-64,-71,]),'VARIABLE':([0,2,3,5,7,8,9,12,14,15,16,22,23,24,25,27,28,29,30,31,35,42,54,55,56,58,60,64,65,66,69,70,71,72,73,74,77,78,81,82,83,100,101,102,103,106,107,112,114,116,121,122,123,132,133,138,141,143,],[17,17,-3,-11,-6,-7,-8,34,43,17,57,-13,-14,-16,-28,-2,-4,-5,-9,-10,43,43,-70,17,-68,85,43,-15,-29,34,43,17,-66,43,43,43,43,43,85,43,17,43,43,43,43,43,43,-67,135,85,43,17,-65,-69,17,-64,43,-71,]),'MOVE':([0,2,3,5,7,8,9,14,15,27,28,29,30,31,35,42,54,55,56,60,69,70,71,72,73,74,77,78,82,83,100,101,102,103,106,107,112,121,122,123,132,133,138,141,143,],[18,18,-3,-11,-6,-7,-8,18,18,-2,-4,-5,-9,-10,18,18,-70,18,-68,18,18,18,-66,18,18,18,18,18,18,18,18,18,18,18,18,18,-67,18,18,-65,-69,18,-64,18,-71,]),'RIGHT':([0,2,3,5,7,8,9,14,15,18,27,28,29,30,31,35,42,54,55,56,60,69,70,71,72,73,74,77,78,82,83,100,101,102,103,106,107,112,121,122,123,132,133,138,141,143,],[19,19,-3,-11,-6,-7,-8,19,19,62,-2,-4,-5,-9,-10,19,19,-70,19,-68,19,19,19,-66,19,19,19,19,19,19,19,19,19,19,19,19,19,-67,19,19,-65,-69,19,-64,19,-71,]),'LEFT':([0,2,3,5,7,8,9,14,15,18,27,28,29,30,31,35,42,54,55,56,60,69,70,71,72,73,74,77,78,82,83,100,101,102,103,106,107,112,121,122,123,132,133,138,141,143,],[20,20,-3,-11,-6,-7,-8,20,20,63,-2,-4,-5,-9,-10,20,20,-70,20,-68,20,20,20,-66,20,20,20,20,20,20,20,20,20,20,20,20,20,-67,20,20,-65,-69,20,-64,20,-71,]),'LMS':([0,2,3,5,7,8,9,14,15,27,28,29,30,31,35,42,54,55,56,60,69,70,71,72,73,74,77,78,82,83,100,101,102,103,106,107,112,121,122,123,132,133,138,141,143,],[21,21,-3,-11,-6,-7,-8,21,21,-2,-4,-5,-9,-10,21,21,-70,21,-68,21,21,21,-66,21,21,21,21,21,21,21,21,21,21,21,21,21,-67,21,21,-65,-69,21,-64,21,-71,]),'INT':([0,2,3,5,7,8,9,15,24,26,27,28,29,30,31,54,55,56,70,71,81,83,84,112,122,123,132,133,134,138,143,],[22,22,-3,-11,-6,-7,-8,22,64,22,-2,-4,-5,-9,-10,-70,22,-68,22,-66,22,22,22,-67,22,-65,-69,22,22,-64,-71,]),'BOOL':([0,2,3,5,7,8,9,15,26,27,28,29,30,31,54,55,56,70,71,81,83,84,112,122,123,132,133,134,138,143,],[23,23,-3,-11,-6,-7,-8,23,23,-2,-4,-5,-9,-10,-70,23,-68,23,-66,23,23,23,-67,23,-65,-69,23,23,-64,-71,]),'SHORT':([0,2,3,5,7,8,9,15,26,27,28,29,30,31,54,55,56,70,71,81,83,84,112,122,123,132,133,134,138,143,],[24,24,-3,-11,-6,-7,-8,24,24,-2,-4,-5,-9,-10,-70,24,-68,24,-66,24,24,24,-67,24,-65,-69,24,24,-64,-71,]),'VECTOROF':([0,2,3,5,7,8,9,15,26,27,28,29,30,31,54,55,56,70,71,81,83,84,112,122,123,132,133,134,138,143,],[26,26,-3,-11,-6,-7,-8,26,26,-2,-4,-5,-9,-10,-70,26,-68,26,-66,26,26,26,-67,26,-65,-69,26,26,-64,-71,]),'$end':([1,2,3,5,7,8,9,27,28,29,30,31,54,56,71,112,123,132,138,143,],[0,-1,-3,-11,-6,-7,-8,-2,-4,-5,-9,-10,-70,-68,-66,-67,-65,-69,-64,-71,]),'END':([3,5,7,8,9,27,28,29,30,31,54,56,71,83,112,123,132,138,143,],[-3,-11,-6,-7,-8,-2,-4,-5,-9,-10,-70,-68,-66,112,-67,-65,-69,-64,-71,]),'WHILE':([5,7,8,9,28,29,30,31,53,54,56,71,112,123,132,138,143,],[-11,-6,-7,-8,-4,-5,-9,-10,82,-70,-68,-66,-67,-65,-69,-64,-71,]),'ELSE':([5,7,8,9,28,29,30,31,54,56,71,96,112,123,132,138,143,],[-11,-6,-7,-8,-4,-5,-9,-10,-70,-68,-66,122,-67,-65,-69,-64,-71,]),'error':([5,7,8,9,15,18,19,20,21,28,29,30,31,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,54,56,59,61,62,63,71,89,96,97,98,99,104,105,108,112,115,117,123,124,125,126,127,128,129,130,131,132,138,143,],[-11,-6,-7,-8,54,-74,-76,-77,-78,-4,-5,-9,-10,71,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-70,-68,-39,-75,-79,-80,-66,-41,123,-49,-50,-51,-56,-57,-26,-67,-60,-40,-65,-52,-53,-54,-55,-58,-59,-42,-43,-69,-64,-71,]),'RETURN':([5,7,8,9,28,29,30,31,54,56,71,112,123,132,138,139,143,],[-11,-6,-7,-8,-4,-5,-9,-10,-70,-68,-66,-67,-65,-69,-64,141,-71,]),'SET':([13,17,34,59,89,117,],[35,-38,-38,-39,-41,-40,]),'OPBR':([14,17,35,42,43,52,57,60,69,72,73,74,77,78,82,100,101,102,103,106,107,121,141,],[42,58,42,42,58,81,84,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'INTTYP':([14,35,42,58,60,69,72,73,74,77,78,82,100,101,102,103,106,107,116,121,141,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'SHORTTYP':([14,35,42,58,60,69,72,73,74,77,78,82,100,101,102,103,106,107,116,121,141,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'TRUE':([14,35,42,58,60,69,72,73,74,77,78,82,100,101,102,103,106,107,116,121,141,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'FALSE':([14,35,42,58,60,69,72,73,74,77,78,82,100,101,102,103,106,107,116,121,141,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'UNDEFINED':([14,35,42,58,60,69,72,73,74,77,78,82,100,101,102,103,106,107,116,121,141,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'SIZEOF':([14,35,42,58,60,69,72,73,74,77,78,82,100,101,102,103,106,107,116,121,141,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'BEGIN':([15,70,122,133,],[55,55,55,55,]),'SQOPBR':([17,34,43,59,85,89,117,],[60,60,60,60,60,60,-40,]),'THEN':([18,19,20,21,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,59,61,62,63,89,97,98,99,104,105,108,115,117,124,125,126,127,128,129,130,131,],[-74,-76,-77,-78,70,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-39,-75,-79,-80,-41,-49,-50,-51,-56,-57,-26,-60,-40,-52,-53,-54,-55,-58,-59,-42,-43,]),'EQUAL':([18,19,20,21,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,59,61,62,63,67,80,89,90,95,97,98,99,104,105,108,111,115,117,124,125,126,127,128,129,130,131,142,],[-74,-76,-77,-78,72,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-39,-75,-79,-80,72,72,-41,72,72,72,72,72,72,72,-26,72,-60,-40,72,72,72,72,72,72,-42,-43,72,]),'SUB':([18,19,20,21,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,59,61,62,63,67,80,89,90,95,97,98,99,104,105,108,111,115,117,124,125,126,127,128,129,130,131,142,],[-74,-76,-77,-78,73,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-39,-75,-79,-80,73,73,-41,73,73,73,73,73,73,73,-26,73,-60,-40,73,73,73,73,73,73,-42,-43,73,]),'ADD':([18,19,20,21,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,59,61,62,63,67,80,89,90,95,97,98,99,104,105,108,111,115,117,124,125,126,127,128,129,130,131,142,],[-74,-76,-77,-78,74,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-39,-75,-79,-80,74,74,-41,74,74,74,74,74,74,74,-26,74,-60,-40,74,74,74,74,74,74,-42,-43,74,]),'SECOND':([18,19,20,21,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,59,61,62,63,67,80,89,90,95,97,98,99,104,105,108,111,115,117,124,125,126,127,128,129,130,131,142,],[-74,-76,-77,-78,75,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-39,-75,-79,-80,75,75,-41,75,75,75,75,75,75,75,-26,75,-60,-40,75,75,75,75,75,75,-42,-43,75,]),'FIRST':([18,19,20,21,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,59,61,62,63,67,80,89,90,95,97,98,99,104,105,108,111,115,117,124,125,126,127,128,129,130,131,142,],[-74,-76,-77,-78,76,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-39,-75,-79,-80,76,76,-41,76,76,76,76,76,76,76,-26,76,-60,-40,76,76,76,76,76,76,-42,-43,76,]),'AND':([18,19,20,21,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,59,61,62,63,67,79,80,89,90,95,97,98,99,104,105,108,111,115,117,124,125,126,127,128,129,130,131,142,],[-74,-76,-77,-78,77,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-39,-75,-79,-80,77,106,77,-41,77,77,77,77,77,77,77,-26,77,-60,-40,77,77,77,77,77,77,-42,-43,77,]),'OR':([18,19,20,21,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,59,61,62,63,67,79,80,89,90,95,97,98,99,104,105,108,111,115,117,124,125,126,127,128,129,130,131,142,],[-74,-76,-77,-78,78,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-39,-75,-79,-80,78,107,78,-41,78,78,78,78,78,78,78,-26,78,-60,-40,78,78,78,78,78,78,-42,-43,78,]),'NOT':([18,19,20,21,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,59,61,62,63,67,80,89,90,95,97,98,99,104,105,108,111,115,117,124,125,126,127,128,129,130,131,142,],[-74,-76,-77,-78,79,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-39,-75,-79,-80,79,79,-41,79,79,79,79,79,79,79,-26,79,-60,-40,79,79,79,79,79,79,-42,-43,79,]),'COMMA':([18,19,20,21,32,33,34,37,38,39,40,41,43,44,45,46,47,48,49,50,51,59,61,62,63,67,68,85,86,87,88,89,91,93,94,95,97,98,99,104,105,108,113,115,117,118,119,120,124,125,126,127,128,129,130,131,135,136,137,140,],[-74,-76,-77,-78,66,-17,-19,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-39,-75,-79,-80,-20,92,-38,116,-61,-62,-41,66,92,121,-34,-49,-50,-51,-56,-57,-26,134,-60,-40,92,-30,-32,-52,-53,-54,-55,-58,-59,-42,-43,-72,116,121,134,]),'CLBR':([18,19,20,21,22,23,24,25,37,38,39,40,41,43,44,45,46,47,48,49,50,51,59,61,62,63,64,65,80,85,86,87,88,89,97,98,99,104,105,108,109,110,113,115,117,124,125,126,127,128,129,130,131,135,136,140,],[-74,-76,-77,-78,-13,-14,-16,-28,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-39,-75,-79,-80,-15,-29,108,-38,115,-61,-62,-41,-49,-50,-51,-56,-57,-26,130,131,133,-60,-40,-52,-53,-54,-55,-58,-59,-42,-43,-72,-63,-73,]),'SQCLBR':([18,19,20,21,37,38,39,40,41,43,44,45,46,47,48,49,50,51,59,61,62,63,89,90,97,98,99,104,105,108,115,117,124,125,126,127,128,129,130,131,],[-74,-76,-77,-78,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-39,-75,-79,-80,-41,117,-49,-50,-51,-56,-57,-26,-60,-40,-52,-53,-54,-55,-58,-59,-42,-43,]),'CUCLBR':([18,19,20,21,37,38,39,40,41,43,44,45,46,47,48,49,50,51,59,61,62,63,89,93,94,95,97,98,99,104,105,108,115,117,118,119,120,124,125,126,127,128,129,130,131,137,],[-74,-76,-77,-78,-21,-22,-23,-24,-25,-38,-35,-36,-37,-47,-48,-44,-45,-46,-39,-75,-79,-80,-41,119,120,-34,-49,-50,-51,-56,-57,-26,-60,-40,-31,-30,-32,-52,-53,-54,-55,-58,-59,-42,-43,-33,]),'CUOPBR':([35,69,92,],[69,69,69,]),'LARGER':([75,76,],[100,102,]),'SMALLER':([75,76,],[101,103,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,55,],[2,83,]),'single_statement':([0,2,15,55,70,83,122,133,],[3,27,56,3,56,27,56,56,]),'declaration':([0,2,15,55,70,83,122,133,],[4,4,4,4,4,4,4,4,]),'setting':([0,2,12,15,55,66,70,83,122,133,],[6,6,33,6,6,33,6,6,6,6,]),'if':([0,2,15,55,70,83,122,133,],[7,7,7,7,7,7,7,7,]),'dowhile':([0,2,15,55,70,83,122,133,],[8,8,8,8,8,8,8,8,]),'function':([0,2,15,55,70,83,122,133,],[9,9,9,9,9,9,9,9,]),'callfunc':([0,2,14,15,35,42,55,60,69,70,72,73,74,77,78,82,83,100,101,102,103,106,107,121,122,133,141,],[10,10,40,10,40,40,10,40,40,10,40,40,40,40,40,40,10,40,40,40,40,40,40,40,10,10,40,]),'cmd':([0,2,14,15,35,42,55,60,69,70,72,73,74,77,78,82,83,100,101,102,103,106,107,121,122,133,141,],[11,11,41,11,41,41,11,41,41,11,41,41,41,41,41,41,11,41,41,41,41,41,41,41,11,11,41,]),'type':([0,2,15,26,55,70,81,83,84,122,133,134,],[12,12,12,65,12,12,109,12,114,12,12,114,]),'variable':([0,2,12,14,15,35,42,55,58,60,66,69,70,72,73,74,77,78,81,82,83,100,101,102,103,106,107,116,121,122,133,141,],[13,13,13,37,13,37,37,13,87,37,13,37,13,37,37,37,37,37,110,37,13,37,37,37,37,37,37,87,37,13,13,37,]),'vectorof':([0,2,15,26,55,70,81,83,84,122,133,134,],[25,25,25,25,25,25,25,25,25,25,25,25,]),'var':([12,66,],[32,91,]),'expr':([14,35,42,60,69,72,73,74,77,78,82,100,101,102,103,106,107,121,141,],[36,67,80,90,95,97,98,99,104,105,111,124,125,126,127,128,129,95,142,]),'const':([14,35,42,58,60,69,72,73,74,77,78,82,100,101,102,103,106,107,116,121,141,],[38,38,38,88,38,38,38,38,38,38,38,38,38,38,38,38,38,38,88,38,38,]),'math_expr':([14,35,42,60,69,72,73,74,77,78,82,100,101,102,103,106,107,121,141,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'digit':([14,35,42,58,60,69,72,73,74,77,78,82,100,101,102,103,106,107,116,121,141,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'bool':([14,35,42,58,60,69,72,73,74,77,78,82,100,101,102,103,106,107,116,121,141,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'sizeof':([14,35,42,58,60,69,72,73,74,77,78,82,100,101,102,103,106,107,116,121,141,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'statement_gr':([15,70,122,133,],[53,96,138,139,]),'index':([17,34,43,59,85,89,],[59,59,59,89,59,89,]),'dir':([18,],[61,]),'setarr':([35,69,92,],[68,93,118,]),'varlist':([58,116,],[86,136,]),'exprarr':([69,121,],[94,137,]),'arrtype':([84,134,],[113,140,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','ParserFile.py',23),
  ('statement_list -> statement_list single_statement','statement_list',2,'p_statement_list','ParserFile.py',27),
  ('statement_list -> single_statement','statement_list',1,'p_statement_list','ParserFile.py',28),
  ('single_statement -> declaration ENDSTR','single_statement',2,'p_single_statement','ParserFile.py',33),
  ('single_statement -> setting ENDSTR','single_statement',2,'p_single_statement','ParserFile.py',34),
  ('single_statement -> if','single_statement',1,'p_single_statement','ParserFile.py',35),
  ('single_statement -> dowhile','single_statement',1,'p_single_statement','ParserFile.py',36),
  ('single_statement -> function','single_statement',1,'p_single_statement','ParserFile.py',37),
  ('single_statement -> callfunc ENDSTR','single_statement',2,'p_single_statement','ParserFile.py',38),
  ('single_statement -> cmd ENDSTR','single_statement',2,'p_single_statement','ParserFile.py',39),
  ('single_statement -> ENDSTR','single_statement',1,'p_single_statement','ParserFile.py',40),
  ('declaration -> type var','declaration',2,'p_declaration','ParserFile.py',44),
  ('type -> INT','type',1,'p_type','ParserFile.py',48),
  ('type -> BOOL','type',1,'p_type','ParserFile.py',49),
  ('type -> SHORT INT','type',2,'p_type','ParserFile.py',50),
  ('type -> SHORT','type',1,'p_type','ParserFile.py',51),
  ('var -> setting','var',1,'p_var','ParserFile.py',55),
  ('var -> var COMMA var','var',3,'p_var','ParserFile.py',56),
  ('var -> VARIABLE','var',1,'p_var_v','ParserFile.py',60),
  ('setting -> variable SET expr','setting',3,'p_setting','ParserFile.py',64),
  ('expr -> variable','expr',1,'p_expr','ParserFile.py',68),
  ('expr -> const','expr',1,'p_expr','ParserFile.py',69),
  ('expr -> math_expr','expr',1,'p_expr','ParserFile.py',70),
  ('expr -> callfunc','expr',1,'p_expr','ParserFile.py',71),
  ('expr -> cmd','expr',1,'p_expr','ParserFile.py',72),
  ('expr -> OPBR expr CLBR','expr',3,'p_expr','ParserFile.py',73),
  ('setting -> variable SET setarr','setting',3,'p_setting_arr','ParserFile.py',77),
  ('type -> vectorof','type',1,'p_type_arr','ParserFile.py',81),
  ('vectorof -> VECTOROF type','vectorof',2,'p_vectorof','ParserFile.py',85),
  ('setarr -> CUOPBR setarr CUCLBR','setarr',3,'p_setarr','ParserFile.py',89),
  ('setarr -> setarr COMMA setarr','setarr',3,'p_setarr','ParserFile.py',90),
  ('setarr -> CUOPBR exprarr CUCLBR','setarr',3,'p_setarr','ParserFile.py',91),
  ('exprarr -> exprarr COMMA exprarr','exprarr',3,'p_exprarr','ParserFile.py',95),
  ('exprarr -> expr','exprarr',1,'p_exprarr','ParserFile.py',96),
  ('const -> digit','const',1,'p_const','ParserFile.py',100),
  ('const -> bool','const',1,'p_const','ParserFile.py',101),
  ('const -> sizeof','const',1,'p_const','ParserFile.py',102),
  ('variable -> VARIABLE','variable',1,'p_variable','ParserFile.py',106),
  ('variable -> VARIABLE index','variable',2,'p_variable','ParserFile.py',107),
  ('index -> SQOPBR expr SQCLBR','index',3,'p_index','ParserFile.py',111),
  ('index -> index index','index',2,'p_index','ParserFile.py',112),
  ('sizeof -> SIZEOF OPBR type CLBR','sizeof',4,'p_sizeof','ParserFile.py',116),
  ('sizeof -> SIZEOF OPBR variable CLBR','sizeof',4,'p_sizeof','ParserFile.py',117),
  ('bool -> TRUE','bool',1,'p_bool','ParserFile.py',121),
  ('bool -> FALSE','bool',1,'p_bool','ParserFile.py',122),
  ('bool -> UNDEFINED','bool',1,'p_bool','ParserFile.py',123),
  ('digit -> INTTYP','digit',1,'p_digit','ParserFile.py',127),
  ('digit -> SHORTTYP','digit',1,'p_digit','ParserFile.py',128),
  ('math_expr -> expr EQUAL expr','math_expr',3,'p_math_expr','ParserFile.py',132),
  ('math_expr -> expr SUB expr','math_expr',3,'p_math_expr','ParserFile.py',133),
  ('math_expr -> expr ADD expr','math_expr',3,'p_math_expr','ParserFile.py',134),
  ('math_expr -> expr SECOND LARGER expr','math_expr',4,'p_math_expr','ParserFile.py',135),
  ('math_expr -> expr SECOND SMALLER expr','math_expr',4,'p_math_expr','ParserFile.py',136),
  ('math_expr -> expr FIRST LARGER expr','math_expr',4,'p_math_expr','ParserFile.py',137),
  ('math_expr -> expr FIRST SMALLER expr','math_expr',4,'p_math_expr','ParserFile.py',138),
  ('math_expr -> expr AND expr','math_expr',3,'p_math_expr','ParserFile.py',139),
  ('math_expr -> expr OR expr','math_expr',3,'p_math_expr','ParserFile.py',140),
  ('math_expr -> expr NOT AND expr','math_expr',4,'p_math_expr','ParserFile.py',141),
  ('math_expr -> expr NOT OR expr','math_expr',4,'p_math_expr','ParserFile.py',142),
  ('callfunc -> VARIABLE OPBR varlist CLBR','callfunc',4,'p_callfunc','ParserFile.py',146),
  ('varlist -> variable','varlist',1,'p_varlist','ParserFile.py',150),
  ('varlist -> const','varlist',1,'p_varlist','ParserFile.py',151),
  ('varlist -> varlist COMMA varlist','varlist',3,'p_varlist','ParserFile.py',152),
  ('if -> IF expr THEN statement_gr ELSE statement_gr','if',6,'p_if','ParserFile.py',156),
  ('if -> IF expr THEN statement_gr error','if',5,'p_iferr','ParserFile.py',160),
  ('if -> IF expr error','if',3,'p_iferr','ParserFile.py',161),
  ('statement_gr -> BEGIN statement_list END','statement_gr',3,'p_statement_gr','ParserFile.py',165),
  ('statement_gr -> single_statement','statement_gr',1,'p_statement_gr','ParserFile.py',166),
  ('dowhile -> DO statement_gr WHILE expr ENDSTR','dowhile',5,'p_dowhile','ParserFile.py',170),
  ('dowhile -> DO error','dowhile',2,'p_dowhileerr','ParserFile.py',174),
  ('function -> FUNCTION VARIABLE OPBR arrtype CLBR statement_gr RETURN expr ENDSTR','function',9,'p_function','ParserFile.py',179),
  ('arrtype -> type VARIABLE','arrtype',2,'p_arrtype','ParserFile.py',185),
  ('arrtype -> arrtype COMMA arrtype','arrtype',3,'p_arrtype','ParserFile.py',186),
  ('cmd -> MOVE','cmd',1,'p_cmd','ParserFile.py',190),
  ('cmd -> MOVE dir','cmd',2,'p_cmd','ParserFile.py',191),
  ('cmd -> RIGHT','cmd',1,'p_cmd','ParserFile.py',192),
  ('cmd -> LEFT','cmd',1,'p_cmd','ParserFile.py',193),
  ('cmd -> LMS','cmd',1,'p_cmd','ParserFile.py',194),
  ('dir -> RIGHT','dir',1,'p_dir','ParserFile.py',198),
  ('dir -> LEFT','dir',1,'p_dir','ParserFile.py',199),
]
