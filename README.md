## Base Number

Konversi dari berbagai base number ke desimal dan sebaliknya.

Default karakter di ambil dari ASCII dengan urutan sebagai berikut:

```
Printable characters :
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Konversi dari desimal ke base-16 (hexadesimal)
```python
from basen import Basen

base16 = Basen(base=16)
base16.base_n(15).show
```
hasil :
```
F
```

### Konveri dari desimal ke base-40
```python
Basen(base=40).base_n(10).show
```
hasil :
```
A
```

```python
Basen(base=40).base_n(100).show
```
hasil :
```
2K
```

### Melihat Karakter
```python
from basen import Basen

base94 = Basen()
base94.char.show
```
hasil :
```
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Mengganti Karakter biner 0 dan 1 menjadi karakter A dan B
```python
from basen import Basen

Basen(base=2).base_n(10).show #1010

bi = Basen('AB')
bi.base_n(10).show # BABA
```
hasil :
```
1010
BABA
```

Secara default maksimal karakter adalah 94 di ambil dari Printable karakter ASCII.