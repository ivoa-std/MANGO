# Reference Implementations

This folder contains annotated VOTables that cover most of the MANGO use-cases:


| Class                 | xtapdb | Gaia | datalink |
|-----------------------|--------|------|----------|
| MangoObject           | X      | X    | X        |
| QueryOrigin           |        | X    |          |
| EpochPosition         | X      | X    |          |
| Brightness            | X      | X    |          |
| Color                 | X      | X    |          |
| FootPrint             |        |      | X        |
| Status                | X      |      |          |
| Label                 |        |      | X        |
| BitField              |        |      |          |
| PhysicalProperty      |        |      | X        |
| DataLink              |        |      | X        |
| PhotCal               | X      | X    |          |
| PhotFilter            | X      | X    |          |
| SpaceSys              | X      | X    |          |
| TimeSys               | X      | X    |          |
| PErrorSym1D           | X      | X    |          |
| PErrorAsym1D          |        | X    |          |
| APErrorSym2D          |        | X    |          |
| Ellipse               |        |      |          |
| AssociatedMangoObject |        |      |          |
| AssociatedProperties  |        |      |          |

They can be validated against the model with the Mivot validator:

```bash
% pip install mivot-validator
% mivot-instance-validate gaia_with_mivot.xml 
```

They can read with the Pyvo [model viewer](https://pyvo.readthedocs.io/en/latest/mivot/index.html):

```python
from pyvo.utils import activate_features

# Activate MIVOT for all tests
activate_features('MIVOT')
from pyvo.mivot.viewer.mivot_viewer import MivotViewer


m_viewer = MivotViewer(votable_path="xtapdb.xml")
while m_viewer.next():
    print(m_viewer.dm_instance)
``
