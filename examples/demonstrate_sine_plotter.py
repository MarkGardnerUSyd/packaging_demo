from pathlib import Path
import sys

'''
For testing/ example purposes it's safest to manually update the path variable to ensure our 
package will always be found. This isn't necessary once we actually install the package 
because installation in python essentially means "copying the package to a place where it can be found"
'''
this_file_loc = Path(__file__)
sys.path.insert(0, str(this_file_loc.parent.parent))
#Now we can guarantee that the package will be found we can import it:
import MyPackage
'''
the help and version for the package come from the __init__.py file:
'''
# print(f'packge version = {MyPackage.__version__}. \nPackage info: {help(MyPackage)}')

x, y = MyPackage.sine_wave_utilities.generate_sine_data()
MyPackage.sine_wave_utilities.data_plotter(x, y)
#
# # since we are only using one function from this package a better way to import would be
# from MyPackage import sine_wave_utilities as swu