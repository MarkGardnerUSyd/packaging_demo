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
the help and version for the package come from the __init__.py file
- Always have an __init__.py file in each package directory - it can be empty but it should be there
'''
print(f'packge version = {MyPackage.__version__}. Package info {help(MyPackage)}')

MyPackage.sine_wave_utilities.sine_wave_plotter()

# better way to import would be:
from MyPackage.sine_wave_utilities import sine_wave_plotter