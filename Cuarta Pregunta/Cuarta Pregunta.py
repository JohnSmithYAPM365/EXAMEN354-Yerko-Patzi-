# -*- coding: utf-8 -*-


from kanren import run, var, eq, Relation, facts
a = var()
b = var()

padre = Relation()
primo = Relation()
tio = Relation()
facts(padre, ("Porfirio P","Yerko H"),("Porfirio P","Alex H"),("Tiberio Ab","Porfirio P"), ("Tiberio Ab","Alfredo T"), ("Alfredo T","Rosa H"), ("Alfredo T","Maira H"), ("Alfredo T","Pelayo H"))
facts(primo, ("Yerko H","Maira Pr"),("Alex H","Maira Pr"),("Yerko H","Rosa Pr"),("Alex H"," Rosa Pr"), ("Yerko H","Pelayo Pr"), ("Alex H","Pelayo Pr"))
facts(tio, ("Yerko H","Alfredo T"),("Alex H","Alfredo T"),("Rosa Pr", "Porfirio T"),("Maira Pr"," Porfirio T"), ("Pelayo Pr", "Porfirio T"))

print(padre.facts)

print(run(1,a,padre(a,"Yerko H")))
print(run(1,a,padre(a,"Alfredo T")))
print(run(2,b,padre("Porfirio P",b)))

print(run(1,a,primo(a,"Maira Pr")))
print(run(1,a,primo(a,"Alex H")))
print(run(2,b,primo("Yerko H",b)))

print(run(1,a,tio(a,"Alfredo T")))
print(run(1,a,tio(a,"Porfirio T")))
print(run(2,b,tio("Alex H",b)))