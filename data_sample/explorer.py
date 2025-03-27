from pyvo.utils import activate_features

# Activate MIVOT for all tests
activate_features('MIVOT')
from pyvo.mivot.viewer.mivot_viewer import MivotViewer


m_viewer = MivotViewer(votable_path="xtapdb.xml")
while m_viewer.next():
    print(m_viewer.dm_instance)