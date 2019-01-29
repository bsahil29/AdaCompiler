-- stats.adb:  compute average, standard deviation of array of values
 
 with Ada.Float_Text_IO, Ada.Integer_Text_IO, Ada.Text_IO;
 with Ada.Numerics.Elementary_Functions; --Functions like sqrt
 use Ada, Ada.Numerics.Elementary_Functions;
 
 procedure Stats is
    --Defining array types
    type Scores_Type is array (1 .. 10) of Integer;
    Scores : Scores_Type := (39, 78, 51, 53, 81, 42, 69, 72, 79, 53);
    Sum: Integer;
    Average, Deviation: Float;
 
 begin
    -- Sum "Scores"
    Sum := -1 ; 
    Sum := 0;
    for I in Scores'Range loop
       Sum := Sum + Scores(I);
    end loop;
    Text_IO.Put ("Sum is ");
    Integer_Text_IO.Put (Sum, Width=>0);
    Text_IO.New_Line;

    --Type casting
    Average := Float(Sum) / Float(Scores'Length);
    Text_IO.Put ("Average is ");
    Float_Text_IO.Put (Average, Aft=>2, Exp=>0);
    Text_IO.New_Line;