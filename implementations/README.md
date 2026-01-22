# Reference Implementations

This folder contains working examples as annotated VOTables that cover most of the MANGO use-cases. 

- **xtapdb**:TAP query response on the 4XMMdr14 slim catalog. 
  The VOTable has been annotated on the flight by the server.
  - **file**: `xtapdb.xml`
  - **service**: `https://xcatdb.unistra.fr/xtapdb` 
  - **query**: `SELECT TOP1 * FROM "public".mergedentry`
  - **format**: `application/x-votable+xml;content=mivot` 
  
- **Gaia**:VizieR query response on the GAIA DR3 catalog. 
  The VOTable has been annotated on by hand with the Pyvo MIVOT API.
  - **file**: `gaia_with_mivot.xml`
  - **service**: `https://vizier.cds.unistra.fr/viz-bin/votable` 
  - **query**: see the `mango:origin.QueryOrigin` instance

- **datalink**:Query on an Obscore table made to exercise the mapping on both `Footprint` and `Datalink` classes. 
  The VOTable has been annotated on by hand on the project purpose.
  - **file**: `datalink.xml`
  - **service**: `https://ws.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/argus` 
  - **query**: `SELECT  TOP 1  ivoa.ObsCore.obs_id,ivoa.ObsCore.s_region,ivoa.ObsCore.access_url FROM ivoa.ObsCore`

- **vizier_cs_I_239**:Cone search response on the I/239 VizieR table. 
  The VOTable has been annotated on the flight by the server.
  - **file**: `vizier_cs_I_239.xml`
  - **service**: `https://cds/viz-bin/conesearch/V1.5/I/239/hip_main` 
  - **query**: `RA=0&DEC=0&SR=0.5`

## Feature coverage

This Table lists all MANGO classes and in which project they are implemented:

---------------------------------------------------------------------
| Class                 | xtapdb | Gaia | datalink | vizier_cs_I_239 |
|-----------------------|--------|------|----------|-----------------|
| MangoObject           | X      | X    | X        |                 |
| QueryOrigin           |        | X    |          |                 |
| EpochPosition         | X      | X    |          | X               |
| Brightness            | X      | X    |          |                 |
| Color                 | X      | X    |          |                 |
| FootPrint             |        |      | X        |                 |
| Status                | X      |      |          |                 |
| Label                 |        |      | X        |                 |
| BitField              |        |      |          |                 |
| PhysicalProperty      |        |      | X        |                 |
| DataLink              |        |      | X        |                 |
| PhotCal               | X      | X    |          |                 |
| PhotFilter            | X      | X    |          |                 |
| SpaceSys              | X      | X    |          | X               |
| TimeSys               | X      | X    |          |                 |
| PErrorSym1D           | X      | X    |          |                 |
| PErrorAsym1D          |        | X    |          |                 |
| APErrorSym2D          |        | X    |          |                 |
| Ellipse               |        |      |          |                 |
| AssociatedProperties  | X      |      |          |                 |
| AssociatedMangoObject |        |      |          |                 |
----------------------------------------------------------------------

They can be validated against the model with the Mivot validator:

```bash
% pip install mivot-validator
% mivot-instance-validate gaia_with_mivot.xml 
```

They can read with the Pyvo [model viewer](https://pyvo.readthedocs.io/en/latest/mivot/index.html):

```python
from pyvo.utils import activate_features

# Activate MIVOT feature
activate_features('MIVOT')
from pyvo.mivot.viewer.mivot_viewer import MivotViewer


m_viewer = MivotViewer(votable_path="xtapdb.xml")
while m_viewer.next():
    print(m_viewer.dm_instance)
``
