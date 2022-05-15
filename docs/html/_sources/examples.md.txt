#  Set up examples 

If you're bothering to release your code publically, you are probably hoping someone will use it. In that case, it is integral to have some simple of examples of using your code. Create a new folder inside DemoPythonProject called ```examples```. Inside this folder create a file called ```demonstrate_sine_wave_plotter.py``` and copy the below code into it:

```python
from pathlib import Path
import sys

'''
For testing/ example purposes it's safest to manually append the path variable to ensure our 
package will always be found. This isn't necessary once we actually install the package 
because installation in python essentially means "copying the package to a place where it can be found"
'''
this_file_loc = Path(__file__)
sys.path.insert(0, str(this_file_loc.parent.parent))

'''
Now we can guarantee that the package will be found we can import it:
'''
import MyPackage

'''
the help and version for the package come from the __init__.py file:
'''
print(f'packge version = {MyPackage.__version__}. Package info {help(MyPackage)}')

MyPackage.sine_wave_utilities.sine_wave_plotter()

# since we are only using one function from this package a better way to import would be
from MyPackage.sine_wave_utilities import sine_wave_plotter
# or
from MyPackge import PlotSineWave as PSW
```



> hint: when creating examples and documentation, ask yourself 'what are some typical problems people have that I think this code can solve' and provide examples of how someone can use the code to solve such problems