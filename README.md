# Crystal Canvas
this turtle-based tiny project aims to have fun with turtle drawing library while producing an artist-stylish tool which can be used by people (especialy the geeks). the simplest use of the crystal canvas would be as followed. it randoms shade on each shard and renders triangular noise with the size of 600x240 by default.

<table>
    <tr>
        <th width="35%">Implementation</th>
        <th width="65%">Rendered Result</th>
    </tr>
    <tr>
        <td rowspan="1" align="center"> use default constructor and draw </td>
        <th rowspan="100">
            <img src="./mdsource/example_0.png">
        </th>
    </tr>
    <tr>
        <td><div class="highlight highlight-source-python"><pre>
#import the class
from crstcanvas import CrystalCanvas
        </pre></div><div class="highlight highlight-source-python"><pre>
#render it
CrystalCanvas().draw()
        </pre></div></td>
    </tr>
</table>
</br>

## Advanced Details and Examples
optionally, the **CONSTRUCTOR** of the canvas provides flexibility to control output quality and resolution.

|name       |default         |info                              |
|-----------|----------------|------------------                |
|res        |(600,240)       |render resolution                 |
|grid_res_y |3               |shards' resolution                |
|margin     |50              |htmler knows it                   |
|kernel     |lambda a,b,t: t |kernel function (explained below) |

moreover, in order to shape the canvas and form a pattern, a function(kernel) can be implemented to do so with a manner.
a **KERNEL** function accepts some parameters related to each shard draw with following details and return a density value.

|name    |info                                                          |
|--------|--------------------------------------------------------------|
|x       |relative position on x-axis within range [-1,1]               |
|y       |relative position on y-axis within range [-1,1]               |
|tone    |value within range [0.0,1.0] randomed initially for each shard|

###### Diamond Gredient Kernel
![](./mdsource/example_1.png)
```python
def kernel(x,y, tone):
    tone /= (abs(x) + abs(y))*8
    return tone
    
CrystalCanvas(kernel=kernel).draw()
```

###### Sine Wave Kernel
![](./mdsource/example_2.png)
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
```

###### Light Horizontal Gredient Kernel
![](./mdsource/example_3.png)
```python
def kernel(x,y, tone):
    tone += abs(x)**0.5
    return 1-tone
```


###### Tilted Gredient Kernel
![](./mdsource/example_4.png)
```python
def kernel(x,y, tone):
    reduce = 0.6
    slope = 3
    scatter = 1.4

    yt = slope*x
    diff = 1 - abs(yt-y)/scatter
    impact = diff - reduce

    return tone + impact
```

###### latest README.MD update : 31 March 2018 9:33pm
