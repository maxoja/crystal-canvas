# Crystal Canvas
this turtle-based tiny project aims to have fun with turtle drawing library while producing an artist-stylish tool which can be used by people, i hope. the simplest use of the crystal canvas would be as followed. by default, it randomize a shade on each shard and renders triangular noise with the size of 600x240.

<table>
    <tr>
        <th width="45%">implementation</th>
        <th width="55%">rendered result</th>
    </tr>
    <tr>
        <td colspan="2"></td>
    </tr>
    <tr>
        <td><pre>
#import the class
from crstcanvas import CrystalCanvas</pre>
            <pre>
#render it
CrystalCanvas().draw()</pre></td>
        <td>
            <img src="./mdsource/example_0.png">
        </td>
    </tr>
</table>
</br>

### Advanced Usage

> optionally, the `constructor` of CrystalCanvas() provides flexibility to control output quality and resolution.

|name       |default         |info                              |
|-----------|----------------|------------------                |
|res        |(600,240)       |render resolution                 |
|grid_res_y |3               |shards' resolution                |
|margin     |50              |htmler knows it                   |
|kernel     |lambda a,b,t: t |kernel function (explained below) |

</br>

> moreover, in order to shape the canvas and form a pattern, a function(kernel) can be implemented to do so with a manner.
> a `kernel` function accepts some parameters related to each shard draw with following details and return a density value.

|name    |info                                                             |
|--------|-----------------------------------------------------------------|
|x       |relative position on x-axis within range `[-1.0, 1.0]`           |
|y       |relative position on y-axis within range `[-1.0, 1.0]`           |
|tone    |value within range `[0.0, 1.0]` randomed initially for each shard|

</br>

### Inspirational Kernel
<table>
    <tr>
        <th width="45%">kernel</th>
        <th width="55%">rendered result</th>
    </tr>
    <tr>
        <td colspan="2"> </td>
    </tr>
    <tr>
        <td><pre>
#diamond gredient
def kernel(x,y, tone):
    divisor = (abs(x) + abs(y))*8
    return tone/divisor</pre><p align="center">CrystalCanvas(kernel=kernel).draw()</p></td>
        <td><img src="./mdsource/example_1.png"></td>
    </tr>
    <tr>
        <td colspan="2"></td>
    </tr>
    <tr>
        <td><pre>
#sine wave
def kernel(x,y, tone):
    yt = 0.6*sin(2*x*3.14)
    diff = 1 - abs(yt-y)/0.4
    impact = diff-0.4
    return tone + impact</pre><p align="center">CrystalCanvas(kernel=kernel).draw()</p></td>
        <td>
            <img src="./mdsource/example_2.png">
        </td>
    </tr>
    <tr>
        <td colspan="2"> </td>
    </tr>
    <tr>
        <td><pre>
#mellow horizontal gredient
def kernel(x,y, tone):
    addition = sqrt(abs(x))
    tone += addition
    return 1-tone</pre><p align="center">CrystalCanvas(kernel=kernel).draw()</p></td>
        <td>
            <img src="./mdsource/example_3.png">
        </td>
    </tr>
    <tr>
        <td colspan="2"></td>
    </tr>
    <tr>
        <td><div class="highlight highlight-source-python"><pre>
#tilted gredient
def kernel(x,y, tone):
    yt = 3*x
    diff = 1 - abs(yt-y)/1.4
    impact = diff - 0.6
    return tone + impact</pre><p align="center">CrystalCanvas(kernel=kernel).draw()</p></td>
        <td>
            <img src="./mdsource/example_4.png">
        </td>
    </tr>
        <tr>
        <td colspan="2"></td>
    </tr>
    <tr>
        <td><div class="highlight highlight-source-python"><pre>
#reversed tilted gredient
def kernel(x,y, tone):
    yt = 3*x
    diff = 1 - abs(yt-y)/1.4
    impact = diff - 0.6
    return 1 - (tone + impact)</pre><p align="center">CrystalCanvas(kernel=kernel).draw()</p></td>
        <td>
            <img src="./mdsource/example_5.png">
        </td>
    </tr>
</table>

###### latest README.MD update : 1 April 2018 0:26am
