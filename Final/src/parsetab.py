
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "goal_symbolACCESS AND ARRAY ARROW ASSIGN BEGIN BODY BOX CHAR DOTDOT ELSE END FLOAT FOR FUNCTION GEQ IDENTIFIER IF IN INT IS LAMBDA LEQ LL LOOP MOD NEQ NEW NuLL OF OR PRAGMA PROCEDURE RECORD RETURN RR STARSTAR STRING THEN TICK TYPE USE WHILE WITHgoal_symbol : compilation\n\tpragma : PRAGMA IDENTIFIER ';'\n\t   | PRAGMA simple_name '(' pragma_arg_s ')' ';'\n\tpragma_arg_s : pragma_arg\n\t   | pragma_arg_s ',' pragma_arg\n\tpragma_arg : simple_expression\n\t   | simple_name ARROW simple_expression\n\tpragma_s :\n\t   | pragma_s pragma\n\tdecl : object_decl\n\t   | type_decl\n\t   | record_decl\n\t   | subprog_decl\n\t   | lambda_decl\n\t   | access_decl\n\ttype_decl : TYPE IDENTIFIER ';'\n\taccess_decl : TYPE IDENTIFIER IS ACCESS name ';'\n\tobject_decl : def_id_s ':' object_type_def ';'   \n\tdef_id_s : def_id\n\t   | def_id_s ',' def_id\n\tdef_id  : IDENTIFIER\n\tobject_type_def : type_ind\n\t   | array_type\n\trecord_decl : TYPE IDENTIFIER IS record_def ';'\n\ttype_ind : name\n\tderived_type : NEW type_ind\n\trange : simple_expression DOTDOT simple_expression\n\tarray_type : ARRAY iter_index_constraint OF type_ind\n\titer_index_constraint : '(' range_s ')'\n\trange_s : range\n\t   | range_s ',' range\n\trecord_def : RECORD param_s ';' END RECORD\n\tdecl_part :\n\t   | decl_item_or_body_s\n\tdecl_item : decl\n\t   | use_clause\n\t   | pragma\n\tdecl_item_or_body_s : decl_item_or_body\n\t   | decl_item_or_body_s decl_item_or_body\n\tdecl_item_or_body : body\n\t   | decl_item\n\tbody : subprog_body\n\tname : compound_name\n\t   | indexed_comp\n\tmark : name\n\tsimple_name : IDENTIFIER\n\tcompound_name : simple_name\n\t   | compound_name '.' simple_name\n\tc_name_list : compound_name\n\t    | c_name_list ',' compound_name\n\tindexed_comp : name '(' value_s ')'\n\t\t| name '(' STRING ')'\n\tvalue_s : value\n\t   | value_s ',' value\n\tvalue : simple_expression\n\tliteral : numeric_lit\n\t\t\t\t| char_lit\n\t\t\t\t| NuLL\n\tchar_lit : CHAR\n\tnumeric_lit : INT\n\tnumeric_lit : FLOAT\n\t M : \n\texpression : relation\n\t   | expression logical M relation\n\tlogical : AND\n\t   | OR\n\trelation : simple_expression relational simple_expression\n\trelational : '='\n\t   | NEQ\n\t   | '<'\n\t   | LEQ\n\t   | '>'\n\t   | GEQ\n\tsimple_expression : term\n\t   | unary term\n\t   | simple_expression adding term\n\tunary : '+'\n\t\t\t| '-'\n\tadding  : '+'\n\t   | '-'\n\tterm : factor\n\t   | term multiplying factor\n\tmultiplying : '*'\n\t   | '/'\n\t   | MOD\n\t   | STARSTAR\n\tfactor : primary\n\tprimary : literal\n\t   | name\n\t   | parenthesized_primary\n\tparenthesized_primary : '(' simple_expression ')'\n\tstatement_s : statement\n\t   | statement_s M statement\n\tstatement : simple_stmt\n\t\t| compound_stmt\n\tsimple_stmt : assign_stmt\n\t   | return_stmt\n\t   | procedure_call\n\tcompound_stmt : if_stmt\n\t   | loop_stmt\n\tlambda_decl : lambda_begin simple_expression ';'\n\tlambda_begin : def_id ASSIGN LAMBDA param ':'\n\tassign_stmt : name ASSIGN simple_expression ';'\n\t\t\t\t\t| name ASSIGN derived_type ';'\n\tif_stmt : IF cond_clause else_opt END IF ';'\n\tN :\n\tcond_clause : condition THEN M statement_s N\n\tcondition : expression\n\telse_opt :\n\t   | ELSE M statement_s\n\tloop_stmt : iteration M basic_loop ';'\n\titeration : WHILE M condition\n\t\t| FOR IDENTIFIER IN range\n\tbasic_loop : LOOP statement_s END LOOP\n\tblock_body : BEGIN statement_s\n\treturn_stmt : RETURN ';'\n\t   | RETURN simple_expression ';'\n\tsubprog_decl : subprog_spec ';'\n\tsubprog_spec : PROCEDURE def_id formal_part_opt\n\t   | FUNCTION def_id formal_part_opt RETURN name\n\tformal_part_opt : \n\t   | formal_part\n\tformal_part : '(' param_s ')'\n\tparam_s : param\n\t   | param_s ';' param\n\tparam : def_id_s ':' mark\n\tsubprog_spec_is_push : subprog_spec IS\n\tsubprog_body : subprog_spec_is_push decl_part block_body END ';'\n\tprocedure_call : name ';'\n\tuse_clause : USE name_s ';'\n\tname_s : name\n\t   | name_s ',' name\n\tcompilation :\n\t   | compilation comp_unit\n\t   | pragma pragma_s\n\tcomp_unit : context_spec unit pragma_s\n\t   | unit pragma_s\n\tcontext_spec : with_clause use_clause_opt\n\t   | context_spec with_clause use_clause_opt\n\t   | context_spec pragma\n\twith_clause : WITH c_name_list ';'\n\tuse_clause_opt :\n\t   | use_clause_opt use_clause\n\tunit : subprog_decl\n\t   | subprog_body\n\t"
    
