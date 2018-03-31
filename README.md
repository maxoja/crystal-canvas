# Crystal Canvas
the simplest use of the crystal canvas would be as followed. it randoms shade on each shard and renders triangular noise with the size of 600x240 by default.

![](./mdsource/example_0.png)
<table>
    <tr>
        <th>Implementation</th>
        <th>Rendered Result</th>
    </tr>
    <tr>
        <td><div><pre name="code" class="python">
CrystalCanvas().draw()
        </pre></div></td>
        <td>
            <img src="https://github.com/maxoja/crystal-canvas/blob/readme-and-examples/mdsource/example_0.png">
        <td>
    </tr>
</table>

## Advanced Examples
in order to shape the canvas and form a pattern, a function(kernel) can be implemented to do so with a manner.
a kernel function accepts some parameters related to each shard draw with following details and return a density value.

|name    |info        |
|--------|------------|
|x       |relative position on x-axis within range [-1,1]|
|y       |relative position on y-axis within range [-1,1] |
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
