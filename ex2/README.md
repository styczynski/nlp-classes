# Ex 2

Niech X_F, będzie zbiorem form z SGJP, X_L zbiorem lematów z SGJP, a X_f i X_l zbiorem form i lematów z SGJP sprowadzonych do małych liter.
Niech Y_F, będzie zbiorem form z NKJP1M, Y_L zbiorem lematów z NKJP1M, a Y_f i Y_l zbiorem form i lematów z NKJP1M sprowadzonych do małych liter.
Niech f_F: Y_F -> N, będzie liczbą wystąpień formy w NKJP1M, f_L: Y_L -> N, będzie liczbą wystąpień lematu w NKJP1M, a f_f i f_l odpowiednio liczbą wystąpień form i lematów z NKJP1M sprowadzonych do małych liter.


Zadanie 1. Pokrycie SGJP na formach i lematach NKJP1M (4 pkt)
Jaki odsetek form i lematów z NKJP1M (oraz z listy frekwencyjnej NKJP1m) znajduje się w SGJP i vice versa. Co się zmieni po sprowadzeniu form do małych liter?
Formalnie:

Dla i \in {F,f,L,l} należy obliczyć wartości:
|X_i \cap Y_i| / |X_i|,
|X_i \cap Y_i| / |Y_i|,
\sum_{s \in X_i \cap Y_i} f_i(s) / \sum_{s \in Y_i} f_i(s)


Zadanie 2. Niejednoznaczność lematyzacji (2 pkt)
Forma 'lub' lematyzuje się do 'lub' i 'lubić'.
Ile jest form w SGJP, które mają niejednoznaczną lematyzację.
Co się stanie, gdy utniemy części lematów, które są po ':' ?

Zadanie 3. Niejednoznaczność lematyzacji (2 pkt)
Jaki procent form z NKJP1M lematyzowalnych za pomocą SGJP lematyzuje się jednoznacznie? Co się zmieni po sprowadzeniu form do małych liter?



Zadania dodatkowe:

1. znalezienie za pomocą Poliqarp'a znań mających sekwencję "każdy" - "pewien".
2. oszacuj średnią długość zdania w języku polskim na podstawie NKJP1M.
3. narysuj rozkład długości zdań na podstawie NKJP1M.
