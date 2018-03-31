# Crystal Canvas
the simplest example of use will be

```python
from crstcanvas import CrystalCanvas
CrystalCanvas().draw()
```

### example 1
```python
def kernel(x,y, tone):
    tone /= (abs(x) + abs(y))*8
    return tone

CrystalCanvas(res=(300, 300), grid_res_y=10, kernel=kernel).draw()
```

### example 2
```python
def kernel(x,y, tone):
    freq = 2
    reduce = 0.4
    amp = 0.6
    scatter = 0.4

    yt = amp*sin(freq*x*3.14)
    diff = 1 - abs(yt-y)*scatter**-1
    impact = diff-reduce
    tone += impact

    return tone

CrystalCanvas(res=(600,300), grid_res_y=10, kernel=kernel).draw()
```

### example 3
```python
def kernel(x,y, tone):
    tone += abs(x)**0.5
    return 1-tone
    
CrystalCanvas(res=(300,300), grid_res_y=10, kernel=kernel).draw()
```
