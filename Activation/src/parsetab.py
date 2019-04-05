
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "goal_symbolAND ARRAY ARROW ASSIGN BEGIN BODY BOX CHAR DOTDOT ELSE END FLOAT FOR FUNCTION GEQ IDENTIFIER IF IN INT IS LAMBDA LEQ LL LOOP MOD NEQ OF OR PRAGMA PROCEDURE RECORD RETURN RR STARSTAR STRING THEN TICK TYPE USE WHILE WITHgoal_symbol : compilation\n\tpragma : PRAGMA IDENTIFIER ';'\n\t   | PRAGMA simple_name '(' pragma_arg_s ')' ';'\n\tpragma_arg_s : pragma_arg\n\t   | pragma_arg_s ',' pragma_arg\n\tpragma_arg : simple_expression\n\t   | simple_name ARROW simple_expression\n\tpragma_s :\n\t   | pragma_s pragma\n\tdecl : object_decl\n\t   | record_decl\n\t   | subprog_decl\n\t   | lambda_decl\n\tobject_decl : def_id_s ':' object_type_def ';'   \n\tdef_id_s : def_id\n\t   | def_id_s ',' def_id\n\tdef_id  : IDENTIFIER\n\tobject_type_def : type_ind\n\t   | array_type\n\trecord_decl : TYPE IDENTIFIER IS record_def ';'\n\ttype_ind : name\n\trange : simple_expression DOTDOT simple_expression\n\tarray_type : ARRAY iter_index_constraint OF type_ind\n\titer_index_constraint : '(' range_s ')'\n\trange_s : range\n\t   | range_s ',' range\n\trecord_def : RECORD param_s ';' END RECORD\n\tdecl_part :\n\t   | decl_item_or_body_s\n\tdecl_item : decl\n\t   | use_clause\n\t   | pragma\n\tdecl_item_or_body_s : decl_item_or_body\n\t   | decl_item_or_body_s decl_item_or_body\n\tdecl_item_or_body : body\n\t   | decl_item\n\tbody : subprog_body\n\tname : compound_name\n\t   | indexed_comp\n\tmark : name\n\tsimple_name : IDENTIFIER\n\tcompound_name : simple_name\n\t   | compound_name '.' simple_name\n\tc_name_list : compound_name\n\t    | c_name_list ',' compound_name\n\tindexed_comp : name '(' value_s ')'\n\t\t| name '(' STRING ')'\n\tvalue_s : value\n\t   | value_s ',' value\n\tvalue : simple_expression\n\tliteral : numeric_lit\n\tnumeric_lit : INT\n\tnumeric_lit : FLOAT\n\t M : \n\texpression : relation\n\t   | expression logical M relation\n\tlogical : AND\n\t   | OR\n\trelation : simple_expression relational simple_expression\n\trelational : '='\n\t   | NEQ\n\t   | '<'\n\t   | LEQ\n\t   | '>'\n\t   | GEQ\n\tsimple_expression : term\n\t   | simple_expression adding term\n\tadding  : '+'\n\t   | '-'\n\tterm : factor\n\t   | term multiplying factor\n\tmultiplying : '*'\n\t   | '/'\n\t   | MOD\n\t   | STARSTAR\n\tfactor : primary\n\tprimary : literal\n\t   | name\n\t   | parenthesized_primary\n\tparenthesized_primary : '(' simple_expression ')'\n\tstatement_s : statement\n\t   | statement_s M statement\n\tstatement : simple_stmt\n\t\t| compound_stmt\n\tsimple_stmt : assign_stmt\n\t   | return_stmt\n\t   | procedure_call\n\tcompound_stmt : if_stmt\n\t   | loop_stmt\n\tlambda_decl : lambda_begin simple_expression ';'\n\tlambda_begin : def_id ASSIGN LAMBDA param ':'\n\tassign_stmt : name ASSIGN simple_expression ';'\n\tif_stmt : IF cond_clause else_opt END IF ';'\n\tN :\n\tcond_clause : condition THEN M statement_s N\n\tcondition : expression\n\telse_opt :\n\t   | ELSE M statement_s\n\tloop_stmt : iteration M basic_loop ';'\n\titeration : WHILE M condition\n\t\t| FOR IDENTIFIER IN range\n\tbasic_loop : LOOP statement_s END LOOP\n\tblock_body : BEGIN statement_s\n\treturn_stmt : RETURN ';'\n\t   | RETURN simple_expression ';'\n\tsubprog_decl : subprog_spec ';'\n\tsubprog_spec : PROCEDURE def_id formal_part_opt\n\t   | FUNCTION def_id formal_part_opt RETURN name\n\tformal_part_opt : \n\t   | formal_part\n\tformal_part : '(' param_s ')'\n\tparam_s : param\n\t   | param_s ';' param\n\tparam : def_id_s ':' mark\n\tsubprog_spec_is_push : subprog_spec IS\n\tsubprog_body : subprog_spec_is_push decl_part block_body END ';'\n\tprocedure_call : name ';'\n\tuse_clause : USE name_s ';'\n\tname_s : name\n\t   | name_s ',' name\n\tcompilation :\n\t   | compilation comp_unit\n\t   | pragma pragma_s\n\tcomp_unit : context_spec unit pragma_s\n\t   | unit pragma_s\n\tcontext_spec : with_clause use_clause_opt\n\t   | context_spec with_clause use_clause_opt\n\t   | context_spec pragma\n\twith_clause : WITH c_name_list ';'\n\tuse_clause_opt :\n\t   | use_clause_opt use_clause\n\tunit : subprog_decl\n\t   | subprog_body\n\t"
    
