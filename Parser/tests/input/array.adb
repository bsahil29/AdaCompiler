with Ada.Text_IO;
use Ada.Text_IO;

procedure demo is
	squares: array (1 .. 10) of integer;
	i : Integer;
	begin
		i := 1;
		while i < 10 loop
			squares(i) := i * 2;
			i := i + 5;
		end loop;
	end demo;