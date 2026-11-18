# Design System de BASE (copia en el repo)

La fuente de verdad de la marca es el Design System «BASE Suplementos» en claude.ai:
https://claude.ai/artifact/SRgRcmN9exDwVdXc9r6J2q

Esta carpeta guarda una copia de su `README.md` (guía de marca) y `tokens.json` (colores, tipografías,
medidas) para que la rutina diaria la lea aunque no tenga acceso al artifact.
`kit/lib.py` implementa estos mismos valores: si alguna vez difieren, mandan los de esta carpeta
y hay que actualizar `kit/lib.py`.

Si Valentín cambia el Design System, actualizá esta copia (Artifact read del artifact, paths
`project/README.md` y `project/tokens.json`) en el mismo PR del día.