_lr_action_items = {'>':([52,53,55,56,58,59,60,62,63,66,68,69,70,136,138,139,140,158,173,175,],[-41,-42,-53,-70,-51,-66,-52,-39,-78,-38,-79,-77,-76,-43,-67,-71,-80,185,-47,-46,]),':':([22,36,48,52,53,62,66,104,106,116,136,172,173,175,176,177,],[-17,80,-15,-41,-42,-39,-38,148,-15,-16,-43,205,-47,-46,-114,-40,]),'USE':([12,15,19,23,24,26,29,31,33,34,35,37,38,39,40,41,43,47,49,74,76,87,90,109,134,147,155,169,204,],[-130,32,-2,-115,-106,32,-130,-11,-12,-13,-32,-31,-35,-33,-36,-10,-30,-37,32,-131,32,-34,-129,-118,-90,-3,-14,-116,-20,]),'-':([52,53,55,56,57,58,59,60,62,63,65,66,68,69,70,85,99,136,138,139,140,143,145,158,165,173,175,180,197,213,221,],[-41,-42,-53,-70,91,-51,-66,-52,-39,-78,-42,-38,-79,-77,-76,91,91,-43,-67,-71,-80,91,91,91,91,-47,-46,91,91,91,91,]),'FOR':([82,117,118,119,122,124,125,127,129,130,163,164,167,184,192,198,200,201,212,214,217,218,219,223,224,230,],[120,-84,-83,-89,-81,-85,-88,-86,-54,-87,-117,-104,120,-54,-54,-105,120,-82,120,120,-92,-99,-54,-54,-54,-93,]),'LEQ':([52,53,55,56,58,59,60,62,63,66,68,69,70,136,138,139,140,158,173,175,],[-41,-42,-53,-70,-51,-66,-52,-39,-78,-38,-79,-77,-76,-43,-67,-71,-80,188,-47,-46,]),'BEGIN':([15,19,23,24,31,33,34,35,37,38,39,40,41,42,43,47,49,87,109,134,147,155,169,204,],[-28,-2,-115,-106,-11,-12,-13,-32,-31,-35,-33,-36,-10,82,-30,-37,-29,-34,-118,-90,-3,-14,-116,-20,]),'OF':([154,209,],[182,-24,]),'THEN':([52,53,55,56,58,59,60,62,63,66,68,69,70,136,138,139,140,157,160,161,173,175,213,226,],[-41,-42,-53,-70,-51,-66,-52,-39,-78,-38,-79,-77,-76,-43,-67,-71,-80,184,-96,-55,-47,-46,-59,-56,]),'WHILE':([82,117,118,119,122,124,125,127,129,130,163,164,167,184,192,198,200,201,212,214,217,218,219,223,224,230,],[131,-84,-83,-89,-81,-85,-88,-86,-54,-87,-117,-104,131,-54,-54,-105,131,-82,131,131,-92,-99,-54,-54,-54,-93,]),'<':([52,53,55,56,58,59,60,62,63,66,68,69,70,136,138,139,140,158,173,175,],[-41,-42,-53,-70,-51,-66,-52,-39,-78,-38,-79,-77,-76,-43,-67,-71,-80,190,-47,-46,]),'ELSE':([117,118,119,122,124,125,127,130,159,163,164,198,201,217,218,223,229,230,],[-84,-83,-89,-81,-85,-88,-86,-87,192,-117,-104,-105,-82,-92,-99,-94,-95,-93,]),'=':([52,53,55,56,58,59,60,62,63,66,68,69,70,136,138,139,140,158,173,175,],[-41,-42,-53,-70,-51,-66,-52,-39,-78,-38,-79,-77,-76,-43,-67,-71,-80,191,-47,-46,]),'STARSTAR':([52,53,55,56,58,59,60,62,63,65,66,68,69,70,136,138,139,140,173,175,],[-41,-42,-53,-70,-51,96,-52,-39,-78,-42,-38,-79,-77,-76,-43,96,-71,-80,-47,-46,]),'FUNCTION':([0,2,4,8,10,11,12,13,15,17,18,19,23,24,25,26,27,28,29,31,33,34,35,37,38,39,40,41,43,47,49,54,74,75,76,87,90,109,134,147,155,169,204,],[-121,14,-8,-122,-8,-132,-130,14,14,-133,-123,-2,-115,-106,-125,-126,-8,-128,-130,-11,-12,-13,-32,-31,-35,-33,-36,-10,-30,-37,14,-9,-131,-124,-127,-34,-129,-118,-90,-3,-14,-116,-20,]),'PRAGMA':([0,4,10,11,12,13,15,17,18,19,23,24,25,26,27,28,29,31,33,34,35,37,38,39,40,41,43,47,49,54,74,75,76,87,90,109,134,147,155,169,204,],[1,-8,-8,-132,-130,1,1,-133,1,-2,-115,-106,1,-126,-8,-128,-130,-11,-12,-13,-32,-31,-35,-33,-36,-10,-30,-37,1,-9,-131,1,-127,-34,-129,-118,-90,-3,-14,-116,-20,]),'DOTDOT':([52,53,55,56,58,59,60,62,63,66,68,69,70,136,138,139,140,173,175,180,],[-41,-42,-53,-70,-51,-66,-52,-39,-78,-38,-79,-77,-76,-43,-67,-71,-80,-47,-46,207,]),'STRING':([100,],[141,]),'AND':([52,53,55,56,58,59,60,62,63,66,68,69,70,136,138,139,140,160,161,173,175,213,226,],[-41,-42,-53,-70,-51,-66,-52,-39,-78,-38,-79,-77,-76,-43,-67,-71,-80,194,-55,-47,-46,-59,-56,]),'WITH':([0,2,4,8,10,11,12,13,17,18,19,24,25,26,27,28,29,54,74,75,76,90,109,147,169,],[-121,16,-8,-122,-8,-132,-130,16,-133,-123,-2,-106,-125,-126,-8,-128,-130,-9,-131,-124,-127,-129,-118,-3,-116,]),'ASSIGN':([22,48,52,53,62,66,123,136,173,175,],[-17,86,-41,-42,-39,-38,162,-43,-47,-46,]),'IF':([82,117,118,119,122,124,125,127,129,130,163,164,167,184,192,198,200,201,212,214,215,217,218,219,223,224,230,],[121,-84,-83,-89,-81,-85,-88,-86,-54,-87,-117,-104,121,-54,-54,-105,121,-82,121,121,225,-92,-99,-54,-54,-54,-93,]),'ARROW':([52,65,],[-41,101,]),'+':([52,53,55,56,57,58,59,60,62,63,65,66,68,69,70,85,99,136,138,139,140,143,145,158,165,173,175,180,197,213,221,],[-41,-42,-53,-70,92,-51,-66,-52,-39,-78,-42,-38,-79,-77,-76,92,92,-43,-67,-71,-80,92,92,92,92,-47,-46,92,92,92,92,]),'IS':([9,21,22,45,52,53,62,66,71,72,84,136,150,151,173,175,],[23,-109,-17,23,-41,-42,-39,-38,-107,-110,133,-43,-111,-108,-47,-46,]),'FLOAT':([20,46,61,91,92,93,94,95,96,97,98,100,101,102,121,126,131,153,162,168,174,183,185,186,187,188,189,190,191,194,195,196,205,207,208,216,],[55,55,55,-69,-68,55,-73,55,-75,-72,-74,55,55,55,55,55,-54,55,55,55,55,55,-64,-61,55,-63,-65,-62,-60,-57,-54,-58,-91,55,55,55,]),'PROCEDURE':([0,2,4,8,10,11,12,13,15,17,18,19,23,24,25,26,27,28,29,31,33,34,35,37,38,39,40,41,43,47,49,54,74,75,76,87,90,109,134,147,155,169,204,],[-121,7,-8,-122,-8,-132,-130,7,7,-133,-123,-2,-115,-106,-125,-126,-8,-128,-130,-11,-12,-13,-32,-31,-35,-33,-36,-10,-30,-37,7,-9,-131,-124,-127,-34,-129,-118,-90,-3,-14,-116,-20,]),'ARRAY':([80,],[112,]),'NEQ':([52,53,55,56,58,59,60,62,63,66,68,69,70,136,138,139,140,158,173,175,],[-41,-42,-53,-70,-51,-66,-52,-39,-78,-38,-79,-77,-76,-43,-67,-71,-80,186,-47,-46,]),',':([22,36,48,50,51,52,53,55,56,57,58,59,60,62,63,64,65,66,67,68,69,70,78,79,104,106,116,136,137,138,139,140,142,143,144,145,146,152,173,175,179,181,206,221,222,],[-17,81,-15,-44,89,-41,-42,-53,-70,-6,-51,-66,-52,-39,-78,-4,-42,-38,102,-79,-77,-76,110,-119,81,-15,-16,-43,-45,-67,-71,-80,-48,-50,174,-7,-5,-120,-47,-46,-25,208,-49,-22,-26,]),';':([5,9,21,22,45,50,51,52,53,55,56,58,59,60,62,63,66,68,69,70,71,72,78,79,85,103,105,107,111,113,114,115,123,126,132,136,137,138,139,140,150,151,152,165,171,173,175,176,177,178,197,199,203,210,225,231,232,],[19,24,-109,-17,24,-44,90,-41,-42,-53,-70,-51,-66,-52,-39,-78,-38,-79,-77,-76,-107,-110,109,-119,134,147,149,-112,-18,155,-21,-19,163,164,169,-43,-45,-67,-71,-80,-111,-108,-120,198,204,-47,-46,-114,-40,-113,217,218,220,-23,230,-102,-27,]),'GEQ':([52,53,55,56,58,59,60,62,63,66,68,69,70,136,138,139,140,158,173,175,],[-41,-42,-53,-70,-51,-66,-52,-39,-78,-38,-79,-77,-76,-43,-67,-71,-80,189,-47,-46,]),'.':([50,52,53,65,66,136,137,],[88,-41,-42,-42,88,-43,88,]),'OR':([52,53,55,56,58,59,60,62,63,66,68,69,70,136,138,139,140,160,161,173,175,213,226,],[-41,-42,-53,-70,-51,-66,-52,-39,-78,-38,-79,-77,-76,-43,-67,-71,-80,196,-55,-47,-46,-59,-56,]),'INT':([20,46,61,91,92,93,94,95,96,97,98,100,101,102,121,126,131,153,162,168,174,183,185,186,187,188,189,190,191,194,195,196,205,207,208,216,],[60,60,60,-69,-68,60,-73,60,-75,-72,-74,60,60,60,60,60,-54,60,60,60,60,60,-64,-61,60,-63,-65,-62,-60,-57,-54,-58,-91,60,60,60,]),'IDENTIFIER':([1,7,14,15,16,19,20,23,24,31,32,33,34,35,37,38,39,40,41,43,44,46,47,49,61,73,80,81,82,87,88,89,91,92,93,94,95,96,97,98,100,101,102,108,109,110,117,118,119,120,121,122,124,125,126,127,129,130,131,134,135,147,148,149,153,155,162,163,164,167,168,169,170,174,182,183,184,185,186,187,188,189,190,191,192,194,195,196,198,200,201,204,205,207,208,212,214,216,217,218,219,220,223,224,230,],[5,22,22,22,52,-2,52,-115,-106,-11,52,-12,-13,-32,-31,-35,-33,-36,-10,-30,84,52,-37,22,52,22,52,22,52,-34,52,52,-69,-68,52,-73,52,-75,-72,-74,52,52,52,52,-118,52,-84,-83,-89,156,52,-81,-85,-88,52,-86,-54,-87,-54,-90,22,-3,52,22,52,-14,52,-117,-104,52,52,-116,22,52,52,52,-54,-64,-61,52,-63,-65,-62,-60,-54,-57,-54,-58,-105,52,-82,-20,-91,52,52,52,52,52,-92,-99,-54,22,-54,-54,-93,]),'(':([5,6,20,21,22,30,46,52,53,61,62,63,65,66,79,91,92,93,94,95,96,97,98,100,101,102,112,114,121,123,126,131,136,151,152,153,162,168,173,174,175,177,183,185,186,187,188,189,190,191,194,195,196,205,207,208,216,],[-41,20,61,73,-17,73,61,-41,-42,61,-39,100,-42,-38,100,-69,-68,61,-73,61,-75,-72,-74,61,61,61,153,100,61,100,61,-54,-43,100,100,61,61,61,-47,61,-46,100,61,-64,-61,61,-63,-65,-62,-60,-57,-54,-58,-91,61,61,61,]),'*':([52,53,55,56,58,59,60,62,63,65,66,68,69,70,136,138,139,140,173,175,],[-41,-42,-53,-70,-51,97,-52,-39,-78,-42,-38,-79,-77,-76,-43,97,-71,-80,-47,-46,]),')':([52,53,55,56,57,58,59,60,62,63,64,65,66,67,68,69,70,99,105,107,136,138,139,140,141,142,143,144,145,146,173,175,176,177,178,179,181,206,221,222,],[-41,-42,-53,-70,-6,-51,-66,-52,-39,-78,-4,-42,-38,103,-79,-77,-76,140,150,-112,-43,-67,-71,-80,173,-48,-50,175,-7,-5,-47,-46,-114,-40,-113,-25,209,-49,-22,-26,]),'/':([52,53,55,56,58,59,60,62,63,65,66,68,69,70,136,138,139,140,173,175,],[-41,-42,-53,-70,-51,94,-52,-39,-78,-42,-38,-79,-77,-76,-43,94,-71,-80,-47,-46,]),'RECORD':([133,228,],[170,232,]),'$end':([0,2,3,4,8,10,11,17,18,19,24,25,27,54,75,147,169,],[-121,-1,0,-8,-122,-8,-132,-133,-123,-2,-106,-125,-8,-9,-124,-3,-116,]),'TYPE':([15,19,23,24,31,33,34,35,37,38,39,40,41,43,47,49,87,109,134,147,155,169,204,],[44,-2,-115,-106,-11,-12,-13,-32,-31,-35,-33,-36,-10,-30,-37,44,-34,-118,-90,-3,-14,-116,-20,]),'IN':([156,],[183,]),'LOOP':([52,53,55,56,58,59,60,62,63,66,68,69,70,128,136,138,139,140,160,161,166,173,175,202,211,213,221,226,227,],[-41,-42,-53,-70,-51,-66,-52,-39,-78,-38,-79,-77,-76,-54,-43,-67,-71,-80,-96,-55,200,-47,-46,-100,-101,-59,-22,-56,231,]),'RETURN':([22,30,72,77,82,117,118,119,122,124,125,127,129,130,150,163,164,167,184,192,198,200,201,212,214,217,218,219,223,224,230,],[-17,-109,-110,108,126,-84,-83,-89,-81,-85,-88,-86,-54,-87,-111,-117,-104,126,-54,-54,-105,126,-82,126,126,-92,-99,-54,-54,-54,-93,]),'MOD':([52,53,55,56,58,59,60,62,63,65,66,68,69,70,136,138,139,140,173,175,],[-41,-42,-53,-70,-51,98,-52,-39,-78,-42,-38,-79,-77,-76,-43,98,-71,-80,-47,-46,]),'END':([83,117,118,119,122,124,125,127,129,130,159,163,164,193,198,201,217,218,219,220,223,224,229,230,],[132,-84,-83,-89,-81,-85,-88,-86,-103,-87,-97,-117,-104,215,-105,-82,-92,-99,227,228,-94,-98,-95,-93,]),'LAMBDA':([86,],[135,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'M':([128,129,131,184,192,195,219,223,224,],[166,167,168,212,214,216,167,167,167,]),'record_decl':([15,49,],[31,31,]),'use_clause_opt':([12,29,],[26,76,]),'record_def':([133,],[171,]),'param_s':([73,170,],[105,203,]),'simple_name':([1,16,20,32,46,61,80,82,88,89,93,95,100,101,102,108,110,121,126,148,153,162,167,168,174,182,183,187,200,207,208,212,214,216,],[6,53,65,53,53,53,53,53,136,53,53,53,53,53,65,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'mark':([148,],[176,]),'simple_expression':([20,46,61,100,101,102,121,126,153,162,168,174,183,187,207,208,216,],[57,85,99,143,145,57,158,165,180,197,158,143,180,213,221,180,158,]),'loop_stmt':([82,167,200,212,214,],[119,119,119,119,119,]),'def_id':([7,14,15,49,73,81,135,149,170,220,],[21,30,48,48,106,116,106,106,106,106,]),'subprog_decl':([2,13,15,49,],[11,11,33,33,]),'expression':([121,168,],[160,160,]),'formal_part':([21,30,],[72,72,]),'term':([20,46,61,93,100,101,102,121,126,153,162,168,174,183,187,207,208,216,],[59,59,59,138,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'statement':([82,167,200,212,214,],[122,201,122,122,122,]),'indexed_comp':([20,32,46,61,80,82,93,95,100,101,102,108,110,121,126,148,153,162,167,168,174,182,183,187,200,207,208,212,214,216,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'N':([223,],[229,]),'lambda_decl':([15,49,],[34,34,]),'pragma':([0,13,15,18,25,49,75,],[4,28,35,54,54,35,54,]),'if_stmt':([82,167,200,212,214,],[125,125,125,125,125,]),'with_clause':([2,13,],[12,29,]),'name_s':([32,],[78,]),'context_spec':([2,],[13,]),'c_name_list':([16,],[51,]),'return_stmt':([82,167,200,212,214,],[127,127,127,127,127,]),'def_id_s':([15,49,73,135,149,170,220,],[36,36,104,104,104,104,104,]),'param':([73,135,149,170,220,],[107,172,178,107,178,]),'relational':([158,],[187,]),'use_clause':([15,26,49,76,],[37,74,37,74,]),'compound_name':([16,20,32,46,61,80,82,89,93,95,100,101,102,108,110,121,126,148,153,162,167,168,174,182,183,187,200,207,208,212,214,216,],[50,66,66,66,66,66,66,137,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'pragma_s':([4,10,27,],[18,25,75,]),'statement_s':([82,200,212,214,],[129,219,223,224,]),'compilation':([0,],[2,]),'relation':([121,168,216,],[161,161,226,]),'parenthesized_primary':([20,46,61,93,95,100,101,102,121,126,153,162,168,174,183,187,207,208,216,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'iter_index_constraint':([112,],[154,]),'cond_clause':([121,],[159,]),'body':([15,49,],[38,38,]),'subprog_spec':([2,13,15,49,],[9,9,45,45,]),'basic_loop':([166,],[199,]),'range':([153,183,208,],[179,211,222,]),'primary':([20,46,61,93,95,100,101,102,121,126,153,162,168,174,183,187,207,208,216,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'factor':([20,46,61,93,95,100,101,102,121,126,153,162,168,174,183,187,207,208,216,],[56,56,56,56,139,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'range_s':([153,],[181,]),'compound_stmt':([82,167,200,212,214,],[117,117,117,117,117,]),'condition':([121,168,],[157,202,]),'procedure_call':([82,167,200,212,214,],[130,130,130,130,130,]),'simple_stmt':([82,167,200,212,214,],[118,118,118,118,118,]),'comp_unit':([2,],[8,]),'numeric_lit':([20,46,61,93,95,100,101,102,121,126,153,162,168,174,183,187,207,208,216,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'unit':([2,13,],[10,27,]),'literal':([20,46,61,93,95,100,101,102,121,126,153,162,168,174,183,187,207,208,216,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'logical':([160,],[195,]),'name':([20,32,46,61,80,82,93,95,100,101,102,108,110,121,126,148,153,162,167,168,174,182,183,187,200,207,208,212,214,216,],[63,79,63,63,114,123,63,63,63,63,63,151,152,63,63,177,63,63,123,63,63,114,63,63,123,63,63,123,123,63,]),'object_decl':([15,49,],[41,41,]),'else_opt':([159,],[193,]),'assign_stmt':([82,167,200,212,214,],[124,124,124,124,124,]),'adding':([57,85,99,143,145,158,165,180,197,213,221,],[93,93,93,93,93,93,93,93,93,93,93,]),'type_ind':([80,182,],[111,210,]),'decl_item':([15,49,],[40,40,]),'decl':([15,49,],[43,43,]),'pragma_arg':([20,102,],[64,146,]),'object_type_def':([80,],[113,]),'decl_item_or_body':([15,49,],[39,87,]),'iteration':([82,167,200,212,214,],[128,128,128,128,128,]),'subprog_spec_is_push':([2,13,15,49,],[15,15,15,15,]),'block_body':([42,],[83,]),'decl_item_or_body_s':([15,],[49,]),'lambda_begin':([15,49,],[46,46,]),'pragma_arg_s':([20,],[67,]),'multiplying':([59,138,],[95,95,]),'goal_symbol':([0,],[3,]),'subprog_body':([2,13,15,49,],[17,17,47,47,]),'formal_part_opt':([21,30,],[71,77,]),'value':([100,174,],[142,206,]),'value_s':([100,],[144,]),'decl_part':([15,],[42,]),'array_type':([80,],[115,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> goal_symbol","S'",1,None,None,None),
  ('goal_symbol -> compilation','goal_symbol',1,'p_goal_symbol','grammar.py',18),
  ('pragma -> PRAGMA IDENTIFIER ;','pragma',3,'p_pragma','grammar.py',27),
  ('pragma -> PRAGMA simple_name ( pragma_arg_s ) ;','pragma',6,'p_pragma','grammar.py',28),
  ('pragma_arg_s -> pragma_arg','pragma_arg_s',1,'p_pragma_arg_s','grammar.py',32),
  ('pragma_arg_s -> pragma_arg_s , pragma_arg','pragma_arg_s',3,'p_pragma_arg_s','grammar.py',33),
  ('pragma_arg -> simple_expression','pragma_arg',1,'p_pragma_arg','grammar.py',38),
  ('pragma_arg -> simple_name ARROW simple_expression','pragma_arg',3,'p_pragma_arg','grammar.py',39),
  ('pragma_s -> <empty>','pragma_s',0,'p_pragma_s','grammar.py',43),
  ('pragma_s -> pragma_s pragma','pragma_s',2,'p_pragma_s','grammar.py',44),
  ('decl -> object_decl','decl',1,'p_decl','grammar.py',48),
  ('decl -> record_decl','decl',1,'p_decl','grammar.py',49),
  ('decl -> subprog_decl','decl',1,'p_decl','grammar.py',50),
  ('decl -> lambda_decl','decl',1,'p_decl','grammar.py',51),
  ('object_decl -> def_id_s : object_type_def ;','object_decl',4,'p_object_decl','grammar.py',56),
  ('def_id_s -> def_id','def_id_s',1,'p_def_id_s','grammar.py',91),
  ('def_id_s -> def_id_s , def_id','def_id_s',3,'p_def_id_s','grammar.py',92),
  ('def_id -> IDENTIFIER','def_id',1,'p_def_id','grammar.py',97),
  ('object_type_def -> type_ind','object_type_def',1,'p_object_type_def','grammar.py',102),
  ('object_type_def -> array_type','object_type_def',1,'p_object_type_def','grammar.py',103),
  ('record_decl -> TYPE IDENTIFIER IS record_def ;','record_decl',5,'p_record_decl','grammar.py',108),
  ('type_ind -> name','type_ind',1,'p_type_ind','grammar.py',124),
  ('range -> simple_expression DOTDOT simple_expression','range',3,'p_range','grammar.py',129),
  ('array_type -> ARRAY iter_index_constraint OF type_ind','array_type',4,'p_array_type','grammar.py',140),
  ('iter_index_constraint -> ( range_s )','iter_index_constraint',3,'p_iter_index_constraint','grammar.py',153),
  ('range_s -> range','range_s',1,'p_range_s','grammar.py',158),
  ('range_s -> range_s , range','range_s',3,'p_range_s','grammar.py',159),
  ('record_def -> RECORD param_s ; END RECORD','record_def',5,'p_record_def','grammar.py',164),
  ('decl_part -> <empty>','decl_part',0,'p_decl_part','grammar.py',169),
  ('decl_part -> decl_item_or_body_s','decl_part',1,'p_decl_part','grammar.py',170),
  ('decl_item -> decl','decl_item',1,'p_decl_item','grammar.py',174),
  ('decl_item -> use_clause','decl_item',1,'p_decl_item','grammar.py',175),
  ('decl_item -> pragma','decl_item',1,'p_decl_item','grammar.py',176),
  ('decl_item_or_body_s -> decl_item_or_body','decl_item_or_body_s',1,'p_decl_item_or_body_s','grammar.py',181),
  ('decl_item_or_body_s -> decl_item_or_body_s decl_item_or_body','decl_item_or_body_s',2,'p_decl_item_or_body_s','grammar.py',182),
  ('decl_item_or_body -> body','decl_item_or_body',1,'p_decl_item_or_body','grammar.py',187),
  ('decl_item_or_body -> decl_item','decl_item_or_body',1,'p_decl_item_or_body','grammar.py',188),
  ('body -> subprog_body','body',1,'p_body','grammar.py',193),
  ('name -> compound_name','name',1,'p_name','grammar.py',199),
  ('name -> indexed_comp','name',1,'p_name','grammar.py',200),
  ('mark -> name','mark',1,'p_mark','grammar.py',208),
  ('simple_name -> IDENTIFIER','simple_name',1,'p_simple_name','grammar.py',213),
  ('compound_name -> simple_name','compound_name',1,'p_compound_name','grammar.py',218),
  ('compound_name -> compound_name . simple_name','compound_name',3,'p_compound_name','grammar.py',219),
  ('c_name_list -> compound_name','c_name_list',1,'p_c_name_list','grammar.py',227),
  ('c_name_list -> c_name_list , compound_name','c_name_list',3,'p_c_name_list','grammar.py',228),
  ('indexed_comp -> name ( value_s )','indexed_comp',4,'p_indexed_comp','grammar.py',233),
  ('indexed_comp -> name ( STRING )','indexed_comp',4,'p_indexed_comp','grammar.py',234),
  ('value_s -> value','value_s',1,'p_value_s','grammar.py',304),
  ('value_s -> value_s , value','value_s',3,'p_value_s','grammar.py',305),
  ('value -> simple_expression','value',1,'p_value','grammar.py',310),
  ('literal -> numeric_lit','literal',1,'p_literal','grammar.py',315),
  ('numeric_lit -> INT','numeric_lit',1,'p_numeric_lit1','grammar.py',320),
  ('numeric_lit -> FLOAT','numeric_lit',1,'p_numeric_lit2','grammar.py',325),
  ('M -> <empty>','M',0,'p_M','grammar.py',330),
  ('expression -> relation','expression',1,'p_expression','grammar.py',335),
  ('expression -> expression logical M relation','expression',4,'p_expression','grammar.py',336),
  ('logical -> AND','logical',1,'p_logical','grammar.py',358),
  ('logical -> OR','logical',1,'p_logical','grammar.py',359),
  ('relation -> simple_expression relational simple_expression','relation',3,'p_relation','grammar.py',364),
  ('relational -> =','relational',1,'p_relational','grammar.py',379),
  ('relational -> NEQ','relational',1,'p_relational','grammar.py',380),
  ('relational -> <','relational',1,'p_relational','grammar.py',381),
  ('relational -> LEQ','relational',1,'p_relational','grammar.py',382),
  ('relational -> >','relational',1,'p_relational','grammar.py',383),
  ('relational -> GEQ','relational',1,'p_relational','grammar.py',384),
  ('simple_expression -> term','simple_expression',1,'p_simple_expression','grammar.py',389),
  ('simple_expression -> simple_expression adding term','simple_expression',3,'p_simple_expression','grammar.py',390),
  ('adding -> +','adding',1,'p_adding','grammar.py',423),
  ('adding -> -','adding',1,'p_adding','grammar.py',424),
  ('term -> factor','term',1,'p_term','grammar.py',429),
  ('term -> term multiplying factor','term',3,'p_term','grammar.py',430),
  ('multiplying -> *','multiplying',1,'p_multiplying','grammar.py',466),
  ('multiplying -> /','multiplying',1,'p_multiplying','grammar.py',467),
  ('multiplying -> MOD','multiplying',1,'p_multiplying','grammar.py',468),
  ('multiplying -> STARSTAR','multiplying',1,'p_multiplying','grammar.py',469),
  ('factor -> primary','factor',1,'p_factor','grammar.py',475),
  ('primary -> literal','primary',1,'p_primary','grammar.py',480),
  ('primary -> name','primary',1,'p_primary','grammar.py',481),
  ('primary -> parenthesized_primary','primary',1,'p_primary','grammar.py',482),
  ('parenthesized_primary -> ( simple_expression )','parenthesized_primary',3,'p_parenthesized_primary','grammar.py',487),
  ('statement_s -> statement','statement_s',1,'p_statement_s','grammar.py',492),
  ('statement_s -> statement_s M statement','statement_s',3,'p_statement_s','grammar.py',493),
  ('statement -> simple_stmt','statement',1,'p_statement','grammar.py',502),
  ('statement -> compound_stmt','statement',1,'p_statement','grammar.py',503),
  ('simple_stmt -> assign_stmt','simple_stmt',1,'p_simple_stmt','grammar.py',509),
  ('simple_stmt -> return_stmt','simple_stmt',1,'p_simple_stmt','grammar.py',510),
  ('simple_stmt -> procedure_call','simple_stmt',1,'p_simple_stmt','grammar.py',511),
  ('compound_stmt -> if_stmt','compound_stmt',1,'p_compound_stmt','grammar.py',516),
  ('compound_stmt -> loop_stmt','compound_stmt',1,'p_compound_stmt','grammar.py',517),
  ('lambda_decl -> lambda_begin simple_expression ;','lambda_decl',3,'p_lambda_decl','grammar.py',522),
  ('lambda_begin -> def_id ASSIGN LAMBDA param :','lambda_begin',5,'p_lambda_begin','grammar.py',530),
  ('assign_stmt -> name ASSIGN simple_expression ;','assign_stmt',4,'p_assign_stmt','grammar.py',542),
  ('if_stmt -> IF cond_clause else_opt END IF ;','if_stmt',6,'p_if_stmt','grammar.py',557),
  ('N -> <empty>','N',0,'p_N','grammar.py',565),
  ('cond_clause -> condition THEN M statement_s N','cond_clause',5,'p_cond_clause','grammar.py',572),
  ('condition -> expression','condition',1,'p_condition','grammar.py',579),
  ('else_opt -> <empty>','else_opt',0,'p_else_opt','grammar.py',590),
  ('else_opt -> ELSE M statement_s','else_opt',3,'p_else_opt','grammar.py',591),
  ('loop_stmt -> iteration M basic_loop ;','loop_stmt',4,'p_loop_stmt','grammar.py',601),
  ('iteration -> WHILE M condition','iteration',3,'p_iteration','grammar.py',610),
  ('iteration -> FOR IDENTIFIER IN range','iteration',4,'p_iteration','grammar.py',611),
  ('basic_loop -> LOOP statement_s END LOOP','basic_loop',4,'p_basic_loop','grammar.py',629),
  ('block_body -> BEGIN statement_s','block_body',2,'p_block_body','grammar.py',634),
  ('return_stmt -> RETURN ;','return_stmt',2,'p_return_stmt','grammar.py',639),
  ('return_stmt -> RETURN simple_expression ;','return_stmt',3,'p_return_stmt','grammar.py',640),
  ('subprog_decl -> subprog_spec ;','subprog_decl',2,'p_subprog_decl','grammar.py',649),
  ('subprog_spec -> PROCEDURE def_id formal_part_opt','subprog_spec',3,'p_subprog_spec','grammar.py',654),
  ('subprog_spec -> FUNCTION def_id formal_part_opt RETURN name','subprog_spec',5,'p_subprog_spec','grammar.py',655),
  ('formal_part_opt -> <empty>','formal_part_opt',0,'p_formal_part_opt','grammar.py',673),
  ('formal_part_opt -> formal_part','formal_part_opt',1,'p_formal_part_opt','grammar.py',674),
  ('formal_part -> ( param_s )','formal_part',3,'p_formal_part','grammar.py',679),
  ('param_s -> param','param_s',1,'p_param_s','grammar.py',684),
  ('param_s -> param_s ; param','param_s',3,'p_param_s','grammar.py',685),
  ('param -> def_id_s : mark','param',3,'p_param','grammar.py',693),
  ('subprog_spec_is_push -> subprog_spec IS','subprog_spec_is_push',2,'p_subprog_spec_is_push','grammar.py',707),
  ('subprog_body -> subprog_spec_is_push decl_part block_body END ;','subprog_body',5,'p_subprog_body','grammar.py',717),
  ('procedure_call -> name ;','procedure_call',2,'p_procedure_call','grammar.py',725),
  ('use_clause -> USE name_s ;','use_clause',3,'p_use_clause','grammar.py',734),
  ('name_s -> name','name_s',1,'p_name_s','grammar.py',739),
  ('name_s -> name_s , name','name_s',3,'p_name_s','grammar.py',740),
  ('compilation -> <empty>','compilation',0,'p_compilation','grammar.py',745),
  ('compilation -> compilation comp_unit','compilation',2,'p_compilation','grammar.py',746),
  ('compilation -> pragma pragma_s','compilation',2,'p_compilation','grammar.py',747),
  ('comp_unit -> context_spec unit pragma_s','comp_unit',3,'p_comp_unit','grammar.py',751),
  ('comp_unit -> unit pragma_s','comp_unit',2,'p_comp_unit','grammar.py',752),
  ('context_spec -> with_clause use_clause_opt','context_spec',2,'p_context_spec','grammar.py',756),
  ('context_spec -> context_spec with_clause use_clause_opt','context_spec',3,'p_context_spec','grammar.py',757),
  ('context_spec -> context_spec pragma','context_spec',2,'p_context_spec','grammar.py',758),
  ('with_clause -> WITH c_name_list ;','with_clause',3,'p_with_clause','grammar.py',762),
  ('use_clause_opt -> <empty>','use_clause_opt',0,'p_use_clause_opt','grammar.py',766),
  ('use_clause_opt -> use_clause_opt use_clause','use_clause_opt',2,'p_use_clause_opt','grammar.py',767),
  ('unit -> subprog_decl','unit',1,'p_unit','grammar.py',771),
  ('unit -> subprog_body','unit',1,'p_unit','grammar.py',772),
]
