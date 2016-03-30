#references
#	 http://beneathdata.com/how-to/visualizing-my-location-history/

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap
#from shapely.geometry import Point, Polygon, MultiPoint, MultiPolygon
#from shapely.prepared import prep
#import fiona
from matplotlib.collections import PatchCollection
from descartes import PolygonPatch
import json
import datetime