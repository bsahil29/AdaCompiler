with Ada.Text_IO;
use Ada.Text_IO;

procedure demo is
	procedure main is
		squares: array (1 .. 10, 1 .. 5) of integer;
		i : integer;
	begin
		i := 1 + i*i;
		squares ( i , 5 ) := i * 2;
		squares ( i , 5 ) := squares(i,5) * 2;
		print_int( squares(i,5) );
	end;
begin
	main;
end;