_lr_action_items = {'OF':([168,225,],[197,-29,]),'LEQ':([50,52,57,58,59,60,61,62,63,64,65,68,72,73,74,78,111,147,148,151,157,179,184,186,],[-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,-89,-61,-58,-43,-75,-48,-82,-76,-91,210,-52,-51,]),'NEQ':([50,52,57,58,59,60,61,62,63,64,65,68,72,73,74,78,111,147,148,151,157,179,184,186,],[-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,-89,-61,-58,-43,-75,-48,-82,-76,-91,211,-52,-51,]),'END':([93,130,131,135,136,137,138,139,141,142,170,174,177,202,205,206,222,227,228,230,231,243,244,248,249,],[145,-98,-92,-97,-95,-96,-100,-99,-94,-115,-129,-116,-109,-117,-93,232,238,-104,-103,241,-111,-110,-106,-105,-107,]),'<':([50,52,57,58,59,60,61,62,63,64,65,68,72,73,74,78,111,147,148,151,157,179,184,186,],[-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,-89,-61,-58,-43,-75,-48,-82,-76,-91,212,-52,-51,]),'GEQ':([50,52,57,58,59,60,61,62,63,64,65,68,72,73,74,78,111,147,148,151,157,179,184,186,],[-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,-89,-61,-58,-43,-75,-48,-82,-76,-91,213,-52,-51,]),'>':([50,52,57,58,59,60,61,62,63,64,65,68,72,73,74,78,111,147,148,151,157,179,184,186,],[-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,-89,-61,-58,-43,-75,-48,-82,-76,-91,209,-52,-51,]),'BEGIN':([13,21,26,27,28,29,31,32,33,34,35,37,39,43,44,45,46,47,48,85,119,120,123,150,169,183,192,221,],[-33,-2,-118,-127,-11,-12,-15,-35,-37,-41,-34,-13,-10,-38,-40,-14,-36,-42,92,-39,-101,-16,-130,-3,-18,-128,-24,-17,]),'FOR':([92,130,131,135,136,137,138,139,141,142,170,174,176,202,203,205,207,215,227,228,230,231,233,235,243,244,248,],[144,-98,-92,-97,-95,-96,-100,-99,-94,-62,-129,-116,144,-117,144,-93,-62,-62,-104,-103,-62,-111,144,144,-62,-62,-105,]),'STRING':([110,],[153,]),'/':([50,52,57,58,59,60,61,62,63,64,65,68,70,72,73,74,78,111,147,148,151,157,184,186,],[-46,-47,-44,-88,-87,-81,-59,103,-57,-56,-90,-60,-47,-89,-61,-58,-43,103,-48,-82,103,-91,-52,-51,]),'ARRAY':([91,],[128,]),'RECORD':([121,238,],[165,246,]),',':([23,30,42,49,50,51,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,78,88,89,111,113,114,124,146,147,148,149,151,152,154,155,156,157,166,184,186,194,196,220,239,240,],[-21,-19,90,94,-46,-49,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,104,-4,-60,-6,-47,-89,-61,-58,-43,122,-131,-75,90,-19,-20,-50,-48,-82,-5,-76,-7,-55,-53,185,-91,-132,-52,-51,-30,224,-54,-27,-31,]),'CHAR':([20,36,71,75,76,77,99,100,101,102,103,104,106,107,108,109,110,133,134,143,167,171,172,185,190,208,209,210,211,212,213,214,216,217,218,219,223,224,236,],[61,61,-78,61,-77,61,-86,-85,61,-83,-84,61,61,-79,-80,61,61,-62,61,61,61,61,61,61,-102,61,-72,-71,-69,-70,-73,-68,-66,-65,-62,61,61,61,61,]),'*':([50,52,57,58,59,60,61,62,63,64,65,68,70,72,73,74,78,111,147,148,151,157,184,186,],[-46,-47,-44,-88,-87,-81,-59,102,-57,-56,-90,-60,-47,-89,-61,-58,-43,102,-48,-82,102,-91,-52,-51,]),'IS':([12,22,23,41,50,52,57,78,79,80,87,147,160,161,184,186,],[27,-121,-21,27,-46,-47,-44,-43,-119,-122,121,-48,-123,-120,-52,-51,]),'ARROW':([50,70,],[-46,109,]),'STARSTAR':([50,52,57,58,59,60,61,62,63,64,65,68,70,72,73,74,78,111,147,148,151,157,184,186,],[-46,-47,-44,-88,-87,-81,-59,99,-57,-56,-90,-60,-47,-89,-61,-58,-43,99,-48,-82,99,-91,-52,-51,]),'NuLL':([20,36,71,75,76,77,99,100,101,102,103,104,106,107,108,109,110,133,134,143,167,171,172,185,190,208,209,210,211,212,213,214,216,217,218,219,223,224,236,],[74,74,-78,74,-77,74,-86,-85,74,-83,-84,74,74,-79,-80,74,74,-62,74,74,74,74,74,74,-102,74,-72,-71,-69,-70,-73,-68,-66,-65,-62,74,74,74,74,]),'AND':([50,52,57,58,59,60,61,62,63,64,65,68,72,73,74,78,111,147,148,151,157,178,181,184,186,234,245,],[-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,-89,-61,-58,-43,-75,-48,-82,-76,-91,-63,217,-52,-51,-67,-64,]),'LAMBDA':([84,],[118,]),'+':([20,36,50,52,57,58,59,60,61,62,63,64,65,68,69,70,72,73,74,77,78,86,104,109,110,111,112,133,134,143,147,148,151,152,154,157,167,171,172,173,179,184,185,186,190,195,199,208,209,210,211,212,213,214,216,217,218,219,223,224,234,236,239,],[76,76,-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,107,-47,-89,-61,-58,76,-43,107,76,76,76,-75,107,-62,76,76,-48,-82,-76,107,107,-91,76,76,76,107,107,-52,76,-51,-102,107,107,76,-72,-71,-69,-70,-73,-68,-66,-65,-62,76,76,76,107,76,107,]),'FLOAT':([20,36,71,75,76,77,99,100,101,102,103,104,106,107,108,109,110,133,134,143,167,171,172,185,190,208,209,210,211,212,213,214,216,217,218,219,223,224,236,],[73,73,-78,73,-77,73,-86,-85,73,-83,-84,73,73,-79,-80,73,73,-62,73,73,73,73,73,73,-102,73,-72,-71,-69,-70,-73,-68,-66,-65,-62,73,73,73,73,]),'IF':([92,130,131,135,136,137,138,139,141,142,170,174,176,202,203,205,207,215,227,228,230,231,232,233,235,243,244,248,],[143,-98,-92,-97,-95,-96,-100,-99,-94,-62,-129,-116,143,-117,143,-93,-62,-62,-104,-103,-62,-111,242,143,143,-62,-62,-105,]),'PROCEDURE':([0,1,4,5,10,11,13,14,16,17,18,19,21,25,26,27,28,29,31,32,33,34,35,37,39,43,44,45,46,47,53,54,55,56,83,85,95,97,98,119,120,123,150,169,183,192,221,],[-133,-8,8,-135,-144,-142,8,-134,-8,8,-145,-9,-2,-138,-118,-127,-11,-12,-15,-35,-37,-41,8,-13,-10,-38,-40,-14,-36,-42,-137,-140,-142,-8,-143,-39,-141,-139,-136,-101,-16,-130,-3,-18,-128,-24,-17,]),'MOD':([50,52,57,58,59,60,61,62,63,64,65,68,70,72,73,74,78,111,147,148,151,157,184,186,],[-46,-47,-44,-88,-87,-81,-59,100,-57,-56,-90,-60,-47,-89,-61,-58,-43,100,-48,-82,100,-91,-52,-51,]),'ASSIGN':([23,30,50,52,57,78,132,147,184,186,],[-21,84,-46,-47,-44,-43,171,-48,-52,-51,]),'THEN':([50,52,57,58,59,60,61,62,63,64,65,68,72,73,74,78,111,147,148,151,157,178,180,181,184,186,234,245,],[-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,-89,-61,-58,-43,-75,-48,-82,-76,-91,-63,215,-108,-52,-51,-67,-64,]),'-':([20,36,50,52,57,58,59,60,61,62,63,64,65,68,69,70,72,73,74,77,78,86,104,109,110,111,112,133,134,143,147,148,151,152,154,157,167,171,172,173,179,184,185,186,190,195,199,208,209,210,211,212,213,214,216,217,218,219,223,224,234,236,239,],[71,71,-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,108,-47,-89,-61,-58,71,-43,108,71,71,71,-75,108,-62,71,71,-48,-82,-76,108,108,-91,71,71,71,108,108,-52,71,-51,-102,108,108,71,-72,-71,-69,-70,-73,-68,-66,-65,-62,71,71,71,108,71,108,]),')':([50,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,78,111,112,115,116,147,148,149,151,152,153,154,155,156,157,184,186,187,188,189,194,196,220,239,240,],[-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,105,-4,-60,-6,-47,-89,-61,-58,-43,-75,157,160,-124,-48,-82,-5,-76,-7,184,-55,-53,186,-91,-52,-51,-45,-126,-125,-30,225,-54,-27,-31,]),';':([7,12,22,23,41,49,50,51,52,57,58,59,60,61,62,63,64,65,68,72,73,74,78,79,80,86,87,88,89,105,111,115,116,125,126,127,129,132,134,145,146,147,148,151,157,160,161,164,166,173,184,186,187,188,189,191,193,198,199,204,226,229,242,246,247,],[21,26,-121,-21,26,95,-46,-49,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,-89,-61,-58,-43,-119,-122,119,120,123,-131,150,-75,159,-124,-25,-23,-22,169,170,174,183,-50,-48,-82,-76,-91,-123,-120,192,-132,202,-52,-51,-45,-126,-125,221,222,227,228,231,-28,-26,248,-32,-114,]),'PRAGMA':([0,1,5,10,11,13,16,17,18,19,21,25,26,27,28,29,31,32,33,34,35,37,39,43,44,45,46,47,53,54,55,56,83,85,95,97,98,119,120,123,150,169,183,192,221,],[3,-8,3,-144,-142,3,-8,3,-145,-9,-2,-138,-118,-127,-11,-12,-15,-35,-37,-41,3,-13,-10,-38,-40,-14,-36,-42,3,-140,-142,-8,-143,-39,-141,-139,3,-101,-16,-130,-3,-18,-128,-24,-17,]),'ELSE':([130,131,135,136,137,138,139,141,170,174,177,202,205,227,228,231,244,248,249,],[-98,-92,-97,-95,-96,-100,-99,-94,-129,-116,207,-117,-93,-104,-103,-111,-106,-105,-107,]),'WHILE':([92,130,131,135,136,137,138,139,141,142,170,174,176,202,203,205,207,215,227,228,230,231,233,235,243,244,248,],[133,-98,-92,-97,-95,-96,-100,-99,-94,-62,-129,-116,133,-117,133,-93,-62,-62,-104,-103,-62,-111,133,133,-62,-62,-105,]),'TYPE':([13,21,26,27,28,29,31,32,33,34,35,37,39,43,44,45,46,47,85,119,120,123,150,169,183,192,221,],[38,-2,-118,-127,-11,-12,-15,-35,-37,-41,38,-13,-10,-38,-40,-14,-36,-42,-39,-101,-16,-130,-3,-18,-128,-24,-17,]),'OR':([50,52,57,58,59,60,61,62,63,64,65,68,72,73,74,78,111,147,148,151,157,178,181,184,186,234,245,],[-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,-89,-61,-58,-43,-75,-48,-82,-76,-91,-63,216,-52,-51,-67,-64,]),'RETURN':([23,24,80,82,92,130,131,135,136,137,138,139,141,142,160,170,174,176,202,203,205,207,215,227,228,230,231,233,235,243,244,248,],[-21,-121,-122,117,134,-98,-92,-97,-95,-96,-100,-99,-94,-62,-123,-129,-116,134,-117,134,-93,-62,-62,-104,-103,-62,-111,134,134,-62,-62,-105,]),'USE':([11,13,21,25,26,27,28,29,31,32,33,34,35,37,39,43,44,45,46,47,55,83,85,95,97,119,120,123,150,169,183,192,221,],[-142,40,-2,40,-118,-127,-11,-12,-15,-35,-37,-41,40,-13,-10,-38,-40,-14,-36,-42,-142,-143,-39,-141,40,-101,-16,-130,-3,-18,-128,-24,-17,]),'INT':([20,36,71,75,76,77,99,100,101,102,103,104,106,107,108,109,110,133,134,143,167,171,172,185,190,208,209,210,211,212,213,214,216,217,218,219,223,224,236,],[68,68,-78,68,-77,68,-86,-85,68,-83,-84,68,68,-79,-80,68,68,-62,68,68,68,68,68,68,-102,68,-72,-71,-69,-70,-73,-68,-66,-65,-62,68,68,68,68,]),'LOOP':([50,52,57,58,59,60,61,62,63,64,65,68,72,73,74,78,111,140,147,148,151,157,175,178,181,184,186,201,234,237,239,241,245,],[-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,-89,-61,-58,-43,-75,-62,-48,-82,-76,-91,203,-63,-108,-52,-51,-112,-67,-113,-27,247,-64,]),'.':([50,51,52,70,78,146,147,],[-46,96,-47,-47,96,96,-48,]),'FUNCTION':([0,1,4,5,10,11,13,14,16,17,18,19,21,25,26,27,28,29,31,32,33,34,35,37,39,43,44,45,46,47,53,54,55,56,83,85,95,97,98,119,120,123,150,169,183,192,221,],[-133,-8,9,-135,-144,-142,9,-134,-8,9,-145,-9,-2,-138,-118,-127,-11,-12,-15,-35,-37,-41,9,-13,-10,-38,-40,-14,-36,-42,-137,-140,-142,-8,-143,-39,-141,-139,-136,-101,-16,-130,-3,-18,-128,-24,-17,]),'WITH':([0,1,4,5,10,11,14,16,17,18,19,21,25,26,53,54,55,56,83,95,97,98,123,150,183,],[-133,-8,15,-135,-144,-142,-134,-8,15,-145,-9,-2,-138,-118,-137,-140,-142,-8,-143,-141,-139,-136,-130,-3,-128,]),'IN':([182,],[219,]),'$end':([0,1,2,4,5,10,14,16,18,19,21,26,53,56,98,150,183,],[-133,-8,0,-1,-135,-144,-134,-8,-145,-9,-2,-118,-137,-8,-136,-3,-128,]),':':([23,30,42,50,52,57,78,113,114,124,147,162,184,186,187,188,],[-21,-19,91,-46,-47,-44,-43,158,-19,-20,-48,190,-52,-51,-45,-126,]),'NEW':([171,],[200,]),'=':([50,52,57,58,59,60,61,62,63,64,65,68,72,73,74,78,111,147,148,151,157,179,184,186,],[-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,-89,-61,-58,-43,-75,-48,-82,-76,-91,214,-52,-51,]),'ACCESS':([121,],[163,]),'IDENTIFIER':([3,8,9,13,15,20,21,26,27,28,29,31,32,33,34,35,36,37,38,39,40,43,44,45,46,47,71,75,76,77,81,85,90,91,92,94,96,99,100,101,102,103,104,106,107,108,109,110,117,118,119,120,122,123,130,131,133,134,135,136,137,138,139,141,142,143,144,150,158,159,163,165,167,169,170,171,172,174,176,183,185,190,192,197,200,202,203,205,207,208,209,210,211,212,213,214,215,216,217,218,219,221,222,223,224,227,228,230,231,233,235,236,243,244,248,],[7,23,23,23,50,50,-2,-118,-127,-11,-12,-15,-35,-37,-41,23,50,-13,87,-10,50,-38,-40,-14,-36,-42,-78,50,-77,50,23,-39,23,50,50,50,50,-86,-85,50,-83,-84,50,50,-79,-80,50,50,50,23,-101,-16,50,-130,-98,-92,-62,50,-97,-95,-96,-100,-99,-94,-62,50,182,-3,50,23,50,23,50,-18,-129,50,50,-116,50,-128,50,-102,-24,50,50,-117,50,-93,-62,50,-72,-71,-69,-70,-73,-68,-62,-66,-65,-62,50,-17,23,50,50,-104,-103,-62,-111,50,50,50,-62,-62,-105,]),'(':([6,7,20,22,23,24,36,50,52,57,70,71,72,75,76,77,78,89,99,100,101,102,103,104,106,107,108,109,110,125,128,132,133,134,143,147,161,166,167,171,172,184,185,186,187,190,191,208,209,210,211,212,213,214,216,217,218,219,223,224,236,],[20,-46,77,81,-21,81,77,-46,-47,-44,-47,-78,110,77,-77,77,-43,110,-86,-85,77,-83,-84,77,77,-79,-80,77,77,110,167,110,-62,77,77,-48,110,110,77,77,77,-52,77,-51,110,-102,110,77,-72,-71,-69,-70,-73,-68,-66,-65,-62,77,77,77,77,]),'DOTDOT':([50,52,57,58,59,60,61,62,63,64,65,68,72,73,74,78,111,147,148,151,157,184,186,195,],[-46,-47,-44,-88,-87,-81,-59,-74,-57,-56,-90,-60,-89,-61,-58,-43,-75,-48,-82,-76,-91,-52,-51,223,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'indexed_comp':([20,36,40,75,77,91,92,101,104,106,109,110,117,122,134,143,158,163,167,171,172,176,185,197,200,203,208,219,223,224,233,235,236,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'name_s':([40,],[88,]),'statement':([92,176,203,233,235,],[131,205,131,131,131,]),'char_lit':([20,36,75,77,101,104,106,109,110,134,143,167,171,172,185,208,219,223,224,236,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'basic_loop':([175,],[204,]),'primary':([20,36,75,77,101,104,106,109,110,134,143,167,171,172,185,208,219,223,224,236,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'type_decl':([13,35,],[28,28,]),'array_type':([91,],[126,]),'else_opt':([177,],[206,]),'record_decl':([13,35,],[29,29,]),'pragma_s':([1,16,56,],[5,53,98,]),'param':([81,118,159,165,222,],[116,162,189,116,189,]),'with_clause':([4,17,],[11,55,]),'if_stmt':([92,176,203,233,235,],[139,139,139,139,139,]),'N':([244,],[249,]),'factor':([20,36,75,77,101,104,106,109,110,134,143,167,171,172,185,208,219,223,224,236,],[60,60,60,60,148,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'def_id':([8,9,13,35,81,90,118,159,165,222,],[22,24,30,30,114,124,114,114,114,114,]),'relation':([143,172,236,],[178,178,245,]),'pragma_arg':([20,104,],[67,149,]),'param_s':([81,165,],[115,193,]),'block_body':([48,],[93,]),'value':([110,185,],[155,220,]),'access_decl':([13,35,],[31,31,]),'range_s':([167,],[196,]),'use_clause_opt':([11,55,],[25,97,]),'literal':([20,36,75,77,101,104,106,109,110,134,143,167,171,172,185,208,219,223,224,236,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'type_ind':([91,197,200,],[127,226,229,]),'multiplying':([62,111,151,],[101,101,101,]),'subprog_body':([4,13,17,35,],[18,47,18,47,]),'iter_index_constraint':([128,],[168,]),'c_name_list':([15,],[49,]),'simple_stmt':([92,176,203,233,235,],[141,141,141,141,141,]),'formal_part':([22,24,],[80,80,]),'body':([13,35,],[44,44,]),'statement_s':([92,203,233,235,],[142,230,243,244,]),'value_s':([110,],[156,]),'procedure_call':([92,176,203,233,235,],[130,130,130,130,130,]),'relational':([179,],[208,]),'pragma':([0,5,13,17,35,53,98,],[1,19,33,54,33,19,19,]),'pragma_arg_s':([20,],[66,]),'decl_item':([13,35,],[34,34,]),'name':([20,36,40,75,77,91,92,101,104,106,109,110,117,122,134,143,158,163,167,171,172,176,185,197,200,203,208,219,223,224,233,235,236,],[72,72,89,72,72,125,132,72,72,72,72,72,161,166,72,72,187,191,72,72,72,132,72,125,125,132,72,72,72,72,132,132,72,]),'decl_item_or_body_s':([13,],[35,]),'object_type_def':([91,],[129,]),'lambda_begin':([13,35,],[36,36,]),'subprog_decl':([4,13,17,35,],[10,37,10,37,]),'range':([167,219,224,],[194,237,240,]),'cond_clause':([143,],[177,]),'object_decl':([13,35,],[39,39,]),'parenthesized_primary':([20,36,75,77,101,104,106,109,110,134,143,167,171,172,185,208,219,223,224,236,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'return_stmt':([92,176,203,233,235,],[135,135,135,135,135,]),'logical':([181,],[218,]),'compound_stmt':([92,176,203,233,235,],[136,136,136,136,136,]),'assign_stmt':([92,176,203,233,235,],[137,137,137,137,137,]),'simple_expression':([20,36,77,104,109,110,134,143,167,171,172,185,208,219,223,224,236,],[69,86,112,69,152,154,173,179,195,199,179,154,234,195,239,195,179,]),'compilation':([0,],[4,]),'subprog_spec':([4,13,17,35,],[12,41,12,41,]),'condition':([143,172,],[180,201,]),'subprog_spec_is_push':([4,13,17,35,],[13,13,13,13,]),'comp_unit':([4,],[14,]),'formal_part_opt':([22,24,],[79,82,]),'simple_name':([3,15,20,36,40,75,77,91,92,94,96,101,104,106,109,110,117,122,134,143,158,163,167,171,172,176,185,197,200,203,208,219,223,224,233,235,236,],[6,52,70,52,52,52,52,52,52,52,147,52,70,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'def_id_s':([13,35,81,118,159,165,222,],[42,42,113,113,113,113,113,]),'term':([20,36,75,77,104,106,109,110,134,143,167,171,172,185,208,219,223,224,236,],[62,62,111,62,62,151,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'mark':([158,],[188,]),'derived_type':([171,],[198,]),'adding':([69,86,112,152,154,173,179,195,199,234,239,],[106,106,106,106,106,106,106,106,106,106,106,]),'decl_item_or_body':([13,35,],[43,85,]),'loop_stmt':([92,176,203,233,235,],[138,138,138,138,138,]),'goal_symbol':([0,],[2,]),'numeric_lit':([20,36,75,77,101,104,106,109,110,134,143,167,171,172,185,208,219,223,224,236,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'lambda_decl':([13,35,],[45,45,]),'M':([133,140,142,207,215,218,230,243,244,],[172,175,176,233,235,236,176,176,176,]),'use_clause':([13,25,35,97,],[46,83,46,83,]),'unit':([4,17,],[16,56,]),'context_spec':([4,],[17,]),'decl_part':([13,],[48,]),'iteration':([92,176,203,233,235,],[140,140,140,140,140,]),'unary':([20,36,77,104,109,110,134,143,167,171,172,185,208,219,223,224,236,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'expression':([143,172,],[181,181,]),'decl':([13,35,],[32,32,]),'compound_name':([15,20,36,40,75,77,91,92,94,101,104,106,109,110,117,122,134,143,158,163,167,171,172,176,185,197,200,203,208,219,223,224,233,235,236,],[51,78,78,78,78,78,78,78,146,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'record_def':([121,],[164,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> goal_symbol","S'",1,None,None,None),
  ('goal_symbol -> compilation','goal_symbol',1,'p_goal_symbol','grammar.py',21),
  ('pragma -> PRAGMA IDENTIFIER ;','pragma',3,'p_pragma','grammar.py',29),
  ('pragma -> PRAGMA simple_name ( pragma_arg_s ) ;','pragma',6,'p_pragma','grammar.py',30),
  ('pragma_arg_s -> pragma_arg','pragma_arg_s',1,'p_pragma_arg_s','grammar.py',34),
  ('pragma_arg_s -> pragma_arg_s , pragma_arg','pragma_arg_s',3,'p_pragma_arg_s','grammar.py',35),
  ('pragma_arg -> simple_expression','pragma_arg',1,'p_pragma_arg','grammar.py',40),
  ('pragma_arg -> simple_name ARROW simple_expression','pragma_arg',3,'p_pragma_arg','grammar.py',41),
  ('pragma_s -> <empty>','pragma_s',0,'p_pragma_s','grammar.py',45),
  ('pragma_s -> pragma_s pragma','pragma_s',2,'p_pragma_s','grammar.py',46),
  ('decl -> object_decl','decl',1,'p_decl','grammar.py',50),
  ('decl -> type_decl','decl',1,'p_decl','grammar.py',51),
  ('decl -> record_decl','decl',1,'p_decl','grammar.py',52),
  ('decl -> subprog_decl','decl',1,'p_decl','grammar.py',53),
  ('decl -> lambda_decl','decl',1,'p_decl','grammar.py',54),
  ('decl -> access_decl','decl',1,'p_decl','grammar.py',55),
  ('type_decl -> TYPE IDENTIFIER ;','type_decl',3,'p_type_decl','grammar.py',60),
  ('access_decl -> TYPE IDENTIFIER IS ACCESS name ;','access_decl',6,'p_access_decl','grammar.py',75),
  ('object_decl -> def_id_s : object_type_def ;','object_decl',4,'p_object_decl','grammar.py',93),
  ('def_id_s -> def_id','def_id_s',1,'p_def_id_s','grammar.py',136),
  ('def_id_s -> def_id_s , def_id','def_id_s',3,'p_def_id_s','grammar.py',137),
  ('def_id -> IDENTIFIER','def_id',1,'p_def_id','grammar.py',142),
  ('object_type_def -> type_ind','object_type_def',1,'p_object_type_def','grammar.py',147),
  ('object_type_def -> array_type','object_type_def',1,'p_object_type_def','grammar.py',148),
  ('record_decl -> TYPE IDENTIFIER IS record_def ;','record_decl',5,'p_record_decl','grammar.py',153),
  ('type_ind -> name','type_ind',1,'p_type_ind','grammar.py',172),
  ('derived_type -> NEW type_ind','derived_type',2,'p_derived_type','grammar.py',177),
  ('range -> simple_expression DOTDOT simple_expression','range',3,'p_range','grammar.py',187),
  ('array_type -> ARRAY iter_index_constraint OF type_ind','array_type',4,'p_array_type','grammar.py',198),
  ('iter_index_constraint -> ( range_s )','iter_index_constraint',3,'p_iter_index_constraint','grammar.py',211),
  ('range_s -> range','range_s',1,'p_range_s','grammar.py',216),
  ('range_s -> range_s , range','range_s',3,'p_range_s','grammar.py',217),
  ('record_def -> RECORD param_s ; END RECORD','record_def',5,'p_record_def','grammar.py',222),
  ('decl_part -> <empty>','decl_part',0,'p_decl_part','grammar.py',227),
  ('decl_part -> decl_item_or_body_s','decl_part',1,'p_decl_part','grammar.py',228),
  ('decl_item -> decl','decl_item',1,'p_decl_item','grammar.py',232),
  ('decl_item -> use_clause','decl_item',1,'p_decl_item','grammar.py',233),
  ('decl_item -> pragma','decl_item',1,'p_decl_item','grammar.py',234),
  ('decl_item_or_body_s -> decl_item_or_body','decl_item_or_body_s',1,'p_decl_item_or_body_s','grammar.py',239),
  ('decl_item_or_body_s -> decl_item_or_body_s decl_item_or_body','decl_item_or_body_s',2,'p_decl_item_or_body_s','grammar.py',240),
  ('decl_item_or_body -> body','decl_item_or_body',1,'p_decl_item_or_body','grammar.py',245),
  ('decl_item_or_body -> decl_item','decl_item_or_body',1,'p_decl_item_or_body','grammar.py',246),
  ('body -> subprog_body','body',1,'p_body','grammar.py',251),
  ('name -> compound_name','name',1,'p_name','grammar.py',257),
  ('name -> indexed_comp','name',1,'p_name','grammar.py',258),
  ('mark -> name','mark',1,'p_mark','grammar.py',266),
  ('simple_name -> IDENTIFIER','simple_name',1,'p_simple_name','grammar.py',271),
  ('compound_name -> simple_name','compound_name',1,'p_compound_name','grammar.py',276),
  ('compound_name -> compound_name . simple_name','compound_name',3,'p_compound_name','grammar.py',277),
  ('c_name_list -> compound_name','c_name_list',1,'p_c_name_list','grammar.py',285),
  ('c_name_list -> c_name_list , compound_name','c_name_list',3,'p_c_name_list','grammar.py',286),
  ('indexed_comp -> name ( value_s )','indexed_comp',4,'p_indexed_comp','grammar.py',291),
  ('indexed_comp -> name ( STRING )','indexed_comp',4,'p_indexed_comp','grammar.py',292),
  ('value_s -> value','value_s',1,'p_value_s','grammar.py',421),
  ('value_s -> value_s , value','value_s',3,'p_value_s','grammar.py',422),
  ('value -> simple_expression','value',1,'p_value','grammar.py',427),
  ('literal -> numeric_lit','literal',1,'p_literal','grammar.py',432),
  ('literal -> char_lit','literal',1,'p_literal','grammar.py',433),
  ('literal -> NuLL','literal',1,'p_literal','grammar.py',434),
  ('char_lit -> CHAR','char_lit',1,'p_char_lit','grammar.py',439),
  ('numeric_lit -> INT','numeric_lit',1,'p_numeric_lit1','grammar.py',444),
  ('numeric_lit -> FLOAT','numeric_lit',1,'p_numeric_lit2','grammar.py',449),
  ('M -> <empty>','M',0,'p_M','grammar.py',454),
  ('expression -> relation','expression',1,'p_expression','grammar.py',459),
  ('expression -> expression logical M relation','expression',4,'p_expression','grammar.py',460),
  ('logical -> AND','logical',1,'p_logical','grammar.py',482),
  ('logical -> OR','logical',1,'p_logical','grammar.py',483),
  ('relation -> simple_expression relational simple_expression','relation',3,'p_relation','grammar.py',488),
  ('relational -> =','relational',1,'p_relational','grammar.py',546),
  ('relational -> NEQ','relational',1,'p_relational','grammar.py',547),
  ('relational -> <','relational',1,'p_relational','grammar.py',548),
  ('relational -> LEQ','relational',1,'p_relational','grammar.py',549),
  ('relational -> >','relational',1,'p_relational','grammar.py',550),
  ('relational -> GEQ','relational',1,'p_relational','grammar.py',551),
  ('simple_expression -> term','simple_expression',1,'p_simple_expression','grammar.py',556),
  ('simple_expression -> unary term','simple_expression',2,'p_simple_expression','grammar.py',557),
  ('simple_expression -> simple_expression adding term','simple_expression',3,'p_simple_expression','grammar.py',558),
  ('unary -> +','unary',1,'p_unary','grammar.py',617),
  ('unary -> -','unary',1,'p_unary','grammar.py',618),
  ('adding -> +','adding',1,'p_adding','grammar.py',623),
  ('adding -> -','adding',1,'p_adding','grammar.py',624),
  ('term -> factor','term',1,'p_term','grammar.py',629),
  ('term -> term multiplying factor','term',3,'p_term','grammar.py',630),
  ('multiplying -> *','multiplying',1,'p_multiplying','grammar.py',668),
  ('multiplying -> /','multiplying',1,'p_multiplying','grammar.py',669),
  ('multiplying -> MOD','multiplying',1,'p_multiplying','grammar.py',670),
  ('multiplying -> STARSTAR','multiplying',1,'p_multiplying','grammar.py',671),
  ('factor -> primary','factor',1,'p_factor','grammar.py',677),
  ('primary -> literal','primary',1,'p_primary','grammar.py',682),
  ('primary -> name','primary',1,'p_primary','grammar.py',683),
  ('primary -> parenthesized_primary','primary',1,'p_primary','grammar.py',684),
  ('parenthesized_primary -> ( simple_expression )','parenthesized_primary',3,'p_parenthesized_primary','grammar.py',689),
  ('statement_s -> statement','statement_s',1,'p_statement_s','grammar.py',694),
  ('statement_s -> statement_s M statement','statement_s',3,'p_statement_s','grammar.py',695),
  ('statement -> simple_stmt','statement',1,'p_statement','grammar.py',704),
  ('statement -> compound_stmt','statement',1,'p_statement','grammar.py',705),
  ('simple_stmt -> assign_stmt','simple_stmt',1,'p_simple_stmt','grammar.py',711),
  ('simple_stmt -> return_stmt','simple_stmt',1,'p_simple_stmt','grammar.py',712),
  ('simple_stmt -> procedure_call','simple_stmt',1,'p_simple_stmt','grammar.py',713),
  ('compound_stmt -> if_stmt','compound_stmt',1,'p_compound_stmt','grammar.py',718),
  ('compound_stmt -> loop_stmt','compound_stmt',1,'p_compound_stmt','grammar.py',719),
  ('lambda_decl -> lambda_begin simple_expression ;','lambda_decl',3,'p_lambda_decl','grammar.py',724),
  ('lambda_begin -> def_id ASSIGN LAMBDA param :','lambda_begin',5,'p_lambda_begin','grammar.py',732),
  ('assign_stmt -> name ASSIGN simple_expression ;','assign_stmt',4,'p_assign_stmt','grammar.py',744),
  ('assign_stmt -> name ASSIGN derived_type ;','assign_stmt',4,'p_assign_stmt','grammar.py',745),
  ('if_stmt -> IF cond_clause else_opt END IF ;','if_stmt',6,'p_if_stmt','grammar.py',778),
  ('N -> <empty>','N',0,'p_N','grammar.py',786),
  ('cond_clause -> condition THEN M statement_s N','cond_clause',5,'p_cond_clause','grammar.py',793),
  ('condition -> expression','condition',1,'p_condition','grammar.py',800),
  ('else_opt -> <empty>','else_opt',0,'p_else_opt','grammar.py',811),
  ('else_opt -> ELSE M statement_s','else_opt',3,'p_else_opt','grammar.py',812),
  ('loop_stmt -> iteration M basic_loop ;','loop_stmt',4,'p_loop_stmt','grammar.py',822),
  ('iteration -> WHILE M condition','iteration',3,'p_iteration','grammar.py',831),
  ('iteration -> FOR IDENTIFIER IN range','iteration',4,'p_iteration','grammar.py',832),
  ('basic_loop -> LOOP statement_s END LOOP','basic_loop',4,'p_basic_loop','grammar.py',850),
  ('block_body -> BEGIN statement_s','block_body',2,'p_block_body','grammar.py',855),
  ('return_stmt -> RETURN ;','return_stmt',2,'p_return_stmt','grammar.py',860),
  ('return_stmt -> RETURN simple_expression ;','return_stmt',3,'p_return_stmt','grammar.py',861),
  ('subprog_decl -> subprog_spec ;','subprog_decl',2,'p_subprog_decl','grammar.py',870),
  ('subprog_spec -> PROCEDURE def_id formal_part_opt','subprog_spec',3,'p_subprog_spec','grammar.py',875),
  ('subprog_spec -> FUNCTION def_id formal_part_opt RETURN name','subprog_spec',5,'p_subprog_spec','grammar.py',876),
  ('formal_part_opt -> <empty>','formal_part_opt',0,'p_formal_part_opt','grammar.py',894),
  ('formal_part_opt -> formal_part','formal_part_opt',1,'p_formal_part_opt','grammar.py',895),
  ('formal_part -> ( param_s )','formal_part',3,'p_formal_part','grammar.py',900),
  ('param_s -> param','param_s',1,'p_param_s','grammar.py',905),
  ('param_s -> param_s ; param','param_s',3,'p_param_s','grammar.py',906),
  ('param -> def_id_s : mark','param',3,'p_param','grammar.py',915),
  ('subprog_spec_is_push -> subprog_spec IS','subprog_spec_is_push',2,'p_subprog_spec_is_push','grammar.py',929),
  ('subprog_body -> subprog_spec_is_push decl_part block_body END ;','subprog_body',5,'p_subprog_body','grammar.py',942),
  ('procedure_call -> name ;','procedure_call',2,'p_procedure_call','grammar.py',954),
  ('use_clause -> USE name_s ;','use_clause',3,'p_use_clause','grammar.py',970),
  ('name_s -> name','name_s',1,'p_name_s','grammar.py',975),
  ('name_s -> name_s , name','name_s',3,'p_name_s','grammar.py',976),
  ('compilation -> <empty>','compilation',0,'p_compilation','grammar.py',981),
  ('compilation -> compilation comp_unit','compilation',2,'p_compilation','grammar.py',982),
  ('compilation -> pragma pragma_s','compilation',2,'p_compilation','grammar.py',983),
  ('comp_unit -> context_spec unit pragma_s','comp_unit',3,'p_comp_unit','grammar.py',987),
  ('comp_unit -> unit pragma_s','comp_unit',2,'p_comp_unit','grammar.py',988),
  ('context_spec -> with_clause use_clause_opt','context_spec',2,'p_context_spec','grammar.py',992),
  ('context_spec -> context_spec with_clause use_clause_opt','context_spec',3,'p_context_spec','grammar.py',993),
  ('context_spec -> context_spec pragma','context_spec',2,'p_context_spec','grammar.py',994),
  ('with_clause -> WITH c_name_list ;','with_clause',3,'p_with_clause','grammar.py',998),
  ('use_clause_opt -> <empty>','use_clause_opt',0,'p_use_clause_opt','grammar.py',1002),
  ('use_clause_opt -> use_clause_opt use_clause','use_clause_opt',2,'p_use_clause_opt','grammar.py',1003),
  ('unit -> subprog_decl','unit',1,'p_unit','grammar.py',1007),
  ('unit -> subprog_body','unit',1,'p_unit','grammar.py',1008),
]
